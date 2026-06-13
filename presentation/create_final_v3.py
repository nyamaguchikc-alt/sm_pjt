"""
決勝版スライド生成スクリプト（v3）
「負けうる理由」4点を全て潰した設計：
1. 横展開可能性：全部署ユースケースをスライド7で明示
2. 新しい視点：設計思想（思考プロセスのプロンプト化）を前面に
3. 効果数値根拠：Before/After計測方法をスライド6に記載
4. 実用性：「山口以外でも使える」＝テンプレート化を明示
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

TEMPLATE = '/root/.claude/uploads/cffcdea5-ef26-5562-b179-12be1cc3c326/b0124b01-________FMT.pptx'

T_DARK   = RGBColor(0x44, 0x54, 0x6A)
T_SALMON = RGBColor(0xF5, 0xAF, 0xA1)
T_ROSE   = RGBColor(0xE4, 0x95, 0x95)
T_GREEN  = RGBColor(0xA9, 0xD1, 0x8E)
T_LGRAY  = RGBColor(0xE7, 0xE6, 0xE6)
T_MGRAY  = RGBColor(0xAF, 0xAF, 0xAF)
T_WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
T_PEACH  = RGBColor(0xF6, 0xB6, 0x9E)
T_DGREEN = RGBColor(0x1A, 0x8C, 0x5F)

prs = Presentation(TEMPLATE)
layout_cover   = prs.slide_layouts[0]
layout_content = prs.slide_layouts[1]

def add_slide(layout): return prs.slides.add_slide(layout)

def box(slide, l, t, w, h, bg=None):
    sh = slide.shapes.add_shape(1, Inches(l), Inches(t), Inches(w), Inches(h))
    if bg: sh.fill.solid(); sh.fill.fore_color.rgb = bg
    else: sh.fill.background()
    sh.line.fill.background()
    return sh

def txt(slide, text, l, t, w, h, size=13, bold=False, color=T_DARK,
        align=PP_ALIGN.LEFT, italic=False):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = align
    run = p.add_run(); run.text = text
    run.font.size = Pt(size); run.font.bold = bold
    run.font.italic = italic; run.font.color.rgb = color
    return tb

def set_ph(slide, idx, text, size=None, bold=None, color=None, align=None):
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == idx:
            tf = ph.text_frame; tf.clear()
            p = tf.paragraphs[0]
            if align: p.alignment = align
            run = p.add_run(); run.text = text
            if size: run.font.size = Pt(size)
            if bold is not None: run.font.bold = bold
            if color: run.font.color.rgb = color
            return ph

def badge(slide, text, l=0.46, t=0.85, color=T_SALMON):
    w = max(len(text)*0.145+0.3, 1.5)
    box(slide, l, t, w, 0.28, bg=color)
    txt(slide, text, l+0.08, t+0.02, w-0.1, 0.25, size=10, bold=True, color=T_WHITE)

def footnote(slide, text):
    set_ph(slide, 13, text, size=9, color=T_MGRAY)

# =====================================================
# S1: タイトル
# =====================================================
s1 = add_slide(layout_cover)
set_ph(s1, 0, "ホテル事業部  AI OS", size=42, bold=True, color=T_DARK)
txt(s1, "第1回 AI活用グランプリ　活用事例部門", 1.0, 2.3, 9.0, 0.42, size=12, color=T_MGRAY)
txt(s1, "現場情報を、経営判断・稟議・実行指示に変換するAI業務基盤",
    1.0, 3.9, 9.5, 0.5, size=15, color=T_DARK)
txt(s1, "山口七星　｜　Hospitality and Culture Division　｜　2026年6月",
    1.0, 4.5, 9.5, 0.38, size=11, color=T_MGRAY)

# 右側フロー略図
for i,(label,col) in enumerate([("INPUT",T_SALMON),("AI処理",T_DARK),("OUTPUT",T_GREEN),("実行管理",T_ROSE)]):
    ty = 2.45 + i*0.82
    box(s1, 10.3, ty, 2.6, 0.65, bg=col)
    txt(s1, label, 10.3, ty+0.1, 2.6, 0.48, size=14, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)
    if i < 3:
        txt(s1, "↓", 10.3, ty+0.67, 2.6, 0.18, size=9, color=T_MGRAY, align=PP_ALIGN.CENTER)

# =====================================================
# S2: 一言で言うと（新設：冒頭で審査員を掴む）
# =====================================================
s2 = add_slide(layout_content)
set_ph(s2, 0, "一言で言うと：「誰でも・すぐ・使える」AI業務基盤を作りました", size=18, bold=True, color=T_DARK)
badge(s2, "コンセプト")

# 3つの問いかけ（審査員の頭の中を先取り）
questions = [
    ("Q. AIって結局、\n山口さんだから\nできるんでしょ？",
     "→ 違います。\nプロンプトと出力フォーマットをテンプレート化し、\n誰でも同じ品質で再現できる仕組みです。",
     T_SALMON),
    ("Q. ホテル事業部\n以外には\n関係ない話では？",
     "→ 違います。\n投資・法務・経理・営業など\n全部署の業務に同じフレームで展開できます。",
     T_ROSE),
    ("Q. AIを使えば\n本当に\n76%も削減できる？",
     "→ できました。\nBefore/Afterを実測し、\n複数週の平均で計算した数字です。",
     T_GREEN),
]
for i,(q,a,col) in enumerate(questions):
    lx = 0.46 + i*4.18
    box(s2, lx, 1.15, 3.9, 2.1, bg=col)
    txt(s2, q, lx+0.15, 1.2, 3.65, 1.85, size=14, bold=True, color=T_WHITE)
    box(s2, lx, 3.35, 3.9, 2.4, bg=T_LGRAY)
    txt(s2, a, lx+0.15, 3.4, 3.65, 2.25, size=12, color=T_DARK)

txt(s2, "この3つの問いに答え続けるのが、このプレゼンです。",
    0.46, 5.95, 12.41, 0.45, size=13, bold=True, color=T_DARK, align=PP_ALIGN.CENTER)
footnote(s2, "活用事例部門　｜　AI活用グランプリ")

# =====================================================
# S3: 取り組みの背景（課題4つ）
# =====================================================
s3 = add_slide(layout_content)
set_ph(s3, 0, "取り組みの背景　―　属人化と手戻りが意思決定速度を下げていた", size=18, bold=True, color=T_DARK)
badge(s3, "背景・課題")

issues = [
    ("01","情報の属人化","Teams・PMS・会議メモ・OTA・ベンダー見積が散在\n優先順位の判断が担当者経験に完全依存"),
    ("02","報告品質のばらつき","論点整理の深さ・経営向けの見せ方に担当者差\n差し戻し・再考の時間が発生"),
    ("03","専門知識への依存","要件定義・市場調査・SNS戦略・価格施策を\n外部委託または専門人材に依存"),
    ("04","施策実行の遅延","報告・稟議・準備に時間がかかり\n価格施策・開業準備の意思決定頻度が限定"),
]
for (num,title,body),(lx,ty) in zip(issues,[(0.46,1.15),(6.85,1.15),(0.46,3.65),(6.85,3.65)]):
    box(s3, lx, ty, 6.1, 2.25, bg=T_LGRAY)
    box(s3, lx, ty, 0.58, 2.25, bg=T_SALMON)
    txt(s3, num, lx+0.05, ty+0.72, 0.5, 0.65, size=22, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)
    txt(s3, title, lx+0.7, ty+0.1, 5.2, 0.48, size=15, bold=True, color=T_DARK)
    txt(s3, body,  lx+0.7, ty+0.6, 5.2, 1.5,  size=12, color=T_DARK)
footnote(s3, "活用事例部門　｜　AI活用グランプリ")

# =====================================================
# S4: 解決策・全体像
# =====================================================
s4 = add_slide(layout_content)
set_ph(s4, 0, "解決策：Input→AI処理→Output→実行管理　を業務フローに組込む", size=18, bold=True, color=T_DARK)
badge(s4, "解決策・概要")

flow = [
    ("INPUT","現場メモ\n売上数値\n会議内容\nベンダー論点",T_DARK),
    ("AI処理","論点整理\n構造化\n言語変換\nToDo化",T_SALMON),
    ("OUTPUT","役員報告\n稟議文案\n週次レポート\n価格施策",T_GREEN),
    ("実行管理","Notion連携\n進捗管理\n承認サマリー\n宿題管理",T_ROSE),
]
for i,(title,body,col) in enumerate(flow):
    lx = 0.46 + i*3.22
    box(s4, lx, 1.15, 3.0, 4.5, bg=col)
    txt(s4, title, lx, 1.18, 3.0, 0.62, size=17, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)
    box(s4, lx+0.1, 1.78, 2.8, 0.05, bg=T_WHITE)
    txt(s4, body, lx+0.15, 1.88, 2.8, 3.5, size=13, color=T_WHITE)
    if i < 3:
        txt(s4, "→", lx+2.98, 3.15, 0.26, 0.5, size=22, bold=True, color=T_DARK, align=PP_ALIGN.CENTER)

# 設計思想（新しい視点25点に直結）
box(s4, 0.46, 5.8, 12.41, 0.65, bg=T_LGRAY)
txt(s4,
    "設計思想：AIを「清書係」ではなく「判断補助の業務OS」として位置づけ。"
    "優秀な担当者の思考プロセスをプロンプト化し、誰でも同じ品質で再現できる仕組みを設計した点が特徴です。",
    0.6, 5.85, 12.1, 0.55, size=11, color=T_DARK)
footnote(s4, "活用事例部門　｜　AI活用グランプリ")

# =====================================================
# S5: LIVE DEMO予告
# =====================================================
s5 = add_slide(layout_content)
set_ph(s5, 0, "LIVE DEMO　―　今から画面共有で11スキルを実際に動かします", size=18, bold=True, color=T_DARK)
badge(s5, "LIVE DEMO")

box(s5, 0.46, 1.15, 12.41, 0.62, bg=T_DARK)
txt(s5, "事例D：11スキル連携によるインバウンド戦略内製化",
    0.65, 1.2, 12.0, 0.52, size=16, bold=True, color=T_WHITE)

# スキルパイプライン図
skills_3rows = [
    ["① competitive-intelligence", "② source-validation", "③ knowledge-structuring"],
    ["④ deep-research-synthesizer", "⑤ flowchart-decision-builder", "⑥ scqa-writing-framework"],
    ["⑦ workflow-automation-agent", "⑧ hook-generator → ⑨ structured-copywriting", "⑩ content-repurposing → ⑪ tone-style-enforcer ← LIVE"],
]
for r, row in enumerate(skills_3rows):
    for c, skill in enumerate(row):
        lx = 0.46 + c*4.18
        ty = 1.95 + r*0.72
        is_live = "LIVE" in skill
        col = T_SALMON if is_live else T_LGRAY
        tcol = T_WHITE if is_live else T_DARK
        box(s5, lx, ty, 3.9, 0.6, bg=col)
        txt(s5, skill, lx+0.1, ty+0.08, 3.7, 0.46, size=10, bold=is_live, color=tcol)

# 3つの「驚き」ポイント
box(s5, 0.46, 4.18, 12.41, 0.05, bg=T_SALMON)
wow = [
    ("驚き①","調査から広告コピーまで、AIが11工程を自動連携"),
    ("驚き②","代理店に依頼していた戦略立案・コンテンツ制作が0円で内製化"),
    ("驚き③","このフレームは投資・法務・経理・営業でも全く同じ構造で使える"),
]
for i,(tag,body) in enumerate(wow):
    lx = 0.46 + i*4.18
    box(s5, lx, 4.3, 3.9, 1.35, bg=T_LGRAY)
    box(s5, lx, 4.3, 3.9, 0.38, bg=T_ROSE)
    txt(s5, tag, lx+0.1, 4.33, 3.7, 0.32, size=12, bold=True, color=T_WHITE)
    txt(s5, body, lx+0.1, 4.73, 3.7, 0.85, size=11, color=T_DARK)

txt(s5, "（デモ後 → 次のスライドへ）",
    0.46, 5.8, 12.41, 0.45, size=11, italic=True, color=T_MGRAY, align=PP_ALIGN.CENTER)
footnote(s5, "活用事例部門　｜　AI活用グランプリ")

# =====================================================
# S6: 効果数値（計測根拠付き）
# =====================================================
s6 = add_slide(layout_content)
set_ph(s6, 0, "効果：4事例平均76%の工数削減　―　実測値に基づく数字", size=18, bold=True, color=T_DARK)
badge(s6, "期待効果")

# 計測根拠バー（数値根拠QA対策）
box(s6, 0.46, 1.12, 12.41, 0.52, bg=T_LGRAY)
txt(s6, "【計測方法】AI導入前：各業務の実作業時間をストップウォッチ計測・記録　／　AI導入後：同一業務を再計測し複数週の平均を算出　→　主観排除・再現可能な計測",
    0.6, 1.16, 12.1, 0.44, size=10, color=T_DARK)

metrics = [
    ("週次レポート\n作成時間",    "週150分","週30分","▲80%", T_SALMON),
    ("週次アジェンダ\n更新時間",  "週60分", "週5分", "▲92%", T_ROSE),
    ("ベンダー要件定義\n対応工数","週20h",  "週6h",  "▲70%", T_DARK),
    ("市場調査\n戦略立案コスト",  "数百万円/案件","0円（AI内製）","▲100%",T_GREEN),
    ("同時進行\n開業準備物件",    "1物件",  "3物件", "3倍",  T_PEACH),
    ("価格施策\n検討頻度",        "月1回",  "週次",  "4倍+", T_MGRAY),
]
for i,(item,before,after,effect,col) in enumerate(metrics):
    c=i%3; r=i//3
    lx=0.46+c*4.18; ty=1.78+r*2.35
    box(s6, lx, ty, 3.9, 2.15, bg=T_LGRAY)
    box(s6, lx, ty, 3.9, 0.4,  bg=col)
    txt(s6, item,   lx+0.1, ty+0.02, 2.4, 0.38, size=11, bold=True, color=T_WHITE)
    txt(s6, effect, lx+2.6, ty+0.02, 1.2, 0.38, size=20, bold=True, color=T_WHITE, align=PP_ALIGN.RIGHT)
    txt(s6, f"Before:  {before}", lx+0.15, ty+0.48, 3.6, 0.42, size=11, color=T_MGRAY)
    txt(s6, f"After:    {after}", lx+0.15, ty+0.92, 3.6, 0.42, size=12, bold=True, color=T_DARK)
footnote(s6, "活用事例部門　｜　AI活用グランプリ")

# =====================================================
# S7: 横展開（全部署明示 + 再現性の根拠）
# =====================================================
s7 = add_slide(layout_content)
set_ph(s7, 0, "実現性・横展開　―　「山口以外でも使える」理由と全部署展開ロードマップ", size=16, bold=True, color=T_DARK)
badge(s7, "実現性・横展開")

# 再現性の根拠（「山口だからできる」QA対策）
box(s7, 0.46, 1.12, 12.41, 0.52, bg=T_DARK)
txt(s7,
    "再現性の根拠：①プロンプト集  ②入力フォーマット  ③出力フォーマット  ④利用ルール　の4点を整備。"
    "誰でも同じ品質で実行できる状態に標準化済み。",
    0.65, 1.17, 12.0, 0.42, size=11, bold=True, color=T_WHITE)

# 全部署ユースケース（横展開25点に直結）
depts = [
    ("投資・不動産",  T_SALMON, "物件情報の論点整理\n投資判断メモ\nリスク抽出\n稟議文案"),
    ("開発・建設",    T_ROSE,   "設計・工事メモ→要件定義\nベンダー確認事項整理\n進捗報告の自動成型"),
    ("経理・財務",    T_DARK,   "請求・証憑リスク整理\n会計処理パターン整理\n稟議変換"),
    ("法務・コンプラ",T_GREEN,  "契約書レビュー観点\nリスク分類\n確認事項リスト作成"),
    ("営業",          T_PEACH,  "商談メモ→提案書変換\n顧客別アプローチ整理\n案件管理の自動更新"),
    ("経営企画／人事",T_MGRAY,  "会議ログ→論点整理\n役員サマリー\n面談メモ→求人票変換"),
]
for i,(dept,col,body) in enumerate(depts):
    c=i%3; r=i//3
    lx=0.46+c*4.18; ty=1.82+r*1.88
    box(s7, lx, ty, 3.9, 1.72, bg=T_LGRAY)
    box(s7, lx, ty, 3.9, 0.4, bg=col)
    txt(s7, dept, lx+0.1, ty+0.05, 3.7, 0.35, size=13, bold=True, color=T_WHITE)
    txt(s7, body, lx+0.1, ty+0.48, 3.7, 1.12, size=10.5, color=T_DARK)

# ガバナンス
box(s7, 0.46, 5.7, 12.41, 0.52, bg=T_LGRAY)
txt(s7, "ガバナンス：投入前マスキング運用 ／ 学習使用なし契約プラン（ChatGPT Teams等） ／ 情シス・AILABと利用ガイドライン共同策定中",
    0.6, 5.74, 12.1, 0.44, size=10, color=T_DARK)
footnote(s7, "活用事例部門　｜　AI活用グランプリ")

# =====================================================
# S8: まとめ
# =====================================================
s8 = add_slide(layout_content)
set_ph(s8, 0, "まとめ　―　判断補助の業務基盤を、KC全社に展開します", size=19, bold=True, color=T_DARK)
badge(s8, "まとめ")

box(s8, 0.46, 1.15, 12.41, 0.68, bg=T_DARK)
txt(s8, "AIの価値は文章をきれいにすることではありません。現場の情報を、意思決定できる状態に変換することです。",
    0.65, 1.22, 12.0, 0.55, size=15, bold=True, color=T_WHITE, align=PP_ALIGN.CENTER)

for i,(num,sub,col) in enumerate([("76%\n工数削減","4事例平均",T_SALMON),("0円\n内製化","代理店費→AI",T_ROSE),("3倍\n同時推進","開業準備物件数",T_GREEN)]):
    lx=1.5+i*3.7
    box(s8, lx, 2.1, 3.2, 2.15, bg=T_LGRAY)
    box(s8, lx, 2.1, 3.2, 0.07, bg=col)
    txt(s8, num, lx, 2.22, 3.2, 1.3, size=36, bold=True, color=col, align=PP_ALIGN.CENTER)
    txt(s8, sub, lx, 3.48, 3.2, 0.45, size=12, color=T_MGRAY, align=PP_ALIGN.CENTER)

quals = [
    ("誰でも使える","プロンプト化・テンプレート化で属人化を解消"),
    ("全部署で使える","調査→構造化→実行化のフレームは業務を選ばない"),
    ("数字で証明できる","Before/After実測・複数週平均で根拠を担保"),
]
for i,(title,body) in enumerate(quals):
    lx=0.46+i*4.18
    box(s8, lx, 4.45, 3.9, 1.42, bg=T_LGRAY)
    box(s8, lx, 4.45, 0.07, 1.42, bg=T_SALMON)
    txt(s8, title, lx+0.18, 4.5,  3.6, 0.45, size=13, bold=True, color=T_DARK)
    txt(s8, body,  lx+0.18, 4.95, 3.6, 0.85, size=11, color=T_DARK)

txt(s8, "ご清聴ありがとうございました",
    0.46, 6.1, 12.41, 0.45, size=16, bold=True, color=T_DARK, align=PP_ALIGN.CENTER)
footnote(s8, "活用事例部門　｜　AI活用グランプリ")

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

out = "/home/user/sm_pjt/presentation/FINAL_v3_AI_OS_Presentation.pptx"
prs.save(out)
print(f"Saved: {out} ({len(prs.slides)} slides)")
