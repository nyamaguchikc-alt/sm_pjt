from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

KC_NAVY  = RGBColor(0x1A, 0x2E, 0x4A)
KC_GOLD  = RGBColor(0xC9, 0x9E, 0x3A)
KC_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
KC_LIGHT = RGBColor(0xF2, 0xF5, 0xF9)
KC_GRAY  = RGBColor(0x55, 0x65, 0x7A)
KC_RED   = RGBColor(0xC0, 0x39, 0x2B)
KC_GREEN = RGBColor(0x1A, 0x8C, 0x5F)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H
blank = prs.slide_layouts[6]

def add_slide(): return prs.slides.add_slide(blank)

def bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color

def box(slide, l, t, w, h, bg_color=None):
    shape = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    if bg_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
    else:
        shape.fill.background()
    shape.line.fill.background()
    return shape

def txt(slide, text, l, t, w, h, size=18, bold=False, color=KC_WHITE,
        align=PP_ALIGN.LEFT, italic=False):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return tb

def footer(slide, n):
    box(slide, 0, 7.1, 13.333, 0.4, bg_color=KC_NAVY)
    txt(slide, "第1回 AI活用グランプリ ～ Share & Spark ～　｜　霞ヶ関キャピタル株式会社",
        0.3, 7.12, 10, 0.35, size=9, color=KC_GOLD)
    txt(slide, f"{n} / 8", 12.5, 7.12, 0.8, 0.35, size=9, color=KC_WHITE, align=PP_ALIGN.RIGHT)

def section_tag(slide, text, l=0.4, t=0.18):
    box(slide, l, t, 3.0, 0.32, bg_color=KC_GOLD)
    txt(slide, text, l+0.08, t+0.03, 2.8, 0.28, size=10, bold=True, color=KC_NAVY)

# =====================================================
# S1 タイトル
# =====================================================
s1 = add_slide()
bg(s1, KC_NAVY)
box(s1, 9.5, 0, 3.833, 7.5, bg_color=RGBColor(0x14, 0x24, 0x3A))
box(s1, 9.45, 0, 0.06, 7.5, bg_color=KC_GOLD)
txt(s1, "霞ヶ関キャピタル株式会社", 0.5, 0.3, 6, 0.4, size=11, color=KC_GOLD)
txt(s1, "第1回 AI活用グランプリ　活用事例部門", 0.5, 0.72, 8, 0.4, size=12, color=KC_WHITE)
txt(s1, "ホテル事業部", 0.5, 1.6, 9, 0.55, size=16, color=KC_GOLD, bold=True)
txt(s1, "AI OS", 0.5, 2.15, 9, 1.4, size=72, bold=True, color=KC_WHITE)
box(s1, 0.5, 3.55, 8.7, 0.06, bg_color=KC_GOLD)
txt(s1, "現場情報を、経営判断・稟議・実行指示に変換するAI業務基盤",
    0.5, 3.7, 9, 0.55, size=17, color=KC_LIGHT)
txt(s1, "山口七星　｜　Hospitality and Culture Division",
    0.5, 6.3, 8, 0.4, size=12, color=KC_GRAY)
txt(s1, "2026年6月", 0.5, 6.65, 4, 0.3, size=11, color=KC_GRAY)
txt(s1, "Input\n　↓\nAI処理\n　↓\nOutput\n　↓\n実行管理",
    9.8, 1.5, 3, 4, size=20, bold=True, color=KC_GOLD, align=PP_ALIGN.CENTER)
footer(s1, 1)

# =====================================================
# S2 課題（背景）
# =====================================================
s2 = add_slide()
bg(s2, KC_LIGHT)
box(s2, 0, 0, 13.333, 1.2, bg_color=KC_NAVY)
section_tag(s2, "取り組みの背景")
txt(s2, "なぜAI業務OSが必要だったか：4つの構造的課題",
    0.4, 0.45, 12, 0.55, size=22, bold=True, color=KC_WHITE)
issues = [
    ("01","情報の属人化","Teams・PMS・会議メモ・OTA・ベンダー見積が散在\n優先順位の判断が担当者経験に完全依存"),
    ("02","報告品質のばらつき","論点整理の深さ・経営向けの見せ方に担当者差\n差し戻し・再考の時間が発生"),
    ("03","専門知識への依存","要件定義・市場調査・SNS戦略・価格施策を\n外部委託または専門人材に依存"),
    ("04","施策実行スピードの低下","報告・稟議・準備に時間がかかり\n価格施策・開業準備の意思決定頻度が限定"),
]
positions = [(0.35,1.35),(6.85,1.35),(0.35,4.0),(6.85,4.0)]
for (num,title,body),(lx,ty) in zip(issues,positions):
    box(s2, lx, ty, 6.2, 2.5, bg_color=KC_NAVY)
    box(s2, lx, ty, 0.65, 2.5, bg_color=KC_GOLD)
    txt(s2, num, lx+0.08, ty+0.85, 0.55, 0.7, size=26, bold=True, color=KC_NAVY, align=PP_ALIGN.CENTER)
    txt(s2, title, lx+0.75, ty+0.15, 5.3, 0.5, size=17, bold=True, color=KC_GOLD)
    txt(s2, body, lx+0.75, ty+0.65, 5.3, 1.7, size=13, color=KC_WHITE)
footer(s2, 2)

# =====================================================
# S3 全体像
# =====================================================
s3 = add_slide()
bg(s3, KC_LIGHT)
box(s3, 0, 0, 13.333, 1.2, bg_color=KC_NAVY)
section_tag(s3, "応募内容の概要")
txt(s3, "ホテル事業部の業務OS化：情報を判断材料に変換するフロー",
    0.4, 0.45, 12, 0.55, size=22, bold=True, color=KC_WHITE)
flow_items = [
    ("INPUT","現場メモ\n売上数値\n会議内容\nベンダー論点", KC_GRAY),
    ("AI処理","論点整理\n構造化\n言語変換\nToDo化", KC_NAVY),
    ("OUTPUT","役員報告\n稟議文案\n週次レポート\n価格施策", KC_GREEN),
    ("実行管理","Notion連携\n進捗管理\n承認サマリー\n宿題管理", RGBColor(0x5B,0x4F,0xA0)),
]
for i,(title,body,col) in enumerate(flow_items):
    lx = 0.35 + i*3.25
    box(s3, lx, 1.35, 2.9, 4.5, bg_color=col)
    txt(s3, title, lx, 1.38, 2.9, 0.7, size=18, bold=True, align=PP_ALIGN.CENTER)
    box(s3, lx+0.1, 2.05, 2.7, 0.06, bg_color=KC_GOLD)
    txt(s3, body, lx+0.15, 2.15, 2.65, 3.5, size=14)
    if i < 3:
        txt(s3, "→", lx+2.88, 2.95, 0.4, 0.6, size=28, bold=True, color=KC_GOLD, align=PP_ALIGN.CENTER)
box(s3, 0.35, 6.0, 12.65, 0.75, bg_color=KC_NAVY)
txt(s3, "💡 ポイント：AIを単発利用で終わらせず、入力・処理・出力・実行管理の業務フローに完全組込み。属人的な「考える・整理する・判断材料にする」プロセスを再現可能な業務基盤として設計。",
    0.5, 6.05, 12.3, 0.65, size=12, color=KC_GOLD)
footer(s3, 3)

# =====================================================
# S4 デモ予告（F&K宮島版）
# =====================================================
s4 = add_slide()
bg(s4, KC_NAVY)
box(s4, 0, 3.2, 13.333, 0.08, bg_color=KC_GOLD)
txt(s4, "LIVE DEMO", 0, 0.4, 13.333, 1.4, size=80, bold=True,
    color=KC_WHITE, align=PP_ALIGN.CENTER)
box(s4, 1.5, 1.95, 10.333, 0.95, bg_color=KC_GOLD)
txt(s4, "HOTEL FORK & KNIFE Miyajima　ADR・OCC改善の示唆だし",
    1.5, 1.95, 10.333, 0.95, size=19, bold=True, color=KC_NAVY, align=PP_ALIGN.CENTER)

# 3論点ボックス
topics = [
    ("論点1","レベニュー管理","Twin A OCC 22%\nの構造課題と\n改善施策"),
    ("論点2","チャネル最適化","一休33%依存\nからの脱却\n収益シミュレーション"),
    ("論点3","口コミ×競合","差分抽出と\n次の打ち手\n界 宮島開業対策"),
]
for i,(tag,title,body) in enumerate(topics):
    lx = 1.0 + i*3.9
    box(s4, lx, 3.4, 3.5, 3.0, bg_color=RGBColor(0x14,0x24,0x3A))
    box(s4, lx, 3.4, 3.5, 0.45, bg_color=KC_GOLD)
    txt(s4, tag, lx, 3.4, 3.5, 0.45, size=14, bold=True, color=KC_NAVY, align=PP_ALIGN.CENTER)
    txt(s4, title, lx+0.1, 3.9, 3.3, 0.55, size=15, bold=True, color=KC_GOLD)
    txt(s4, body, lx+0.1, 4.45, 3.3, 1.8, size=13, color=KC_LIGHT)

txt(s4, "11スキルが連携して、現場数値→経営判断サマリーまでを目の前で生成します",
    0.5, 6.45, 12.333, 0.5, size=13, color=KC_GRAY, align=PP_ALIGN.CENTER)
footer(s4, 4)

# =====================================================
# S5 デモ実行
# =====================================================
s5 = add_slide()
bg(s5, RGBColor(0x08, 0x10, 0x1A))
txt(s5, "[ DEMO ]", 0, 0.2, 13.333, 0.9, size=52, bold=True,
    color=KC_GOLD, align=PP_ALIGN.CENTER)
txt(s5, "HOTEL FORK & KNIFE Miyajima　実データで11スキルを実行",
    0, 1.1, 13.333, 0.55, size=18, color=KC_WHITE, align=PP_ALIGN.CENTER)
steps = [
    ("0〜15秒","①②③ OCC/ADR/Twin Aの数値構造化→3シナリオ→価格施策",KC_GRAY),
    ("15〜30秒","④⑤⑥ 一休依存の収益リスク分解→直販シミュレーション→90日ロードマップ",KC_GRAY),
    ("30〜50秒","⑦⑧⑨⑩ 口コミ示唆→競合差分→優先度マトリクス→役員レポート成型",KC_GRAY),
    ("50〜55秒","「最後のスキル⑪を今この場でライブ実行します」と宣言",KC_GOLD),
    ("55〜75秒","⑪ executive-decision-synthesizer：3論点統合＋承認事項リスト　ライブ生成",KC_GREEN),
]
for i,(timing,action,col) in enumerate(steps):
    ty = 1.85 + i*0.92
    box(s5, 1.0, ty, 1.5, 0.75, bg_color=col)
    txt(s5, timing, 1.0, ty+0.12, 1.5, 0.55, size=11, bold=True, color=KC_NAVY, align=PP_ALIGN.CENTER)
    txt(s5, action, 2.65, ty+0.12, 10.0, 0.55, size=13, color=KC_WHITE)
txt(s5, "⚠ 失敗時：「念のため事前収録でお見せします」→ タブBに即切替",
    0.5, 6.4, 12.5, 0.45, size=11, color=KC_RED, italic=True)
footer(s5, 5)

# =====================================================
# S6 効果数値
# =====================================================
s6 = add_slide()
bg(s6, KC_LIGHT)
box(s6, 0, 0, 13.333, 1.2, bg_color=KC_NAVY)
section_tag(s6, "期待効果")
txt(s6, "数字で見る成果：4事例平均 約76%の工数削減",
    0.4, 0.45, 12, 0.55, size=22, bold=True, color=KC_WHITE)
metrics = [
    ("週次レポート\n作成時間","週150分","週30分","▲80%"),
    ("週次アジェンダ\n更新時間","週60分","週5分","▲92%"),
    ("ベンダー要件定義\n・対応工数","週15〜20h","週6h","▲70%"),
    ("市場調査\n戦略立案コスト","数百万円〜\n（代理店）","0円\n（AI内製）","▲100%"),
    ("同時進行できる\n開業準備物件","1物件","3物件","3倍"),
    ("価格施策\n検討頻度","月1回","週次","4倍以上"),
]
for i,(item,before,after,effect) in enumerate(metrics):
    col = i % 3
    row = i // 3
    lx = 0.35 + col*4.3
    ty = 1.35 + row*2.55
    box(s6, lx, ty, 4.0, 2.3, bg_color=KC_NAVY)
    txt(s6, item, lx+0.1, ty+0.1, 3.8, 0.65, size=12, bold=True, color=KC_GOLD)
    txt(s6, f"Before: {before}", lx+0.1, ty+0.75, 3.8, 0.55, size=11, color=KC_GRAY)
    txt(s6, f"After:  {after}",  lx+0.1, ty+1.25, 3.8, 0.55, size=11, color=KC_WHITE)
    box(s6, lx+2.5, ty+0.08, 1.4, 0.55, bg_color=KC_GREEN)
    txt(s6, effect, lx+2.5, ty+0.08, 1.4, 0.55, size=17, bold=True, align=PP_ALIGN.CENTER)
footer(s6, 6)

# =====================================================
# S7 横展開（F&K → 他部署へ の行を追加）
# =====================================================
s7 = add_slide()
bg(s7, KC_LIGHT)
box(s7, 0, 0, 13.333, 1.2, bg_color=KC_NAVY)
section_tag(s7, "実現性・横展開")
txt(s7, "KC全社への展開：4点の標準化で7部門＋既存施設に適用可能",
    0.4, 0.45, 12, 0.55, size=21, bold=True, color=KC_WHITE)
items4 = ["プロンプト集","入力フォーマット","出力フォーマット","利用ルール（ガバナンス）"]
for i,item in enumerate(items4):
    lx = 0.35 + i*3.25
    box(s7, lx, 1.3, 3.0, 0.7, bg_color=KC_GOLD)
    txt(s7, f"0{i+1}  {item}", lx+0.1, 1.35, 2.8, 0.6, size=13, bold=True, color=KC_NAVY)
txt(s7, "→ この4点を整備するだけで全部署・既存施設に横展開可能",
    0.4, 2.05, 12, 0.4, size=13, color=KC_NAVY, bold=True)

# 既存施設展開ボックス（F&K宮島が示したユースケースを最初に）
box(s7, 0.35, 2.55, 12.65, 0.9, bg_color=RGBColor(0x1A, 0x3A, 0x2E))
box(s7, 0.35, 2.55, 0.08, 0.9, bg_color=KC_GOLD)
txt(s7, "★ 既存施設での示唆だし（F&K宮島で実証）",
    0.55, 2.58, 5, 0.38, size=12, bold=True, color=KC_GOLD)
txt(s7, "OCC/ADR/口コミ/競合データを入力→改善施策・チャネル戦略・役員サマリーをその場で生成",
    0.55, 2.95, 12, 0.38, size=11, color=KC_WHITE)

# 7部署
depts = [
    ("投資・不動産","物件論点整理・投資判断・リスク抽出・稟議文案"),
    ("開発・建設","工事/設計/ベンダー要件定義・進捗報告"),
    ("経理・財務","請求・証憑リスク整理・稟議変換"),
    ("法務・コンプラ","契約書レビュー・リスク分類・確認事項"),
    ("営業","商談メモ→提案書・顧客別アプローチ整理"),
    ("情シス・AILAB","要件定義・ベンダー対応・仕様書作成"),
    ("経営企画／人事","会議ログ論点整理・役員サマリー・求人票"),
]
for i,(dept,body) in enumerate(depts):
    col = i % 4
    row = i // 4
    lx = 0.35 + col*3.25
    ty = 3.6 + row*1.65
    box(s7, lx, ty, 3.0, 1.5, bg_color=KC_NAVY)
    txt(s7, dept, lx+0.1, ty+0.1, 2.8, 0.4, size=12, bold=True, color=KC_GOLD)
    txt(s7, body, lx+0.1, ty+0.5, 2.8, 0.9, size=9.5, color=KC_WHITE)

box(s7, 0.35, 6.58, 12.65, 0.5, bg_color=RGBColor(0x2C,0x3E,0x50))
txt(s7, "🔒 ガバナンス：投入前マスキングルール整備 ／ 学習使用なし契約プラン利用 ／ 情シス・AILABと利用ガイドライン共同策定中",
    0.5, 6.62, 12.3, 0.43, size=9.5, color=KC_GOLD)
footer(s7, 7)

# =====================================================
# S8 まとめ
# =====================================================
s8 = add_slide()
bg(s8, KC_NAVY)
box(s8, 0, 2.8, 13.333, 0.08, bg_color=KC_GOLD)
txt(s8, "AIの価値は、文章をきれいにすることではありません。",
    0.5, 0.5, 12.333, 0.85, size=24, bold=True, color=KC_WHITE, align=PP_ALIGN.CENTER)
txt(s8, "現場に散らばる情報を、意思決定できる状態に変換することです。",
    0.5, 1.35, 12.333, 0.85, size=24, bold=True, color=KC_GOLD, align=PP_ALIGN.CENTER)
results = [
    ("76%\n工数削減","4事例平均"),
    ("0円\n内製化","代理店費→AI"),
    ("3倍\n同時推進","開業準備物件数"),
]
for i,(num,sub) in enumerate(results):
    lx = 1.5 + i*3.7
    box(s8, lx, 3.1, 3.2, 2.0, bg_color=RGBColor(0x14,0x24,0x3A))
    box(s8, lx, 3.1, 3.2, 0.06, bg_color=KC_GOLD)
    txt(s8, num, lx, 3.2, 3.2, 1.2, size=32, bold=True, color=KC_GOLD, align=PP_ALIGN.CENTER)
    txt(s8, sub, lx, 4.35, 3.2, 0.5, size=12, color=KC_GRAY, align=PP_ALIGN.CENTER)
txt(s8, "ホテル事業部で実証したこのモデルを、KC全社の業務品質底上げに展開します。",
    0.5, 5.3, 12.333, 0.6, size=16, color=KC_LIGHT, align=PP_ALIGN.CENTER)
txt(s8, "ご清聴ありがとうございました",
    0.5, 6.0, 12.333, 0.5, size=18, bold=True, color=KC_WHITE, align=PP_ALIGN.CENTER)
footer(s8, 8)

out = "/home/user/sm_pjt/presentation/KASUMIGASEKI_AI_OS_Final_FKMiyajima.pptx"
prs.save(out)
print(f"Saved: {out}")
print(f"Slides: {len(prs.slides)}")
