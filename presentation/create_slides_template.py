from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn
from copy import deepcopy
import lxml.etree as etree

TEMPLATE = '/root/.claude/uploads/cffcdea5-ef26-5562-b179-12be1cc3c326/b0124b01-________FMT.pptx'

# ===== テンプレートカラー =====
T_DARK   = RGBColor(0x44, 0x54, 0x6A)   # dk1 ネイビーグレー
T_SALMON = RGBColor(0xF5, 0xAF, 0xA1)   # accent1 サーモン
T_ROSE   = RGBColor(0xE4, 0x95, 0x95)   # accent2 ローズ
T_GREEN  = RGBColor(0xA9, 0xD1, 0x8E)   # accent6 セージグリーン
T_LGRAY  = RGBColor(0xE7, 0xE6, 0xE6)   # lt2 ライトグレー
T_MGRAY  = RGBColor(0xAF, 0xAF, 0xAF)   # accent3 ミディアムグレー
T_WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
T_BLACK  = RGBColor(0x00, 0x00, 0x00)
T_PEACH  = RGBColor(0xF6, 0xB6, 0x9E)   # accent4

prs = Presentation(TEMPLATE)
layout_cover   = prs.slide_layouts[0]   # 表紙
layout_content = prs.slide_layouts[1]   # 1つのコンテンツ


# ===== ユーティリティ =====
def add_slide(layout):
    return prs.slides.add_slide(layout)

def box(slide, l, t, w, h, bg=None, border=None, border_pt=1.0):
    sh = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    if bg:
        sh.fill.solid(); sh.fill.fore_color.rgb = bg
    else:
        sh.fill.background()
    if border:
        sh.line.color.rgb = border
        from pptx.util import Pt as UPt
        sh.line.width = UPt(border_pt)
    else:
        sh.line.fill.background()
    return sh

def txt(slide, text, l, t, w, h, size=14, bold=False, color=T_DARK,
        align=PP_ALIGN.LEFT, italic=False, wrap=True):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = wrap
    p = tf.paragraphs[0]; p.alignment = align
    run = p.add_run(); run.text = text
    run.font.size = Pt(size); run.font.bold = bold
    run.font.italic = italic; run.font.color.rgb = color
    return tb

def set_ph(slide, idx, text, size=None, bold=None, color=None, align=None):
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == idx:
            tf = ph.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            if align: p.alignment = align
            run = p.add_run(); run.text = text
            if size:  run.font.size = Pt(size)
            if bold is not None: run.font.bold = bold
            if color: run.font.color.rgb = color
            return ph
    return None

def section_badge(slide, text, l=0.46, t=0.85):
    box(slide, l, t, len(text)*0.14+0.3, 0.3, bg=T_SALMON)
    txt(slide, text, l+0.1, t+0.03, len(text)*0.14+0.1, 0.26,
        size=10, bold=True, color=T_WHITE)


# =====================================================
# Slide 1: タイトル（表紙レイアウト）
# =====================================================
s1 = add_slide(layout_cover)

# タイトルプレースホルダー
set_ph(s1, 0, "ホテル事業部  AI OS", size=40, bold=True, color=T_DARK)

# 会社名プレースホルダー(idx=13相当 → テキストボックスで補完)
txt(s1, "第1回 AI活用グランプリ　活用事例部門",
    1.0, 2.35, 8.0, 0.45, size=12, color=T_MGRAY)
txt(s1, "現場情報を、経営判断・稟議・実行指示に変換するAI業務基盤",
    1.0, 3.92, 9.5, 0.5, size=14, color=T_DARK)

# 発表者
txt(s1, "山口七星　｜　Hospitality and Culture Division　｜　2026年6月",
    1.0, 4.52, 9.5, 0.4, size=11, color=T_MGRAY)

# 装飾：フロー略図（右側）
box(s1, 10.2, 2.4, 2.7, 3.5, bg=T_LGRAY)
for i,(label,col) in enumerate([("INPUT",T_SALMON),("AI処理",T_DARK),("OUTPUT",T_GREEN),("実行管理",T_ROSE)]):
    ty = 2.5 + i*0.78
    box(s1, 10.3, ty, 2.5, 0.6, bg=col)
    txt(s1, label, 10.3, ty+0.1, 2.5, 0.45, size=13, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)
    if i < 3:
        txt(s1, "↓", 10.3, ty+0.62, 2.5, 0.2, size=10, color=T_MGRAY, align=PP_ALIGN.CENTER)


# =====================================================
# Slide 2: 取り組みの背景
# =====================================================
s2 = add_slide(layout_content)
set_ph(s2, 0, "取り組みの背景　―　なぜAI業務OSが必要だったか", size=20, bold=True, color=T_DARK)
section_badge(s2, "背景・課題")

issues = [
    ("01","情報の属人化",    "Teams・PMS・会議メモ・OTA・ベンダー見積が散在。優先順位の判断が担当者経験に完全依存"),
    ("02","報告品質のばらつき","論点整理の深さ・経営向けの見せ方に担当者差。差し戻し・再考の時間が発生"),
    ("03","専門知識への依存",  "要件定義・市場調査・SNS・価格施策を外部委託または専門人材に依存"),
    ("04","施策実行スピードの低下","報告・稟議・準備に時間がかかり、価格施策・開業準備の意思決定頻度が限定"),
]
cols = [(0.46,1.1),(6.85,1.1),(0.46,3.5),(6.85,3.5)]
for (num,title,body),(lx,ty) in zip(issues,cols):
    box(s2, lx, ty, 6.1, 2.2, bg=T_LGRAY)
    box(s2, lx, ty, 0.6, 2.2, bg=T_SALMON)
    txt(s2, num, lx+0.05, ty+0.7, 0.55, 0.65, size=22, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)
    txt(s2, title, lx+0.7, ty+0.12, 5.25, 0.45, size=15, bold=True, color=T_DARK)
    txt(s2, body,  lx+0.7, ty+0.6,  5.25, 1.45, size=12, color=T_DARK)

set_ph(s2, 13, "活用事例部門　｜　AI活用グランプリ", size=9, color=T_MGRAY)


# =====================================================
# Slide 3: 活用概要・全体像
# =====================================================
s3 = add_slide(layout_content)
set_ph(s3, 0, "活用概要　―　業務OS化フロー：情報を判断材料に変換する仕組み", size=18, bold=True, color=T_DARK)
section_badge(s3, "応募内容の概要")

flow_items = [
    ("INPUT",    "現場メモ\n売上数値\n会議内容\nベンダー論点", T_DARK),
    ("AI処理",   "論点整理\n構造化\n言語変換\nToDo化",       T_SALMON),
    ("OUTPUT",   "役員報告\n稟議文案\n週次レポート\n価格施策", T_GREEN),
    ("実行管理", "Notion連携\n進捗管理\n承認サマリー\n宿題", T_ROSE),
]
for i,(title,body,col) in enumerate(flow_items):
    lx = 0.46 + i*3.22
    box(s3, lx, 1.15, 3.0, 4.5, bg=col)
    txt(s3, title, lx, 1.18, 3.0, 0.6, size=17, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)
    box(s3, lx+0.1, 1.75, 2.8, 0.05, bg=T_WHITE)
    txt(s3, body, lx+0.15, 1.85, 2.8, 3.5, size=13, color=T_WHITE)
    if i < 3:
        txt(s3, "→", lx+2.98, 3.1, 0.28, 0.55, size=22, bold=True, color=T_DARK, align=PP_ALIGN.CENTER)

box(s3, 0.46, 5.8, 12.41, 0.65, bg=T_LGRAY)
txt(s3, "ポイント：AIを単発利用で終わらせず、入力・処理・出力・実行管理の業務フローに組込み。属人的だった「考える・整理・判断材料化」プロセスを再現可能な業務基盤として設計。",
    0.6, 5.85, 12.1, 0.55, size=11, color=T_DARK)

set_ph(s3, 13, "活用事例部門　｜　AI活用グランプリ", size=9, color=T_MGRAY)


# =====================================================
# Slide 4: デモ予告
# =====================================================
s4 = add_slide(layout_content)
set_ph(s4, 0, "LIVE DEMO　―　HOTEL FORK & KNIFE Miyajima　ADR・OCC改善の示唆だし", size=17, bold=True, color=T_DARK)
section_badge(s4, "デモ実演")

# 施設紹介バー
box(s4, 0.46, 1.15, 12.41, 0.65, bg=T_DARK)
txt(s4, "HOTEL FORK & KNIFE Miyajima　／　2026年3月開業　／　34室スモールラグジュアリー　／　薪火ガストロノミー×ルーフトップ温泉SPA",
    0.6, 1.2, 12.1, 0.55, size=12, bold=True, color=T_WHITE)

# 3論点ボックス
topics = [
    ("論点１","レベニュー管理","Twin A OCC 22%\nの構造課題と\n改善施策（3シナリオ）", T_SALMON),
    ("論点２","チャネル最適化","一休.com 33%依存\nからの脱却と\n直販収益シミュレーション", T_ROSE),
    ("論点３","口コミ×競合","差分抽出・打ち手優先度\n界 宮島開業前の\n対応戦略", T_GREEN),
]
for i,(tag,title,body,col) in enumerate(topics):
    lx = 0.46 + i*4.15
    box(s4, lx, 2.0, 3.9, 0.5, bg=col)
    txt(s4, tag, lx, 2.0, 3.9, 0.5, size=14, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)
    box(s4, lx, 2.5, 3.9, 2.6, bg=T_LGRAY)
    txt(s4, title, lx+0.1, 2.55, 3.7, 0.5, size=14, bold=True, color=T_DARK)
    txt(s4, body,  lx+0.1, 3.05, 3.7, 2.0, size=12, color=T_DARK)

# スキル一覧
skills_row1 = "① data-intake  ② revenue-scenario  ③ pricing-action  ④ channel-dependency  ⑤ direct-booking"
skills_row2 = "⑥ channel-roadmap  ⑦ review-insight  ⑧ competitor-gap  ⑨ action-priority  ⑩ weekly-report"
skills_row3 = "⑪ executive-decision-synthesizer　←　LIVE実行（最終スキル）"
box(s4, 0.46, 4.85, 12.41, 1.4, bg=RGBColor(0xF0,0xEE,0xED))
txt(s4, skills_row1, 0.6, 4.9,  12.1, 0.38, size=10, color=T_DARK)
txt(s4, skills_row2, 0.6, 5.28, 12.1, 0.38, size=10, color=T_DARK)
txt(s4, skills_row3, 0.6, 5.66, 12.1, 0.38, size=10, bold=True, color=T_SALMON)

set_ph(s4, 13, "活用事例部門　｜　AI活用グランプリ", size=9, color=T_MGRAY)


# =====================================================
# Slide 5: デモ実行（進行ガイド）
# =====================================================
s5 = add_slide(layout_content)
set_ph(s5, 0, "DEMO実行　―　11スキル連携：現場数値 → 経営判断サマリー", size=18, bold=True, color=T_DARK)
section_badge(s5, "デモ実演")

steps = [
    ("0〜15秒",  "録画",   "①②③  OCC/ADR/Twin A数値の構造化 → OCC改善3シナリオ → Twin A価格施策",       T_MGRAY),
    ("15〜30秒", "録画",   "④⑤⑥  一休依存リスク分解 → 直販収益シミュレーション → 90日チャネルロードマップ", T_MGRAY),
    ("30〜50秒", "録画",   "⑦⑧⑨⑩  口コミ示唆抽出 → 競合差分分析 → 施策優先度マトリクス → 役員レポート成型",T_MGRAY),
    ("50〜55秒", "宣言",   "「最後のスキル⑪をこの場でライブ実行します」と宣言",                             T_SALMON),
    ("55〜75秒", "LIVE",   "⑪ executive-decision-synthesizer  →  3論点統合サマリー＋今月の承認事項リスト",  T_GREEN),
]
for i,(timing,label,action,col) in enumerate(steps):
    ty = 1.15 + i*0.95
    box(s5, 0.46, ty, 1.1, 0.78, bg=col)
    txt(s5, timing, 0.46, ty+0.1, 1.1, 0.6, size=10, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)
    box(s5, 1.58, ty, 0.75, 0.78, bg=T_DARK)
    txt(s5, label, 1.58, ty+0.1, 0.75, 0.6, size=10, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)
    box(s5, 2.35, ty, 10.52, 0.78, bg=T_LGRAY)
    txt(s5, action, 2.48, ty+0.15, 10.2, 0.55, size=12, color=T_DARK)

# フェイルセーフ
box(s5, 0.46, 5.95, 12.41, 0.5, bg=T_PEACH)
txt(s5, "⚠  失敗時：「念のため事前収録でお見せします」→ タブBに切替（バックアップ動画 demo_fullbackup_FK_Miyajima.mp4）",
    0.6, 6.0, 12.1, 0.4, size=10, color=T_DARK, italic=True)

set_ph(s5, 13, "活用事例部門　｜　AI活用グランプリ", size=9, color=T_MGRAY)


# =====================================================
# Slide 6: 効果数値
# =====================================================
s6 = add_slide(layout_content)
set_ph(s6, 0, "期待効果　―　4事例平均 約76%の工数削減・意思決定頻度の向上", size=18, bold=True, color=T_DARK)
section_badge(s6, "期待効果")

metrics = [
    ("週次レポート\n作成時間",    "週150分",    "週30分",    "▲80%", T_SALMON),
    ("週次アジェンダ\n更新時間",  "週60分",     "週5分",     "▲92%", T_ROSE),
    ("ベンダー要件定義\n対応工数","週15〜20h",  "週6h",      "▲70%", T_DARK),
    ("市場調査\n戦略立案コスト",  "代理店数百万〜","0円（AI内製）","▲100%",T_GREEN),
    ("開業準備\n同時進行物件",    "1物件",      "3物件",     "3倍",  T_PEACH),
    ("価格施策\n検討頻度",        "月1回",      "週次",      "4倍+", T_MGRAY),
]
for i,(item,before,after,effect,col) in enumerate(metrics):
    c = i % 3; r = i // 3
    lx = 0.46 + c*4.15; ty = 1.15 + r*2.55
    box(s6, lx, ty, 3.9, 2.3, bg=T_LGRAY)
    box(s6, lx, ty, 3.9, 0.42, bg=col)
    txt(s6, item,   lx+0.1, ty+0.02, 2.5, 0.4, size=12, bold=True, color=T_WHITE)
    txt(s6, effect, lx+2.6, ty+0.02, 1.2, 0.4, size=20, bold=True, color=T_WHITE, align=PP_ALIGN.RIGHT)
    txt(s6, f"Before:  {before}", lx+0.15, ty+0.5,  3.6, 0.45, size=11, color=T_MGRAY)
    txt(s6, f"After:    {after}", lx+0.15, ty+0.95, 3.6, 0.45, size=12, bold=True, color=T_DARK)

set_ph(s6, 13, "活用事例部門　｜　AI活用グランプリ", size=9, color=T_MGRAY)


# =====================================================
# Slide 7: 横展開ロードマップ（F&K → 他部署）
# =====================================================
s7 = add_slide(layout_content)
set_ph(s7, 0, "実現性・横展開　―　4点の標準化で全部署・既存施設に適用可能", size=17, bold=True, color=T_DARK)
section_badge(s7, "実現性・横展開")

# 4点標準化バー
items4 = ["01  プロンプト集","02  入力フォーマット","03  出力フォーマット","04  利用ルール（ガバナンス）"]
for i,item in enumerate(items4):
    lx = 0.46 + i*3.22
    box(s7, lx, 1.15, 3.0, 0.55, bg=T_SALMON)
    txt(s7, item, lx+0.1, 1.2, 2.8, 0.45, size=12, bold=True, color=T_WHITE)

# 既存施設実証バー（F&K宮島）
box(s7, 0.46, 1.82, 12.41, 0.72, bg=T_DARK)
box(s7, 0.46, 1.82, 0.08, 0.72, bg=T_GREEN)
txt(s7, "★ 既存施設での示唆だし（F&K Miyajima で実証済み）",
    0.65, 1.84, 6.5, 0.35, size=12, bold=True, color=T_GREEN)
txt(s7, "OCC/ADR/口コミ/競合データを入力 → 改善施策・チャネル戦略・役員サマリーをその場で生成",
    0.65, 2.18, 12.0, 0.3, size=11, color=T_LGRAY)

# 7部署
depts = [
    ("投資・不動産","物件論点整理・投資判断・リスク抽出・稟議文案"),
    ("開発・建設",  "工事/設計/ベンダー要件定義・進捗報告"),
    ("経理・財務",  "請求・証憑リスク整理・稟議変換"),
    ("法務・コンプラ","契約書レビュー・リスク分類・確認事項"),
    ("営業",        "商談メモ→提案書・顧客別アプローチ"),
    ("情シス・AILAB","要件定義・ベンダー対応・仕様書作成"),
    ("経営企画／人事","会議ログ論点整理・役員サマリー・求人票"),
]
for i,(dept,body) in enumerate(depts):
    c = i % 4; r = i // 4
    lx = 0.46 + c*3.22; ty = 2.68 + r*1.65
    box(s7, lx, ty, 3.0, 1.52, bg=T_LGRAY)
    box(s7, lx, ty, 3.0, 0.38, bg=T_ROSE)
    txt(s7, dept, lx+0.1, ty+0.04, 2.8, 0.32, size=11, bold=True, color=T_WHITE)
    txt(s7, body, lx+0.1, ty+0.42, 2.8, 1.0,  size=9.5, color=T_DARK)

# ガバナンス注記
set_ph(s7, 13, "ガバナンス：投入前マスキング整備 ／ 学習使用なし契約プラン ／ 情シス・AILABと利用ルール策定中", size=9, color=T_MGRAY)


# =====================================================
# Slide 8: まとめ
# =====================================================
s8 = add_slide(layout_content)
set_ph(s8, 0, "まとめ　―　AIは清書係ではなく、判断補助の業務基盤", size=20, bold=True, color=T_DARK)
section_badge(s8, "まとめ")

box(s8, 0.46, 1.15, 12.41, 0.72, bg=T_DARK)
txt(s8, "「現場の情報を、意思決定できる状態に変換すること」が、このAI業務OSの価値です。",
    0.65, 1.25, 12.0, 0.55, size=16, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)

# 3成果
results = [
    ("76%\n工数削減", "4事例平均",       T_SALMON),
    ("0円\n内製化",   "代理店費→AI",    T_ROSE),
    ("3倍\n同時推進", "開業準備物件数",  T_GREEN),
]
for i,(num,sub,col) in enumerate(results):
    lx = 1.5 + i*3.7
    box(s8, lx, 2.1, 3.2, 2.2, bg=T_LGRAY)
    box(s8, lx, 2.1, 3.2, 0.08, bg=col)
    txt(s8, num, lx, 2.25, 3.2, 1.35, size=38, bold=True, color=col, align=PP_ALIGN.CENTER)
    txt(s8, sub, lx, 3.55, 3.2, 0.5,  size=12, color=T_MGRAY, align=PP_ALIGN.CENTER)

# 定性成果
quals = [
    ("判断品質の安定","論点・リスク・意思決定事項をAIが構造化し、役員報告の品質が安定"),
    ("属人化の解消",  "思考プロセスをプロンプト化。誰でも一定品質で再現できる状態に"),
    ("専門機能の内製","PM・調査会社・マーケター・ライターの機能をAIで補完"),
]
for i,(title,body) in enumerate(quals):
    lx = 0.46 + i*4.15
    box(s8, lx, 4.5, 3.9, 1.5, bg=T_LGRAY)
    box(s8, lx, 4.5, 0.08, 1.5, bg=T_SALMON)
    txt(s8, title, lx+0.2, 4.55, 3.55, 0.45, size=13, bold=True, color=T_DARK)
    txt(s8, body,  lx+0.2, 5.0,  3.55, 0.9,  size=11, color=T_DARK)

txt(s8, "ホテル事業部で実証したこのモデルを、KC全社の業務品質底上げに展開します。",
    0.46, 6.15, 12.41, 0.45, size=14, bold=True, color=T_DARK, align=PP_ALIGN.CENTER)

set_ph(s8, 13, "活用事例部門　｜　AI活用グランプリ", size=9, color=T_MGRAY)


# =====================================================
# 元の2枚を削除
# =====================================================
NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
xml_slides = prs.slides._sldIdLst
for _ in range(2):
    el = xml_slides[0]
    rId = el.get(f'{{{NS}}}id')
    prs.part.drop_rel(rId)
    xml_slides.remove(el)

# 保存
out = "/home/user/sm_pjt/presentation/KASUMIGASEKI_AI_OS_FKMiyajima_Template.pptx"
prs.save(out)
print(f"Saved: {out}")
print(f"Slides: {len(prs.slides)}")
