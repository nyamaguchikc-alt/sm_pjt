import { NextRequest, NextResponse } from "next/server";
import Anthropic from "@anthropic-ai/sdk";
import { Client } from "@notionhq/client";

const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
const notion = new Client({ auth: process.env.NOTION_API_KEY });

const LINE_API = "https://api.line.me/v2/bot/message/reply";

async function replyToLine(replyToken: string, text: string) {
  await fetch(LINE_API, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${process.env.LINE_CHANNEL_ACCESS_TOKEN}`,
    },
    body: JSON.stringify({
      replyToken,
      messages: [{ type: "text", text }],
    }),
  });
}

async function classifyMemo(text: string): Promise<{ category: string; usable: string }> {
  const message = await anthropic.messages.create({
    model: "claude-haiku-4-5-20251001",
    max_tokens: 200,
    messages: [
      {
        role: "user",
        content: `以下のメモをホテル業務AI実務アカウントの投稿ネタとして分類してください。

メモ：「${text}」

以下のJSON形式のみで返してください（他の文字は不要）：
{"category": "口コミ分析|FAQ・現場業務|OTA改善|社内報告|開業準備|その他", "usable": "高|中|低"}

categoryは最も近い1つ、usableはX投稿ネタとしての使いやすさです。`,
      },
    ],
  });

  try {
    const raw = (message.content[0] as { type: string; text: string }).text.trim();
    return JSON.parse(raw);
  } catch {
    return { category: "その他", usable: "中" };
  }
}

async function saveToNotion(text: string, category: string, usable: string) {
  await notion.pages.create({
    parent: { database_id: process.env.NOTION_DATABASE_ID! },
    properties: {
      メモ: {
        title: [{ text: { content: text } }],
      },
      日時: {
        date: { start: new Date().toISOString() },
      },
      カテゴリ: {
        select: { name: category },
      },
      ステータス: {
        select: { name: "未使用" },
      },
      使いやすさ: {
        select: { name: usable },
      },
    },
  });
}

export async function POST(req: NextRequest) {
  const body = await req.json();
  const events = body.events ?? [];

  for (const event of events) {
    if (event.type !== "message" || event.message?.type !== "text") continue;

    const text: string = event.message.text;
    const replyToken: string = event.replyToken;

    try {
      const { category, usable } = await classifyMemo(text);
      await saveToNotion(text, category, usable);

      const usableLabel = usable === "高" ? "🟢" : usable === "中" ? "🟡" : "🔴";
      await replyToLine(
        replyToken,
        `✅ 保存しました\n📂 ${category}\n${usableLabel} 使いやすさ：${usable}`
      );
    } catch (err) {
      console.error(err);
      await replyToLine(replyToken, "⚠️ 保存に失敗しました。もう一度試してください。");
    }
  }

  return NextResponse.json({ ok: true });
}
