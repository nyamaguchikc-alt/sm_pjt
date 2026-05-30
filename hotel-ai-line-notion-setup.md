# LINE → Notion 自動メモ保存セットアップガイド
## @hotel_ai_memo ネタ帳連携

---

## 完成イメージ

```
LINEにメモを送信
    ↓ 自動
Notionのデータベースに保存される
    ↓ 週末
Notionのリストを見てClaudeに貼り付け → 投稿文生成
```

---

## 必要なもの（すべて無料）

| ツール | 用途 | 費用 |
|---|---|---|
| LINE公式アカウント | メモを受け取るbot | 無料 |
| Make（旧Integromat） | LINEとNotionを繋ぐ | 無料プランで十分 |
| Notionデータベース | メモの保存先 | 無料 |

---

## Step 1｜LINE公式アカウントの作成（10分）

### 手順

1. [LINE Official Account Manager](https://manager.line.biz/) にアクセス
2. LINEアカウントでログイン
3. 「アカウントを作成」→ 情報を入力
   - アカウント名：`ネタ帳bot`（なんでもOK）
   - 業種：個人
4. 作成完了後、**「Messaging API」を有効化**する
   - 設定 → Messaging API → 「Messaging APIを利用する」
5. **Channel Access Token（長期）をコピーして保存**
   - LINE Developers → 該当チャンネル → Messaging API → Channel access token

### 自分のLINEと友達登録

- 公式アカウントのQRコードで自分のLINEと友達登録する
- これでLINEにメモを送ると公式アカウントが受け取れるようになる

### 自動返信をオフにする

- LINE Official Account Manager → 応答設定
- 「Webhookを使用する」→ ON
- 「応答メッセージ」→ OFF（Makeが処理するため）

---

## Step 2｜Notionデータベースの作成（5分）

### 手順

1. Notionで新規ページを作成
2. 「データベース - フルページ」を選択
3. データベース名：`ネタ帳｜hotel_ai_memo`
4. プロパティを以下に設定：

| プロパティ名 | タイプ | 用途 |
|---|---|---|
| メモ（タイトル） | タイトル | LINEで送った内容 |
| 日時 | 日付 | 送信日時 |
| カテゴリ | セレクト | 口コミ/FAQ/OTA/報告/開業 |
| ステータス | セレクト | 未使用/投稿済み/ボツ |

5. **データベースのIDをコピーして保存**
   - NotionのURL：`https://notion.so/（ここの32文字がID）`

---

## Step 3｜Notion Integrationの作成（5分）

1. [Notion Integrations](https://www.notion.so/my-integrations) にアクセス
2. 「New integration」をクリック
3. 名前：`LINE連携`
4. 「Submit」→ **Internal Integration Token をコピーして保存**
5. 作成したNotionデータベースのページに戻る
6. 右上「...」→「Connect to」→ 作成したIntegrationを選択

---

## Step 4｜Makeのシナリオ作成（20分）

### Makeアカウント作成

1. [Make.com](https://www.make.com) にアクセス
2. 無料登録（Googleアカウントでも可）

### シナリオの作成

1. 「Create a new scenario」をクリック
2. 以下の2つのモジュールを繋げる：

---

#### モジュール1：LINE（Webhookで受信）

- 「Webhooks」→「Custom webhook」を追加
- Webhookが生成される → **URLをコピー**

このURLをLINE DevelopersのWebhook URLに貼り付ける：
- LINE Developers → Messaging API → Webhook URL → 貼り付け → Verify

---

#### モジュール2：Notionに保存

- 「Notion」→「Create a Database Item」を追加
- 設定：
  - Connection：Notionと連携（Internal Integration Tokenを使用）
  - Database ID：Step 2でコピーしたID
  - プロパティのマッピング：

| Notionのプロパティ | Makeで設定する値 |
|---|---|
| メモ（タイトル） | `{{1.events[].message.text}}` |
| 日時 | `{{now}}` |
| ステータス | `未使用`（固定値） |

---

### シナリオの有効化

- 右下の「Scheduling」→「Immediately as data arrives」を選択
- 「ON」に切り替える

---

## Step 5｜動作確認（2分）

1. 自分のLINEから公式アカウントに「テストメモ」と送信
2. Notionデータベースを確認
3. 「テストメモ」が自動で追加されていればOK

---

## 完成後の使い方

### 日常のメモの送り方（毎日 1〜3分）

LINEに以下のようにメモを送るだけ：

```
口コミ分類、4軸がいいな
```

```
OTAプラン名「お得」使いすぎ問題
```

```
会議メモ、要約より宿題抽出の方が使える
```

### 週末の使い方

1. Notionの「ネタ帳」を開く
2. ステータスが「未使用」のメモを確認
3. 使うものを選んでClaude（チャット）に貼り付け
4. 投稿文を生成してもらう
5. 使ったメモのステータスを「投稿済み」に変更

---

## トラブルシューティング

| 症状 | 確認箇所 |
|---|---|
| LINEに送っても何も起きない | LINE DevelopersのWebhook URLが正しいか確認。Makeのシナリオがオンになっているか確認 |
| Notionに保存されない | NotionデータベースにIntegrationが接続されているか確認 |
| エラーが出る | Makeのシナリオのログ（「Run History」）でエラー内容を確認 |

---

## Makeの無料プランの制限

| 項目 | 無料プランの上限 |
|---|---|
| オペレーション数 | 1,000回/月 |
| シナリオ数 | 2本 |

1日3〜5件のメモなら月100〜150件程度なので、無料プランで十分。

---

*作成日：2026年5月30日*
