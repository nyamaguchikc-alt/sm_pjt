import { Suspense } from "react";
import { notFound } from "next/navigation";
import Link from "next/link";
import { calculateFourPillars, ELEMENT_COLORS, ELEMENT_BG } from "@/lib/fourPillars";
import { getZodiacSign, getChineseZodiac } from "@/lib/westernAstrology";

interface ResultPageProps {
  searchParams: { year?: string; month?: string; day?: string; gender?: string; hour?: string };
}

function ElementBar({ element, count, total }: { element: string; count: number; total: number }) {
  const pct = total > 0 ? Math.round((count / total) * 100) : 0;
  const color = ELEMENT_COLORS[element] || "#888";
  return (
    <div className="flex items-center gap-3">
      <span className="w-5 text-sm font-bold text-center" style={{ color }}>{element}</span>
      <div className="flex-1 h-2 rounded-full bg-white/5 overflow-hidden">
        <div
          className="h-full rounded-full transition-all"
          style={{ width: `${pct}%`, background: color, boxShadow: `0 0 8px ${color}60` }}
        />
      </div>
      <span className="text-xs w-6 text-right" style={{ color: "var(--text-secondary)" }}>{count}</span>
    </div>
  );
}

function PillarColumn({
  label,
  pillar,
}: {
  label: string;
  pillar: { stem: string; branch: string; stemElement: string; branchElement: string; yinYang: string; animal: string } | null;
}) {
  if (!pillar) {
    return (
      <div className="pillar-card opacity-40">
        <div className="text-xs text-white/30 mb-2 tracking-widest">{label}</div>
        <div className="pillar-stem text-white/20">—</div>
        <div className="pillar-branch text-white/20">—</div>
        <div className="text-xs text-white/20 mt-1">不明</div>
      </div>
    );
  }
  const stemColor = ELEMENT_COLORS[pillar.stemElement];
  const branchColor = ELEMENT_COLORS[pillar.branchElement];
  return (
    <div className="pillar-card">
      <div className="text-xs tracking-widest mb-2" style={{ color: "var(--text-secondary)" }}>{label}</div>
      <div className="pillar-stem" style={{ color: stemColor, textShadow: `0 0 12px ${stemColor}80` }}>
        {pillar.stem}
      </div>
      <div className="text-xs mb-2" style={{ color: stemColor + "99" }}>
        {pillar.yinYang}{pillar.stemElement}
      </div>
      <div className="w-px h-4 bg-white/10 mx-auto mb-2" />
      <div className="pillar-branch" style={{ color: branchColor, textShadow: `0 0 12px ${branchColor}80` }}>
        {pillar.branch}
      </div>
      <div className="text-xs" style={{ color: branchColor + "99" }}>
        {pillar.animal}
      </div>
    </div>
  );
}

function ResultContent({ searchParams }: ResultPageProps) {
  const year = Number(searchParams.year);
  const month = Number(searchParams.month);
  const day = Number(searchParams.day);
  const gender = searchParams.gender || "male";
  const hourStr = searchParams.hour;
  const hour = hourStr !== undefined && hourStr !== "" ? Number(hourStr) : undefined;

  if (!year || !month || !day || year < 1924 || year > new Date().getFullYear()) {
    notFound();
  }

  const fourPillars = calculateFourPillars(year, month, day, hour);
  const zodiac = getZodiacSign(month, day);
  const chineseZodiac = getChineseZodiac(year);

  const genderLabel = gender === "male" ? "男性" : "女性";
  const elementTotals = Object.values(fourPillars.elementBalance.counts).reduce((a, b) => a + b, 0);

  const elementEmojis: Record<string, string> = {
    木: "🌿",
    火: "🔥",
    土: "🌾",
    金: "⚔️",
    水: "💧",
  };

  return (
    <main className="min-h-screen px-4 py-12 max-w-3xl mx-auto">
      {/* ヘッダー */}
      <div className="text-center mb-10 slide-up">
        <Link href="/" className="inline-flex items-center gap-1.5 text-xs tracking-widest text-amber-400/50 hover:text-amber-400/80 transition-colors mb-6">
          ← 最初に戻る
        </Link>
        <div className="text-4xl mb-3" style={{ filter: "drop-shadow(0 0 20px rgba(201,162,39,0.7))" }}>✦</div>
        <h1
          className="font-serif text-3xl md:text-4xl font-bold mb-2 tracking-widest"
          style={{
            fontFamily: "'Noto Serif JP', serif",
            background: "linear-gradient(135deg, #f0d060, #c9a227, #f5e88a)",
            WebkitBackgroundClip: "text",
            WebkitTextFillColor: "transparent",
            backgroundClip: "text",
          }}
        >
          命式鑑定書
        </h1>
        <p className="text-sm tracking-widest text-amber-400/50">Fortune Reading</p>
      </div>

      {/* 基本情報 */}
      <div className="glass-card p-5 mb-6 slide-up delay-100">
        <div className="flex flex-wrap items-center gap-x-6 gap-y-2 justify-center text-sm">
          <span style={{ color: "var(--text-secondary)" }}>
            <span className="text-amber-400/60 mr-1">生年月日</span>
            {year}年{month}月{day}日
          </span>
          <span style={{ color: "var(--text-secondary)" }}>
            <span className="text-amber-400/60 mr-1">性別</span>{genderLabel}
          </span>
          <span style={{ color: "var(--text-secondary)" }}>
            <span className="text-amber-400/60 mr-1">干支</span>{chineseZodiac}年生まれ
          </span>
          <span style={{ color: "var(--text-secondary)" }}>
            <span className="text-amber-400/60 mr-1">星座</span>{zodiac.symbol} {zodiac.name}
          </span>
        </div>
      </div>

      {/* ━━━━━ 四柱推命 ━━━━━ */}
      <section className="mb-6 slide-up delay-200">
        <div className="glass-card-strong p-6 md:p-8">
          <div className="flex items-center gap-3 mb-6">
            <div className="h-px flex-1 bg-gradient-to-r from-transparent to-amber-400/20" />
            <h2 className="section-title text-amber-300 whitespace-nowrap">
              ☰ 四柱推命
            </h2>
            <div className="h-px flex-1 bg-gradient-to-l from-transparent to-amber-400/20" />
          </div>

          {/* 命式表 */}
          <div className="grid grid-cols-4 gap-2 mb-8">
            <PillarColumn label="年柱" pillar={fourPillars.year} />
            <PillarColumn label="月柱" pillar={fourPillars.month} />
            <PillarColumn label="日柱" pillar={fourPillars.day} />
            <PillarColumn label="時柱" pillar={fourPillars.hour} />
          </div>

          {/* 日主 */}
          <div
            className="rounded-xl p-5 mb-6"
            style={{
              background: ELEMENT_BG[fourPillars.dayMaster.element] || "rgba(255,255,255,0.03)",
              border: `1px solid ${ELEMENT_COLORS[fourPillars.dayMaster.element]}30`,
            }}
          >
            <div className="flex items-start gap-4">
              <div
                className="text-3xl font-serif font-bold rounded-xl w-14 h-14 flex items-center justify-center flex-shrink-0"
                style={{
                  color: ELEMENT_COLORS[fourPillars.dayMaster.element],
                  background: ELEMENT_BG[fourPillars.dayMaster.element],
                  border: `1px solid ${ELEMENT_COLORS[fourPillars.dayMaster.element]}40`,
                  fontFamily: "'Noto Serif JP', serif",
                  textShadow: `0 0 16px ${ELEMENT_COLORS[fourPillars.dayMaster.element]}`,
                }}
              >
                {fourPillars.dayMaster.stem}
              </div>
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs tracking-widest text-amber-400/50">日主（あなたの本質）</span>
                  <span
                    className="text-xs px-2 py-0.5 rounded-full"
                    style={{
                      background: ELEMENT_BG[fourPillars.dayMaster.element],
                      color: ELEMENT_COLORS[fourPillars.dayMaster.element],
                      border: `1px solid ${ELEMENT_COLORS[fourPillars.dayMaster.element]}40`,
                    }}
                  >
                    {elementEmojis[fourPillars.dayMaster.element]} {fourPillars.dayMaster.element}行 {fourPillars.dayMaster.yinYang}
                  </span>
                </div>
                <h3
                  className="font-serif font-bold text-lg mb-2"
                  style={{ fontFamily: "'Noto Serif JP', serif", color: "var(--text-primary)" }}
                >
                  {fourPillars.dayMaster.title}
                </h3>
                <p className="text-sm leading-relaxed" style={{ color: "var(--text-secondary)" }}>
                  {fourPillars.dayMaster.personality}
                </p>
              </div>
            </div>
          </div>

          {/* 強み・課題 */}
          <div className="grid md:grid-cols-2 gap-4 mb-6">
            <div className="rounded-xl p-4 bg-white/3 border border-white/5">
              <h4 className="text-xs tracking-widest text-emerald-400/70 mb-3">強み</h4>
              <ul className="space-y-1.5">
                {fourPillars.dayMaster.strengths.map((s) => (
                  <li key={s} className="flex items-center gap-2 text-sm" style={{ color: "var(--text-secondary)" }}>
                    <span className="text-emerald-400 text-xs">◆</span>{s}
                  </li>
                ))}
              </ul>
            </div>
            <div className="rounded-xl p-4 bg-white/3 border border-white/5">
              <h4 className="text-xs tracking-widest text-rose-400/70 mb-3">課題</h4>
              <ul className="space-y-1.5">
                {fourPillars.dayMaster.challenges.map((c) => (
                  <li key={c} className="flex items-center gap-2 text-sm" style={{ color: "var(--text-secondary)" }}>
                    <span className="text-rose-400 text-xs">◆</span>{c}
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* 五行バランス */}
          <div className="rounded-xl p-4 bg-white/3 border border-white/5 mb-6">
            <h4 className="text-xs tracking-widest text-amber-400/60 mb-4">五行バランス</h4>
            <div className="space-y-2.5">
              {Object.entries(fourPillars.elementBalance.counts).map(([el, cnt]) => (
                <ElementBar key={el} element={el} count={cnt} total={elementTotals} />
              ))}
            </div>
            <p className="mt-3 text-xs leading-relaxed" style={{ color: "var(--text-secondary)" }}>
              {fourPillars.elementBalance.analysis}
            </p>
          </div>

          {/* 命式の運勢 */}
          <div className="rounded-xl p-4 bg-gradient-to-br from-amber-400/5 to-transparent border border-amber-400/15">
            <h4 className="text-xs tracking-widest text-amber-400/70 mb-2">命式の運勢</h4>
            <p className="text-sm leading-relaxed" style={{ color: "var(--text-secondary)" }}>
              {fourPillars.dayMaster.fortune}
            </p>
          </div>

          {/* 流年運 */}
          <div className="rounded-xl p-4 bg-gradient-to-br from-purple-400/5 to-transparent border border-purple-400/15 mt-4">
            <h4 className="text-xs tracking-widest text-purple-400/70 mb-2">
              {new Date().getFullYear()}年の運勢（流年）
            </h4>
            <p className="text-sm leading-relaxed" style={{ color: "var(--text-secondary)" }}>
              {fourPillars.yearFortune}
            </p>
          </div>
        </div>
      </section>

      {/* ━━━━━ 西洋占星術 ━━━━━ */}
      <section className="mb-6 slide-up delay-300">
        <div className="glass-card-strong p-6 md:p-8">
          <div className="flex items-center gap-3 mb-6">
            <div className="h-px flex-1 bg-gradient-to-r from-transparent to-purple-400/20" />
            <h2 className="section-title text-purple-300 whitespace-nowrap">
              ☽ 西洋占星術
            </h2>
            <div className="h-px flex-1 bg-gradient-to-l from-transparent to-purple-400/20" />
          </div>

          {/* 星座ヘッダー */}
          <div className="flex items-center gap-5 mb-6 p-5 rounded-xl bg-white/3 border border-purple-400/15">
            <div className="text-6xl flex-shrink-0" style={{ filter: "drop-shadow(0 0 16px rgba(167,139,250,0.5))" }}>
              {zodiac.symbol}
            </div>
            <div className="flex-1">
              <div className="text-xs tracking-widest text-purple-400/50 mb-1">太陽星座</div>
              <h3 className="font-serif text-2xl font-bold text-purple-200 mb-1" style={{ fontFamily: "'Noto Serif JP', serif" }}>
                {zodiac.name}
              </h3>
              <p className="text-sm text-purple-300/50">{zodiac.nameEn} · {zodiac.dateRange}</p>
              <div className="flex flex-wrap gap-2 mt-2">
                <span className="text-xs px-2 py-0.5 rounded-full bg-purple-400/10 text-purple-300/70 border border-purple-400/20">
                  {zodiac.element}のエレメント
                </span>
                <span className="text-xs px-2 py-0.5 rounded-full bg-purple-400/10 text-purple-300/70 border border-purple-400/20">
                  {zodiac.rulingPlanetEmoji} {zodiac.rulingPlanet}支配
                </span>
                <span className="text-xs px-2 py-0.5 rounded-full bg-purple-400/10 text-purple-300/70 border border-purple-400/20">
                  {zodiac.quality}
                </span>
              </div>
            </div>
          </div>

          {/* 性格 */}
          <div className="mb-4 p-4 rounded-xl bg-white/3 border border-white/5">
            <h4 className="text-xs tracking-widest text-purple-400/60 mb-2">性格・特徴</h4>
            <p className="text-sm leading-relaxed" style={{ color: "var(--text-secondary)" }}>
              {zodiac.personality}
            </p>
          </div>

          {/* 強み・課題 */}
          <div className="grid md:grid-cols-2 gap-4 mb-4">
            <div className="rounded-xl p-4 bg-white/3 border border-white/5">
              <h4 className="text-xs tracking-widest text-emerald-400/70 mb-3">強み</h4>
              <ul className="space-y-1.5">
                {zodiac.strengths.map((s) => (
                  <li key={s} className="flex items-center gap-2 text-sm" style={{ color: "var(--text-secondary)" }}>
                    <span className="text-emerald-400 text-xs">◆</span>{s}
                  </li>
                ))}
              </ul>
            </div>
            <div className="rounded-xl p-4 bg-white/3 border border-white/5">
              <h4 className="text-xs tracking-widest text-rose-400/70 mb-3">課題</h4>
              <ul className="space-y-1.5">
                {zodiac.challenges.map((c) => (
                  <li key={c} className="flex items-center gap-2 text-sm" style={{ color: "var(--text-secondary)" }}>
                    <span className="text-rose-400 text-xs">◆</span>{c}
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* 各運勢 */}
          <div className="grid md:grid-cols-2 gap-4 mb-4">
            {[
              { label: "恋愛運 ❤", text: zodiac.love, color: "rose" },
              { label: "仕事運 💼", text: zodiac.career, color: "blue" },
              { label: "金運 💰", text: zodiac.money, color: "amber" },
              { label: "健康運 🌿", text: zodiac.health, color: "emerald" },
            ].map(({ label, text, color }) => (
              <div key={label} className="rounded-xl p-4 bg-white/3 border border-white/5">
                <h4 className={`text-xs tracking-widest text-${color}-400/70 mb-2`}>{label}</h4>
                <p className="text-sm leading-relaxed" style={{ color: "var(--text-secondary)" }}>
                  {text}
                </p>
              </div>
            ))}
          </div>

          {/* ラッキー情報 */}
          <div className="rounded-xl p-4 bg-white/3 border border-white/5 mb-4">
            <h4 className="text-xs tracking-widest text-amber-400/60 mb-3">ラッキー情報</h4>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
              {[
                { label: "カラー", value: zodiac.lucky.color },
                { label: "ナンバー", value: String(zodiac.lucky.number) },
                { label: "曜日", value: zodiac.lucky.day },
                { label: "ストーン", value: zodiac.lucky.stone },
              ].map(({ label, value }) => (
                <div key={label} className="text-center">
                  <div className="text-xs text-amber-400/40 mb-1">{label}</div>
                  <div className="text-sm font-medium" style={{ color: "var(--text-primary)" }}>{value}</div>
                </div>
              ))}
            </div>
          </div>

          {/* 総合運 */}
          <div className="rounded-xl p-4 bg-gradient-to-br from-purple-400/5 to-transparent border border-purple-400/15">
            <h4 className="text-xs tracking-widest text-purple-400/70 mb-2">総合運</h4>
            <p className="text-sm leading-relaxed" style={{ color: "var(--text-secondary)" }}>
              {zodiac.overallFortune}
            </p>
          </div>
        </div>
      </section>

      {/* ━━━━━ 総合メッセージ ━━━━━ */}
      <section className="mb-10 slide-up delay-400">
        <div
          className="glass-card p-6 text-center"
          style={{
            background: "linear-gradient(135deg, rgba(201,162,39,0.06), rgba(167,139,250,0.06))",
            border: "1px solid rgba(201,162,39,0.2)",
          }}
        >
          <div className="text-3xl mb-3" style={{ filter: "drop-shadow(0 0 12px rgba(201,162,39,0.6))" }}>✦</div>
          <h3 className="font-serif text-lg font-bold text-amber-300 mb-3 tracking-wider" style={{ fontFamily: "'Noto Serif JP', serif" }}>
            あなたへのメッセージ
          </h3>
          <p className="text-sm leading-relaxed max-w-lg mx-auto" style={{ color: "var(--text-secondary)" }}>
            四柱推命の{fourPillars.dayMaster.element}行{fourPillars.dayMaster.yinYang}の日主と、
            {zodiac.name}の{zodiac.element}のエネルギーが融合した命式を持つあなたは、
            {fourPillars.overallFortune}
          </p>
          <div className="mt-4 pt-4 border-t border-white/5">
            <p className="text-xs" style={{ color: "var(--text-secondary)", opacity: 0.5 }}>
              ※ 占いは参考としてお楽しみください。時柱は出生時間が不明な場合、省略されます。
            </p>
          </div>
        </div>
      </section>

      {/* 戻るボタン */}
      <div className="text-center slide-up delay-500">
        <Link
          href="/"
          className="inline-flex items-center gap-2 py-3 px-8 rounded-full border border-amber-400/30 text-amber-400/70 hover:border-amber-400/60 hover:text-amber-300 transition-all duration-200 text-sm tracking-wider"
        >
          ← もう一度占う
        </Link>
      </div>
    </main>
  );
}

export default function ResultPage(props: ResultPageProps) {
  return (
    <Suspense fallback={
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="text-4xl mb-4 animate-pulse">✦</div>
          <p className="text-amber-400/60 tracking-widest text-sm">鑑定中...</p>
        </div>
      </div>
    }>
      <ResultContent {...props} />
    </Suspense>
  );
}
