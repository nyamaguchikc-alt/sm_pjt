// 西洋占星術 計算ライブラリ

export interface ZodiacSign {
  name: string;
  nameEn: string;
  symbol: string;
  emoji: string;
  element: string;
  elementEn: string;
  quality: string;
  rulingPlanet: string;
  rulingPlanetEmoji: string;
  dateRange: string;
  personality: string;
  strengths: string[];
  challenges: string[];
  love: string;
  career: string;
  money: string;
  health: string;
  lucky: {
    color: string;
    number: number;
    day: string;
    stone: string;
  };
  overallFortune: string;
}

export const ZODIAC_SIGNS: ZodiacSign[] = [
  {
    name: "牡羊座",
    nameEn: "Aries",
    symbol: "♈",
    emoji: "🐏",
    element: "火",
    elementEn: "Fire",
    quality: "活動宮",
    rulingPlanet: "火星",
    rulingPlanetEmoji: "♂",
    dateRange: "3/21〜4/19",
    personality:
      "情熱的で行動力があり、新しいことへの挑戦を恐れない先駆者。エネルギッシュでリーダーシップを持ち、直感で動く勇敢な魂の持ち主です。",
    strengths: ["行動力と推進力", "勇気とリーダーシップ", "情熱と熱意", "率直さと純粋さ"],
    challenges: ["衝動的な行動", "忍耐力の不足", "自己中心的になりやすい"],
    love: "一目惚れしやすく、情熱的に愛する恋愛体質。積極的なアプローチが得意ですが、長続きには努力が必要です。",
    career: "開拓者精神が輝く起業・スポーツ・営業などで活躍。スピードと行動力が武器になります。",
    money: "衝動買いに注意が必要。稼ぐ力はありますが、計画的な管理が課題です。",
    health: "エネルギーは旺盛ですが、無茶をしやすい傾向。頭部と顔の健康に注意を。",
    lucky: { color: "赤", number: 9, day: "火曜日", stone: "ルビー" },
    overallFortune: "火星の力強いエネルギーに守られ、挑戦した分だけ道が開けます。臆せず前進することが運命の扉を開く鍵です。",
  },
  {
    name: "牡牛座",
    nameEn: "Taurus",
    symbol: "♉",
    emoji: "🐂",
    element: "地",
    elementEn: "Earth",
    quality: "固定宮",
    rulingPlanet: "金星",
    rulingPlanetEmoji: "♀",
    dateRange: "4/20〜5/20",
    personality:
      "粘り強く堅実で、物質的・感覚的な豊かさを大切にします。審美眼があり、安定と安全を求める信頼できる存在です。",
    strengths: ["忍耐力と持続力", "実用的な判断力", "高い審美眼", "信頼性と誠実さ"],
    challenges: ["変化への抵抗感", "頑固さ", "物欲が強くなりやすい"],
    love: "慎重で時間をかけて愛を育みます。一度心を許すと深く献身的な恋愛をします。",
    career: "金融・芸術・農業・料理など、質と安定を大切にする分野で才能発揮。",
    money: "堅実な金銭管理が得意。長期的な資産形成に向いています。",
    health: "喉と甲状腺に注意。美食家のため食べすぎに気をつけましょう。",
    lucky: { color: "グリーン", number: 6, day: "金曜日", stone: "エメラルド" },
    overallFortune: "金星の恵みで美と豊かさに満ちた人生が約束されています。着実な努力が確かな財産を築きます。",
  },
  {
    name: "双子座",
    nameEn: "Gemini",
    symbol: "♊",
    emoji: "👥",
    element: "風",
    elementEn: "Air",
    quality: "柔軟宮",
    rulingPlanet: "水星",
    rulingPlanetEmoji: "☿",
    dateRange: "5/21〜6/21",
    personality:
      "知的好奇心旺盛で多才・多趣味。コミュニケーション能力が高く、機転が利いて話題が豊富。変化と刺激を求める自由な魂です。",
    strengths: ["優れたコミュニケーション力", "知的好奇心と多才さ", "適応力の高さ", "機転と柔軟な思考"],
    challenges: ["飽きやすい一面", "二面性を持ちやすい", "集中力の持続が難しい"],
    love: "刺激的で知的な相手に惹かれます。会話が弾む恋愛が理想で、自由を大切にします。",
    career: "メディア・教育・通信・翻訳など、情報と言葉を扱う分野で輝きます。",
    money: "収入は多様なルートから。ただし計画性がないと散財しやすいです。",
    health: "肺と神経系に注意。精神的な疲れが体に出やすいです。",
    lucky: { color: "イエロー", number: 5, day: "水曜日", stone: "アクアマリン" },
    overallFortune: "水星の加護で情報と縁に恵まれます。知識を行動に結びつけることが豊かな人生の秘訣です。",
  },
  {
    name: "蟹座",
    nameEn: "Cancer",
    symbol: "♋",
    emoji: "🦀",
    element: "水",
    elementEn: "Water",
    quality: "活動宮",
    rulingPlanet: "月",
    rulingPlanetEmoji: "☽",
    dateRange: "6/22〜7/22",
    personality:
      "深い愛情と共感力を持つ、感受性豊かな魂。家族や愛する人を守る本能が強く、温かく包み込むような優しさがあります。",
    strengths: ["深い愛情と共感力", "強い直感力", "育てる才能", "高い記憶力と感性"],
    challenges: ["気分の波が激しい", "過去への執着", "傷つきやすさ"],
    love: "深く献身的に愛するタイプ。感情的な絆を重視し、安心できる関係を求めます。",
    career: "保育・介護・料理・不動産など、家や人を守る分野で才能発揮。",
    money: "家や家族のためには惜しみなく使います。貯蓄本能もあり、安定志向です。",
    health: "胃腸と感情の健康が連動します。ストレス管理が体調維持の鍵です。",
    lucky: { color: "シルバー", number: 2, day: "月曜日", stone: "ムーンストーン" },
    overallFortune: "月の女神の守護を受け、感情の豊かさが人生を彩ります。愛する人と共に歩む道に幸運が宿ります。",
  },
  {
    name: "獅子座",
    nameEn: "Leo",
    symbol: "♌",
    emoji: "🦁",
    element: "火",
    elementEn: "Fire",
    quality: "固定宮",
    rulingPlanet: "太陽",
    rulingPlanetEmoji: "☀",
    dateRange: "7/23〜8/22",
    personality:
      "生まれながらの王者の風格を持つ、輝く存在。創造力豊かで表現力があり、周囲を明るく照らすカリスマ性の持ち主です。",
    strengths: ["強いカリスマ性", "創造力と表現力", "寛大さと温かさ", "リーダーシップ"],
    challenges: ["プライドの高さ", "注目を求めすぎる", "権威的になりやすい"],
    love: "ドラマチックで情熱的な恋愛を好みます。愛する人を輝かせたい献身的な面も。",
    career: "芸術・エンターテインメント・経営・教育など、舞台に立つ分野で輝きます。",
    money: "派手な使い方をしやすいですが、稼ぐ力も大きい。贈り物や投資に縁があります。",
    health: "心臓と背骨の健康に注意。ストレスを解放するための自己表現が大切です。",
    lucky: { color: "ゴールド", number: 1, day: "日曜日", stone: "サファイア" },
    overallFortune: "太陽の輝きを宿し、どこにいても存在感を放ちます。自分らしく輝き続けることが最大の幸運を引き寄せます。",
  },
  {
    name: "乙女座",
    nameEn: "Virgo",
    symbol: "♍",
    emoji: "👧",
    element: "地",
    elementEn: "Earth",
    quality: "柔軟宮",
    rulingPlanet: "水星",
    rulingPlanetEmoji: "☿",
    dateRange: "8/23〜9/22",
    personality:
      "緻密な分析力と完璧主義を持つ、知性派。実用的で勤勉、細部への注意力が高く、人の役に立つことに喜びを感じます。",
    strengths: ["高い分析力と注意力", "実用的な問題解決能力", "勤勉さと誠実さ", "服務精神の高さ"],
    challenges: ["完璧主義による自己批判", "批判的になりやすい", "心配症になりやすい"],
    love: "慎重に相手を見極めます。知性的で誠実な相手との静かで深い愛を求めます。",
    career: "医療・研究・会計・品質管理など、精度と誠実さが求められる分野で活躍。",
    money: "細かく管理する節約上手。ただし心配のあまり使えないこともあります。",
    health: "消化器系に注意。完璧主義からくるストレスを適度に解放することが大切です。",
    lucky: { color: "ネイビー", number: 5, day: "水曜日", stone: "サーペンティン" },
    overallFortune: "水星の恵みで細やかな才能が花開きます。完璧を求めつつも、ありのままの自分を受け入れることで更なる幸運が訪れます。",
  },
  {
    name: "天秤座",
    nameEn: "Libra",
    symbol: "♎",
    emoji: "⚖️",
    element: "風",
    elementEn: "Air",
    quality: "活動宮",
    rulingPlanet: "金星",
    rulingPlanetEmoji: "♀",
    dateRange: "9/23〜10/23",
    personality:
      "美と調和を愛する外交家。公平さを重んじ、人間関係を大切にします。優雅でセンスが良く、争いを嫌う平和主義者です。",
    strengths: ["優れた外交力と調整能力", "高い審美センス", "公平な判断力", "魅力的な社交性"],
    challenges: ["優柔不断になりやすい", "他者の意見に流されやすい", "自己主張が苦手"],
    love: "ロマンチックで理想の恋愛を求めます。美しい関係を育む芸術的な恋人です。",
    career: "法律・外交・デザイン・人事など、バランスと美を必要とする分野で輝きます。",
    money: "美的なものへの出費が多い傾向。収支バランスを意識することが重要です。",
    health: "腎臓と腰に注意。精神的なバランスが体調に直結します。",
    lucky: { color: "ピンク", number: 6, day: "金曜日", stone: "ローズクォーツ" },
    overallFortune: "金星の美の恵みを受け、人生に優雅さと豊かさをもたらします。人との絆を大切にすることが幸運の源です。",
  },
  {
    name: "蠍座",
    nameEn: "Scorpio",
    symbol: "♏",
    emoji: "🦂",
    element: "水",
    elementEn: "Water",
    quality: "固定宮",
    rulingPlanet: "冥王星",
    rulingPlanetEmoji: "♇",
    dateRange: "10/24〜11/22",
    personality:
      "深い洞察力と強い意志を持つ、神秘的な存在。秘密を守り、物事の本質を見抜く鋭い直感と、再生・変容のパワーがあります。",
    strengths: ["深い洞察力と直感", "強い意志力と集中力", "変革と再生の力", "忠実さと深い愛情"],
    challenges: ["嫉妬深くなりやすい", "秘密主義すぎる", "復讐心が芽生えやすい"],
    love: "全身全霊で愛する一途なタイプ。深い絆と信頼を最も大切にします。",
    career: "捜査・心理・外科・金融など、深く掘り下げる作業や秘密を扱う分野で才能発揮。",
    money: "他者の資金を動かす才能があります。相続や投資に縁があることも。",
    health: "生殖器と排泄器官に注意。感情の浄化がデトックスに繋がります。",
    lucky: { color: "ダークレッド", number: 8, day: "火曜日", stone: "オブシディアン" },
    overallFortune: "冥王星の変容の力を持ち、困難を乗り越えるたびにより強く再生できます。深い信念が最終的な勝利をもたらします。",
  },
  {
    name: "射手座",
    nameEn: "Sagittarius",
    symbol: "♐",
    emoji: "🏹",
    element: "火",
    elementEn: "Fire",
    quality: "柔軟宮",
    rulingPlanet: "木星",
    rulingPlanetEmoji: "♃",
    dateRange: "11/23〜12/21",
    personality:
      "自由と冒険を愛する哲学者。楽観的でエネルギッシュ、真理を探求し、広い視野で世界を見渡す開放的な魂です。",
    strengths: ["楽観的で前向きな姿勢", "広い視野と哲学的思考", "冒険心と自由への情熱", "正直さと率直さ"],
    challenges: ["無責任になりやすい", "飽きっぽい", "デリカシーに欠けることも"],
    love: "自由な恋愛を求め、知的で冒険を共にできるパートナーを望みます。",
    career: "教育・旅行・出版・哲学・法律など、知識と自由を求める分野で活躍。",
    money: "金運は良いですが、楽観的すぎて無計画になりがちです。",
    health: "腰と肝臓に注意。アクティブな活動でエネルギーを発散することが大切です。",
    lucky: { color: "パープル", number: 3, day: "木曜日", stone: "ターコイズ" },
    overallFortune: "木星の幸運と拡大の力に守られ、人生のあらゆる場面で可能性が広がります。信念と冒険心が最大の味方です。",
  },
  {
    name: "山羊座",
    nameEn: "Capricorn",
    symbol: "♑",
    emoji: "🐐",
    element: "地",
    elementEn: "Earth",
    quality: "活動宮",
    rulingPlanet: "土星",
    rulingPlanetEmoji: "♄",
    dateRange: "12/22〜1/19",
    personality:
      "忍耐強く野心的な実力者。責任感が強く、着実に目標へ向かって登り続ける山羊のような精神力の持ち主です。",
    strengths: ["高い責任感と自己管理力", "忍耐強さと粘り強さ", "実用的な判断力", "野心と長期的な計画力"],
    challenges: ["悲観的になりやすい", "仕事優先で私生活が疎かになりがち", "冷淡に見られやすい"],
    love: "慎重に選んだパートナーに対して責任ある愛を示します。長期的な関係を好みます。",
    career: "経営・政治・建築・金融など、長期的な努力が実る分野で成功します。",
    money: "堅実で計画的な金銭管理が得意。着実な資産形成が得意です。",
    health: "骨・関節・皮膚に注意。過労になりやすいため、休息を意識しましょう。",
    lucky: { color: "ブラック", number: 4, day: "土曜日", stone: "オニキス" },
    overallFortune: "土星の規律と時間の力に守られ、遅咲きでも確実に頂点を極める運命です。努力は必ず報われます。",
  },
  {
    name: "水瓶座",
    nameEn: "Aquarius",
    symbol: "♒",
    emoji: "🏺",
    element: "風",
    elementEn: "Air",
    quality: "固定宮",
    rulingPlanet: "天王星",
    rulingPlanetEmoji: "⛢",
    dateRange: "1/20〜2/18",
    personality:
      "独創的で革新的な未来の先駆者。人道主義的精神を持ち、既成概念にとらわれない自由な発想で時代を変えようとする革命家です。",
    strengths: ["独創的な発想力", "人道主義と博愛精神", "高い知性と分析力", "革新への情熱"],
    challenges: ["感情表現が苦手", "頑固な理想主義", "孤立しやすい"],
    love: "友情から始まる知的な愛を求めます。自由と個性を尊重し合えるパートナーが理想です。",
    career: "テクノロジー・社会改革・科学・NGOなど、未来と社会に関わる分野で才能発揮。",
    money: "お金への執着は薄いですが、革新的なビジネスで大きく稼ぐ可能性も。",
    health: "足首と循環器系に注意。規則正しい生活リズムを心がけましょう。",
    lucky: { color: "エレクトリックブルー", number: 7, day: "土曜日", stone: "アメジスト" },
    overallFortune: "天王星の革新エネルギーを受け、時代を先取りする視点が最大の強みです。独自の道を切り拓くことで運命が開花します。",
  },
  {
    name: "魚座",
    nameEn: "Pisces",
    symbol: "♓",
    emoji: "🐟",
    element: "水",
    elementEn: "Water",
    quality: "柔軟宮",
    rulingPlanet: "海王星",
    rulingPlanetEmoji: "♆",
    dateRange: "2/19〜3/20",
    personality:
      "豊かな感受性と直感力を持つ、夢想家。共感力が高く、芸術や霊性への親和性が強い。無限の優しさと愛で周囲を包みます。",
    strengths: ["深い共感力と感受性", "芸術的才能と想像力", "鋭い直感力", "無条件の愛情"],
    challenges: ["現実逃避の傾向", "依存心が強くなりやすい", "境界線を引くのが難しい"],
    love: "深く夢のような愛を求めます。相手のために自己犠牲を厭わない献身的な恋愛をします。",
    career: "芸術・音楽・ヒーリング・映画など、感性と想像力を使う分野で輝きます。",
    money: "金銭管理が苦手な傾向。信頼できる人のサポートが金運アップに繋がります。",
    health: "足と免疫系に注意。メンタルと体が強く連動するため精神面のケアが大切です。",
    lucky: { color: "シーグリーン", number: 7, day: "木曜日", stone: "アクアマリン" },
    overallFortune: "海王星の神秘と直感の恵みを受け、目に見えない縁に守られています。自分の感性を信じることが最大の幸運を引き寄せます。",
  },
];

export function getZodiacSign(month: number, day: number): ZodiacSign {
  const dates = [
    [1, 20], [2, 19], [3, 21], [4, 20], [5, 21], [6, 22],
    [7, 23], [8, 23], [9, 23], [10, 24], [11, 23], [12, 22],
  ];
  // インデックス: 0=水瓶座, 1=魚座, ..., 11=山羊座
  const signOrder = [10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  for (let i = 0; i < 12; i++) {
    const [m, d] = dates[i];
    if (month === m && day >= d) {
      return ZODIAC_SIGNS[signOrder[i]];
    }
    if (month === m && day < d) {
      return ZODIAC_SIGNS[signOrder[(i - 1 + 12) % 12]];
    }
  }
  return ZODIAC_SIGNS[9]; // 山羊座（デフォルト）
}

export function getChineseZodiac(year: number): string {
  const animals = ["鼠", "牛", "虎", "兎", "竜", "蛇", "馬", "羊", "猿", "鶏", "犬", "猪"];
  return animals[(year - 4) % 12];
}
