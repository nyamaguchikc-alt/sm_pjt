from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt
import copy

# ===== カラーパレット =====
KC_NAVY    = RGBColor(0x1A, 0x2E, 0x4A)   # 霞ヶ関キャピタル風ネイビー
KC_GOLD    = RGBColor(0xC9, 0x9E, 0x3A)   # ゴールドアクセント
KC_WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
KC_LIGHT   = RGBColor(0xF2, 0xF5, 0xF9)   # ライトブルーグレー
KC_GRAY    = RGBColor(0x55, 0x65, 0x7A)
KC_RED     = RGBColor(0xC0, 0x39, 0x2B)   # 強調用
KC_GREEN   = RGBColor(0x1A, 0x8C, 0x5F)   # 効果数値用

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H

blank = prs.slide_layouts[6]  # 完全白紙レイアウト

def add_slide():
    return prs.slides.add_slide(blank)

def bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color

def box(slide, l, t, w, h, bg_color=None, border_color=None, border_pt=0):
    from pptx.util import Pt as UPt
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        Inches(l), Inches(t), Inches(w), Inches(h)
    )
    shape.line.fill.background()
    if bg_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
    else:
        shape.fill.background()
    if border_color and border_pt > 0:
        shape.line.color.rgb = border_color
        shape.line.width = UPt(border_pt)
    else:
        shape.line.fill.background()
    return shape

def txt(slide, text, l, t, w, h,
        size=18, bold=False, color=KC_WHITE,
        align=PP_ALIGN.LEFT, wrap=True, italic=False):
    txBox = slide.shapes.add_textbox(
        Inches(l), Inches(t), Inches(w), Inches(h)
    )
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return txBox

def label(slide, text, l, t, w, h, size=11, color=KC_GOLD, bold=True):
    return txt(slide, text, l, t, w, h, size=size, bold=bold, color=color,
               align=PP_ALIGN.LEFT)

def footer(slide, page_num):
    bg_shape = box(slide, 0, 7.1, 13.333, 0.4, bg_color=KC_NAVY)
    txt(slide, f"第1回 AI活用グランプリ ～ Share & Spark ～　｜　霞ヶ関キャピタル株式会社",
        0.3, 7.12, 10, 0.35, size=9, color=KC_GOLD)
    txt(slide, f"{page_num} / 8",
        12.5, 7.12, 0.8, 0.35, size=9, color=KC_WHITE, align=PP_ALIGN.RIGHT)

def section_tag(slide, text, l=0.4, t=0.15):
    b = box(slide, l, t, 2.8, 0.32, bg_color=KC_GOLD)
    txt(slide, text, l+0.08, t+0.03, 2.6, 0.28, size=10, bold=True, color=KC_NAVY)


# =====================================================
# スライド1：タイトル
# =====================================================
s1 = add_slide()
bg(s1, KC_NAVY)

# 背景装飾：右側ゴールドライン
box(s1, 9.5, 0, 3.833, 7.5, bg_color=RGBColor(0x14, 0x24, 0x3A))
box(s1, 9.45, 0, 0.06, 7.5, bg_color=KC_GOLD)

# ロゴ位置
txt(s1, "霞ヶ関キャピタル株式会社", 0.5, 0.3, 6, 0.4, size=11, color=KC_GOLD)
txt(s1, "第1回 AI活用グランプリ　活用事例部門", 0.5, 0.72, 8, 0.4, size=12, color=KC_WHITE)

# メインタイトル
txt(s1, "ホテル事業部", 0.5, 1.6, 9, 0.55, size=16, color=KC_GOLD, bold=True)
txt(s1, "AI OS", 0.5, 2.15, 9, 1.4,
    size=72, bold=True, color=KC_WHITE)

# サブタイトル
box(s1, 0.5, 3.55, 8.7, 0.06, bg_color=KC_GOLD)
txt(s1, "現場情報を、経営判断・稟議・実行指示に変換するAI業務基盤",
    0.5, 3.7, 9, 0.55, size=17, color=KC_LIGHT, bold=False)

# 発表者情報
txt(s1, "山口七星　｜　Hospitality and Culture Division",
    0.5, 6.3, 8, 0.4, size=12, color=KC_GRAY)
txt(s1, "2026年6月", 0.5, 6.65, 4, 0.3, size=11, color=KC_GRAY)

# 右側 装飾テキスト
txt(s1, "Input\n　↓\nAI処理\n　↓\nOutput\n　↓\n実行管理",
    9.8, 1.5, 3, 4, size=20, bold=True, color=KC_GOLD, align=PP_ALIGN.CENTER)

footer(s1, 1)

# =====================================================
# スライド2：取り組みの背景（課題）
# =====================================================
s2 = add_slide()
bg(s2, KC_LIGHT)

box(s2, 0, 0, 13.333, 1.2, bg_color=KC_NAVY)
section_tag(s2, "取り組みの背景", l=0.4, t=0.18)
txt(s2, "なぜAI業務OSが必要だったか：4つの構造的課題",
    0.4, 0.45, 12, 0.55, size=22, bold=True, color=KC_WHITE)

# 4課題ボックス
issues = [
    ("01", "情報の属人化",
     "Teams・PMS・会議メモ・OTA・ベンダー見積が散在\n優先順位の判断が担当者経験に完全依存"),
    ("02", "報告品質のばらつき",
     "論点整理の深さ・経営向けの見せ方に担当者差\n差し戻し・再考の時間が発生"),
    ("03", "専門知識への依存",
     "要件定義・市場調査・SNS戦略・価格施策を\n外部委託または専門人材に依存"),
    ("04", "施策実行スピードの低下",
     "報告・稟議・準備に時間がかかり\n価格施策・開業準備の意思決定頻度が限定"),
]

positions = [(0.35, 1.35), (6.85, 1.35), (0.35, 4.0), (6.85, 4.0)]
for (num, title, body), (lx, ty) in zip(issues, positions):
    box(s2, lx, ty, 6.2, 2.5, bg_color=KC_NAVY)
    box(s2, lx, ty, 0.65, 2.5, bg_color=KC_GOLD)
    txt(s2, num, lx+0.08, ty+0.85, 0.55, 0.7, size=26, bold=True, color=KC_NAVY, align=PP_ALIGN.CENTER)
    txt(s2, title, lx+0.75, ty+0.15, 5.3, 0.5, size=17, bold=True, color=KC_GOLD)
    txt(s2, body, lx+0.75, ty+0.65, 5.3, 1.7, size=13, color=KC_WHITE)

footer(s2, 2)

# =====================================================
# スライド3：全体像（解決策）
# =====================================================
s3 = add_slide()
bg(s3, KC_LIGHT)

box(s3, 0, 0, 13.333, 1.2, bg_color=KC_NAVY)
section_tag(s3, "応募内容の概要", l=0.4, t=0.18)
txt(s3, "ホテル事業部の業務OS化：情報を判断材料に変換するフロー",
    0.4, 0.45, 12, 0.55, size=22, bold=True, color=KC_WHITE)

# フロー図
flow_items = [
    ("INPUT", "現場メモ\n売上数値\n会議内容\nベンダー論点", KC_GRAY),
    ("AI処理", "論点整理\n構造化\n言語変換\nToDo化", KC_NAVY),
    ("OUTPUT", "役員報告\n稟議文案\n週次レポート\n価格施策", KC_GREEN),
    ("実行管理", "Notion連携\n進捗管理\n承認サマリー\n宿題管理", RGBColor(0x5B, 0x4F, 0xA0)),
]

for i, (title, body, col) in enumerate(flow_items):
    lx = 0.35 + i * 3.25
    box(s3, lx, 1.35, 2.9, 4.5, bg_color=col)
    txt(s3, title, lx, 1.38, 2.9, 0.7, size=18, bold=True, color=KC_WHITE, align=PP_ALIGN.CENTER)
    box(s3, lx+0.1, 2.05, 2.7, 0.06, bg_color=KC_GOLD)
    txt(s3, body, lx+0.15, 2.15, 2.65, 3.5, size=14, color=KC_WHITE)
    if i < 3:
        txt(s3, "→", lx+2.88, 2.95, 0.4, 0.6, size=28, bold=True, color=KC_GOLD, align=PP_ALIGN.CENTER)

# ポイント
box(s3, 0.35, 6.0, 12.65, 0.75, bg_color=KC_NAVY)
txt(s3, "💡 ポイント：AIを単発利用で終わらせず、入力・処理・出力・実行管理の業務フローに完全組込み。属人的だった「考える・整理する・判断材料にする」プロセスを再現可能な業務基盤として設計。",
    0.5, 6.05, 12.3, 0.65, size=12, color=KC_GOLD)

footer(s3, 3)

# =====================================================
# スライド4：デモ予告
# =====================================================
s4 = add_slide()
bg(s4, KC_NAVY)

# 装飾
box(s4, 0, 3.2, 13.333, 0.08, bg_color=KC_GOLD)

txt(s4, "LIVE DEMO", 0, 0.6, 13.333, 1.4, size=80, bold=True,
    color=RGBColor(0xFF, 0xFF, 0xFF), align=PP_ALIGN.CENTER)

box(s4, 2.5, 2.0, 8.333, 0.9, bg_color=KC_GOLD)
txt(s4, "事例D：11スキル連携によるインバウンド戦略内製化",
    2.5, 2.0, 8.333, 0.9, size=18, bold=True, color=KC_NAVY, align=PP_ALIGN.CENTER)

txt(s4, "外部代理店に委託していた「市場調査→戦略設計→コンテンツ制作」を\n担当者単独でゼロから完結させる業務フローを、今この場で動かします。",
    1.0, 3.45, 11.333, 1.2, size=16, color=KC_LIGHT, align=PP_ALIGN.CENTER)

# 11スキル一覧（小さく）
skills = [
    "① competitive-intelligence", "② source-validation", "③ knowledge-structuring",
    "④ deep-research-synthesizer", "⑤ flowchart-decision-builder", "⑥ scqa-writing-framework",
    "⑦ workflow-automation-agent", "⑧ hook-generator", "⑨ structured-copywriting",
    "⑩ content-repurposing-engine", "⑪ tone-style-enforcer  ← LIVE"
]
cols = 3
for i, sk in enumerate(skills):
    col = i % cols
    row = i // cols
    lx = 0.8 + col * 4.1
    ty = 4.8 + row * 0.38
    clr = KC_GOLD if "LIVE" in sk else KC_GRAY
    bld = True if "LIVE" in sk else False
    txt(s4, sk, lx, ty, 3.9, 0.36, size=11, color=clr, bold=bld)

footer(s4, 4)

# =====================================================
# スライド5：デモ実行（プレースホルダー）
# =====================================================
s5 = add_slide()
bg(s5, RGBColor(0x08, 0x10, 0x1A))

txt(s5, "[ DEMO ]", 0, 0.2, 13.333, 0.9, size=52, bold=True,
    color=KC_GOLD, align=PP_ALIGN.CENTER)
txt(s5, "ここでライブデモを実行",
    0, 1.1, 13.333, 0.6, size=22, color=KC_WHITE, align=PP_ALIGN.CENTER)

# 進行ガイド（発表者向け・小文字）
steps = [
    ("0〜50秒", "早送り録画再生（スキル①〜⑩）", KC_GRAY),
    ("50〜55秒", "「最後のスキル⑪をライブで実行します」と宣言", KC_GOLD),
    ("55〜65秒", "11_tone_style_enforcer_input_LIVE.txtを貼り付け→実行", KC_GOLD),
    ("65〜75秒", "出力表示を会場に見せる（沈黙OK）", KC_GREEN),
    ("75〜80秒", "「3パターン完成。これが代理店に頼んでいた仕事です」", KC_GREEN),
]
for i, (timing, action, col) in enumerate(steps):
    ty = 1.9 + i * 0.88
    box(s5, 1.0, ty, 1.5, 0.7, bg_color=col)
    txt(s5, timing, 1.0, ty+0.1, 1.5, 0.55, size=12, bold=True, color=KC_NAVY, align=PP_ALIGN.CENTER)
    txt(s5, action, 2.65, ty+0.1, 10.0, 0.55, size=14, color=KC_WHITE)

txt(s5, "⚠ 失敗時：「念のため事前収録でお見せします」→ タブBに切替",
    0.5, 6.4, 12.5, 0.45, size=11, color=KC_RED, italic=True)

footer(s5, 5)

# =====================================================
# スライド6：効果数値
# =====================================================
s6 = add_slide()
bg(s6, KC_LIGHT)

box(s6, 0, 0, 13.333, 1.2, bg_color=KC_NAVY)
section_tag(s6, "期待効果", l=0.4, t=0.18)
txt(s6, "数字で見る成果：4事例平均 約76%の工数削減",
    0.4, 0.45, 12, 0.55, size=22, bold=True, color=KC_WHITE)

metrics = [
    ("週次レポート\n作成時間", "週150分", "週30分", "▲80%"),
    ("週次アジェンダ\n更新時間", "週60分", "週5分", "▲92%"),
    ("ベンダー要件定義\n・対応工数", "週15〜20h", "週6h", "▲70%"),
    ("市場調査\n戦略立案コスト", "数百万円〜\n（代理店）", "0円\n（AI内製）", "▲100%"),
    ("同時進行できる\n開業準備物件", "1物件", "3物件", "3倍"),
    ("価格施策\n検討頻度", "月1回", "週次", "4倍以上"),
]

for i, (item, before, after, effect) in enumerate(metrics):
    col = i % 3
    row = i // 3
    lx = 0.35 + col * 4.3
    ty = 1.35 + row * 2.55

    box(s6, lx, ty, 4.0, 2.3, bg_color=KC_NAVY)
    txt(s6, item, lx+0.1, ty+0.1, 3.8, 0.65, size=12, bold=True, color=KC_GOLD)
    txt(s6, f"Before: {before}", lx+0.1, ty+0.75, 3.8, 0.55, size=11, color=KC_GRAY)
    txt(s6, f"After:  {after}",  lx+0.1, ty+1.25, 3.8, 0.55, size=11, color=KC_WHITE)
    box(s6, lx+2.5, ty+0.08, 1.4, 0.55, bg_color=KC_GREEN)
    txt(s6, effect, lx+2.5, ty+0.08, 1.4, 0.55, size=17, bold=True, color=KC_WHITE, align=PP_ALIGN.CENTER)

footer(s6, 6)

# =====================================================
# スライド7：横展開ロードマップ
# =====================================================
s7 = add_slide()
bg(s7, KC_LIGHT)

box(s7, 0, 0, 13.333, 1.2, bg_color=KC_NAVY)
section_tag(s7, "実現性・横展開", l=0.4, t=0.18)
txt(s7, "KC全社への展開：4点の標準化で7部門に適用可能",
    0.4, 0.45, 12, 0.55, size=22, bold=True, color=KC_WHITE)

# 4点の標準化
items4 = ["プロンプト集", "入力フォーマット", "出力フォーマット", "利用ルール（ガバナンス）"]
for i, item in enumerate(items4):
    lx = 0.35 + i * 3.25
    box(s7, lx, 1.3, 3.0, 0.7, bg_color=KC_GOLD)
    txt(s7, f"0{i+1}  {item}", lx+0.1, 1.35, 2.8, 0.6, size=13, bold=True, color=KC_NAVY)

txt(s7, "→ この4点を整備するだけで全部署に横展開可能",
    0.4, 2.05, 12, 0.4, size=13, color=KC_NAVY, bold=True)

# 7部署
depts = [
    ("投資・不動産", "物件論点整理・投資判断・リスク抽出・稟議文案"),
    ("開発・建設",   "工事/設計/ベンダー要件定義・進捗報告"),
    ("経理・財務",   "請求・証憑リスク整理・稟議変換"),
    ("法務・コンプラ","契約書レビュー・リスク分類・確認事項"),
    ("営業",         "商談メモ→提案書・顧客別アプローチ整理"),
    ("情シス・AILAB","要件定義・ベンダー対応・仕様書作成"),
    ("経営企画／人事","会議ログ論点整理・役員サマリー・求人票"),
]
for i, (dept, body) in enumerate(depts):
    col = i % 4
    row = i // 4
    lx = 0.35 + col * 3.25
    ty = 2.6 + row * 1.95
    box(s7, lx, ty, 3.0, 1.8, bg_color=KC_NAVY)
    txt(s7, dept, lx+0.1, ty+0.1, 2.8, 0.45, size=13, bold=True, color=KC_GOLD)
    txt(s7, body, lx+0.1, ty+0.55, 2.8, 1.1, size=10, color=KC_WHITE)

# ガバナンス注記
box(s7, 0.35, 6.55, 12.65, 0.55, bg_color=RGBColor(0x2C, 0x3E, 0x50))
txt(s7, "🔒 ガバナンス：投入前マスキングルール整備 ／ 学習使用なし契約プラン利用 ／ 情シス・AILABと利用ガイドライン共同策定中",
    0.5, 6.58, 12.3, 0.48, size=10, color=KC_GOLD)

footer(s7, 7)

# =====================================================
# スライド8：まとめ
# =====================================================
s8 = add_slide()
bg(s8, KC_NAVY)

box(s8, 0, 2.8, 13.333, 0.08, bg_color=KC_GOLD)

txt(s8, "AIの価値は、文章をきれいにすることではありません。",
    0.5, 0.5, 12.333, 0.85, size=24, bold=True, color=KC_WHITE, align=PP_ALIGN.CENTER)
txt(s8, "現場に散らばる情報を、意思決定できる状態に変換することです。",
    0.5, 1.35, 12.333, 0.85, size=24, bold=True, color=KC_GOLD, align=PP_ALIGN.CENTER)

# 3つの実績
results = [
    ("76%\n工数削減", "4事例平均"),
    ("0円\n内製化", "代理店費→AI"),
    ("3倍\n同時推進", "開業準備物件数"),
]
for i, (num, sub) in enumerate(results):
    lx = 1.5 + i * 3.7
    box(s8, lx, 3.1, 3.2, 2.0, bg_color=RGBColor(0x14, 0x24, 0x3A))
    box(s8, lx, 3.1, 3.2, 0.06, bg_color=KC_GOLD)
    txt(s8, num, lx, 3.2, 3.2, 1.2, size=32, bold=True, color=KC_GOLD, align=PP_ALIGN.CENTER)
    txt(s8, sub, lx, 4.35, 3.2, 0.5, size=12, color=KC_GRAY, align=PP_ALIGN.CENTER)

txt(s8, "ホテル事業部で実証したこのモデルを、KC全社の業務品質底上げに展開します。",
    0.5, 5.3, 12.333, 0.6, size=16, color=KC_LIGHT, align=PP_ALIGN.CENTER)

txt(s8, "ご清聴ありがとうございました",
    0.5, 6.0, 12.333, 0.5, size=18, bold=True, color=KC_WHITE, align=PP_ALIGN.CENTER)

footer(s8, 8)

# =====================================================
# 保存
# =====================================================
out_path = "/home/user/sm_pjt/presentation/KASUMIGASEKI_AI_OS_Final_Presentation.pptx"
prs.save(out_path)
print(f"Saved: {out_path}")
print(f"Slides: {len(prs.slides)}")
