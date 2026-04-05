// 四柱推命 計算ライブラリ

export const HEAVENLY_STEMS = [
  "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸",
];

export const EARTHLY_BRANCHES = [
  "子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥",
];

export const STEM_ELEMENTS = [
  "木", "木", "火", "火", "土", "土", "金", "金", "水", "水",
];

export const BRANCH_ELEMENTS = [
  "水", "土", "木", "木", "土", "火", "火", "土", "金", "金", "土", "水",
];

export const STEM_YIN_YANG = [
  "陽", "陰", "陽", "陰", "陽", "陰", "陽", "陰", "陽", "陰",
];

export const BRANCH_ANIMALS = [
  "鼠", "牛", "虎", "兎", "竜", "蛇", "馬", "羊", "猿", "鶏", "犬", "猪",
];

export const ELEMENT_COLORS: Record<string, string> = {
  木: "#22c55e",
  火: "#ef4444",
  土: "#f59e0b",
  金: "#94a3b8",
  水: "#3b82f6",
};

export const ELEMENT_BG: Record<string, string> = {
  木: "rgba(34,197,94,0.15)",
  火: "rgba(239,68,68,0.15)",
  土: "rgba(245,158,11,0.15)",
  金: "rgba(148,163,184,0.15)",
  水: "rgba(59,130,246,0.15)",
};

export interface Pillar {
  stem: string;
  branch: string;
  stemIndex: number;
  branchIndex: number;
  stemElement: string;
  branchElement: string;
  yinYang: string;
  animal: string;
}

export interface FourPillarsResult {
  year: Pillar;
  month: Pillar;
  day: Pillar;
  hour: Pillar | null;
  dayMaster: DayMasterReading;
  elementBalance: ElementBalance;
  overallFortune: string;
  yearFortune: string;
}

export interface DayMasterReading {
  stem: string;
  element: string;
  yinYang: string;
  title: string;
  personality: string;
  strengths: string[];
  challenges: string[];
  fortune: string;
}

export interface ElementBalance {
  counts: Record<string, number>;
  dominant: string;
  lacking: string;
  analysis: string;
}

function makePillar(stemIndex: number, branchIndex: number): Pillar {
  const si = ((stemIndex % 10) + 10) % 10;
  const bi = ((branchIndex % 12) + 12) % 12;
  return {
    stem: HEAVENLY_STEMS[si],
    branch: EARTHLY_BRANCHES[bi],
    stemIndex: si,
    branchIndex: bi,
    stemElement: STEM_ELEMENTS[si],
    branchElement: BRANCH_ELEMENTS[bi],
    yinYang: STEM_YIN_YANG[si],
    animal: BRANCH_ANIMALS[bi],
  };
}

// 年柱計算
function getYearPillar(year: number): Pillar {
  const stemIndex = (year - 4) % 10;
  const branchIndex = (year - 4) % 12;
  return makePillar(stemIndex, branchIndex);
}

// 月柱計算（節入り近似）
// 節: 寅月=立春(2/4頃), 卯月=啓蟄(3/6頃), 辰月=清明(4/5頃)
// 巳月=立夏(5/6頃), 午月=芒種(6/6頃), 未月=小暑(7/7頃)
// 申月=立秋(8/7頃), 酉月=白露(9/8頃), 戌月=寒露(10/8頃)
// 亥月=立冬(11/7頃), 子月=大雪(12/7頃), 丑月=小寒(1/6頃)
function getChineseMonthIndex(month: number, day: number): number {
  // 節入り近似日（各月）
  const setsuri = [6, 4, 6, 5, 6, 6, 7, 7, 8, 8, 7, 7];
  // 西暦月→中国月インデックス（寅月=0）
  // Jan(1)→丑月(12番目の節)を経て…
  // 寅=2, 卯=3, 辰=4, 巳=5, 午=6, 未=7, 申=8, 酉=9, 戌=10, 亥=11, 子=0, 丑=1
  const branchMap = [11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; // Jan〜Dec の地支インデックス（节前は-1）
  let idx = branchMap[month - 1];
  if (day < setsuri[month - 1]) {
    idx = (idx - 1 + 12) % 12;
  }
  return idx; // 0=寅月, 1=卯月, ...
}

function getMonthPillar(
  month: number,
  day: number,
  yearStemIndex: number
): Pillar {
  const chineseMonthIdx = getChineseMonthIndex(month, day);
  // 地支: 寅(2)が月1なので branchIndex = (chineseMonthIdx + 2) % 12
  const branchIndex = (chineseMonthIdx + 2) % 12;
  // 天干: 年干から月干を計算 （五虎遁年法）
  // 甲/己年→寅月は丙, 乙/庚→戊, 丙/辛→庚, 丁/壬→壬, 戊/癸→甲
  const stemStartIndex = ((yearStemIndex % 5) * 2 + 2) % 10;
  const stemIndex = (stemStartIndex + chineseMonthIdx) % 10;
  return makePillar(stemIndex, branchIndex);
}

// 日柱計算
// 参照: 1900年1月1日は甲戌日（位置10）
function getDayPillar(year: number, month: number, day: number): Pillar {
  const ref = new Date(Date.UTC(1900, 0, 1));
  const target = new Date(Date.UTC(year, month - 1, day));
  const diffDays = Math.floor(
    (target.getTime() - ref.getTime()) / (1000 * 60 * 60 * 24)
  );
  const position = ((10 + diffDays) % 60 + 60) % 60;
  const stemIndex = position % 10;
  const branchIndex = position % 12;
  return makePillar(stemIndex, branchIndex);
}

// 時柱計算（五鼠遁日法）
function getHourPillar(hour: number, dayStemIndex: number): Pillar {
  // 時支: 子(0)=23-1時, 丑(1)=1-3時, ...
  let branchIndex: number;
  if (hour >= 23) branchIndex = 0;
  else branchIndex = Math.floor((hour + 1) / 2);

  // 時干: 日干から算出
  const stemStartIndex = (dayStemIndex % 5) * 2;
  const stemIndex = (stemStartIndex + branchIndex) % 10;
  return makePillar(stemIndex, branchIndex);
}

const DAY_MASTER_READINGS: Record<string, DayMasterReading> = {
  甲: {
    stem: "甲",
    element: "木",
    yinYang: "陽",
    title: "甲木 — 天高くそびえる大樹",
    personality:
      "直立する大木のように、強い意志と高い理想を持ちます。リーダーシップがあり、成長と発展を求める精神の持ち主。正直で誠実、人々を導く力があります。",
    strengths: ["強いリーダーシップ", "高い理想と志", "誠実さと正直さ", "粘り強い実行力"],
    challenges: ["頑固になりやすい", "融通が利きにくい", "プライドが傷つきやすい"],
    fortune:
      "上昇志向が強く、目標に向かって真っ直ぐ進む力があります。人生の中で大きな成功を収める可能性を秘めていますが、柔軟性を持つことでさらなる飛躍が期待できます。",
  },
  乙: {
    stem: "乙",
    element: "木",
    yinYang: "陰",
    title: "乙木 — しなやかに伸びる蔦",
    personality:
      "柔軟な蔦のように、環境に適応しながら成長します。穏やかで協調性があり、芸術的センスに優れています。周囲との調和を大切にする優しい心の持ち主です。",
    strengths: ["高い適応力", "芸術的センス", "協調性の高さ", "細やかな気配り"],
    challenges: ["優柔不断になりやすい", "自己主張が苦手", "依存心が出やすい"],
    fortune:
      "人との繋がりを通じて運が開けます。美的センスや創造力を活かせる分野で才能を発揮できます。周囲の人々との協力関係が成功の鍵となるでしょう。",
  },
  丙: {
    stem: "丙",
    element: "火",
    yinYang: "陽",
    title: "丙火 — 万物を照らす太陽",
    personality:
      "太陽のように輝き、周囲を明るく照らす存在。情熱的でエネルギッシュ、人々を引き付ける圧倒的な魅力があります。明朗活発で、どんな場所でも中心的存在になります。",
    strengths: ["強いカリスマ性", "情熱と行動力", "明るく前向きな性格", "直観力の鋭さ"],
    challenges: ["感情の起伏が激しい", "衝動的になりやすい", "細部への注意が散漫"],
    fortune:
      "生まれながらの輝きと魅力で、多くの人を引きつけます。人生のあらゆる場面で注目される存在になりますが、エネルギーのコントロールが成功の鍵です。",
  },
  丁: {
    stem: "丁",
    element: "火",
    yinYang: "陰",
    title: "丁火 — 深夜を照らすろうそくの炎",
    personality:
      "ろうそくの炎のように、温かく内側から照らします。繊細で直感力があり、深い洞察力を持ちます。感受性が豊かで、芸術や精神的なものへの親和性が高いです。",
    strengths: ["深い洞察力と直感", "豊かな感受性", "芸術的才能", "温かい人間性"],
    challenges: ["神経質になりやすい", "傷つきやすい", "内省的すぎる"],
    fortune:
      "精神的な深さと直感力が人生の武器になります。表舞台より裏方でその力を発揮するタイプです。創造的な仕事や人を助ける仕事で大きな成果を上げられます。",
  },
  戊: {
    stem: "戊",
    element: "土",
    yinYang: "陽",
    title: "戊土 — 万物を支える大地",
    personality:
      "大地のように安定していて頼りになります。誠実で忍耐強く、人々を支える力があります。堅実で保守的、信頼される人柄が特徴です。",
    strengths: ["揺るぎない安定感", "高い忍耐力と持続力", "誠実さと信頼性", "包容力の大きさ"],
    challenges: ["変化への対応が遅い", "頑固になりやすい", "行動が慎重すぎる"],
    fortune:
      "着実に努力を積み重ねることで人生を豊かにできます。急いで成功を求めるより、長期的な視点で取り組むことが繁栄への道です。人からの信頼が最大の財産になります。",
  },
  己: {
    stem: "己",
    element: "土",
    yinYang: "陰",
    title: "己土 — 豊かに実る田畑",
    personality:
      "肥沃な田畑のように、育てる力があります。注意深く細やかで、実務的な才能に優れています。人の世話をすることが得意で、周囲から頼られる存在です。",
    strengths: ["細やかな注意力", "実務能力の高さ", "人を育てる才能", "几帳面さと丁寧さ"],
    challenges: ["心配性になりやすい", "過干渉になる場合がある", "決断が遅い"],
    fortune:
      "コツコツと努力する姿勢が実を結びます。人を助けることで自分自身も豊かになる運命を持っています。教育や医療、サポート業務で特に才能を発揮できます。",
  },
  庚: {
    stem: "庚",
    element: "金",
    yinYang: "陽",
    title: "庚金 — 万物を断つ剛刃",
    personality:
      "鋼鉄のような強さと鋭さを持ちます。決断力があり、正義感が強く、目標達成への意志が固いです。白黒をはっきりさせる性格で、不公正なことを嫌います。",
    strengths: ["強い決断力と実行力", "揺るぎない正義感", "精神的な強さ", "高い目標設定能力"],
    challenges: ["妥協が難しい", "人間関係が荒くなりがち", "融通が利かない"],
    fortune:
      "強い意志と決断力で困難を突破する力があります。目標を定めたら一直線に進む力がありますが、時に人の意見を聞く柔軟さも必要です。正義と誠実さが成功の礎になります。",
  },
  辛: {
    stem: "辛",
    element: "金",
    yinYang: "陰",
    title: "辛金 — 光り輝く宝玉",
    personality:
      "宝石のように輝く才能を持ちます。完璧主義で美意識が高く、高い審美眼があります。洗練された感性と知性が魅力で、独自のスタイルを持っています。",
    strengths: ["高い美意識と審美眼", "完璧主義による質の高さ", "知性と洗練された感性", "独創性"],
    challenges: ["完璧主義による疲れ", "批判的になりやすい", "プライドが高い"],
    fortune:
      "美的センスと知性を活かして輝ける人生が待っています。品質にこだわる姿勢が高い評価に繋がります。芸術、デザイン、高級品に関わる分野で才能を発揮できます。",
  },
  壬: {
    stem: "壬",
    element: "水",
    yinYang: "陽",
    title: "壬水 — 限りなく広がる大海",
    personality:
      "大海のように広い心と深い知恵を持ちます。適応力が高く、新しい環境にも柔軟に対処できます。知的好奇心が旺盛で、常に新しいことを学び吸収しようとします。",
    strengths: ["高い知性と探求心", "優れた適応力", "広い視野と包容力", "直感力の鋭さ"],
    challenges: ["方向性が定まりにくい", "感情の波が大きい", "飽きやすい面がある"],
    fortune:
      "広大な知識と洞察力で人生を切り開きます。多様な経験を通じて成長し続ける運命を持ちます。国際的な活動や研究・知識系の分野で大きな活躍が期待できます。",
  },
  癸: {
    stem: "癸",
    element: "水",
    yinYang: "陰",
    title: "癸水 — 澄み渡る清らかな泉",
    personality:
      "清らかな泉のように、純粋で深い感受性を持ちます。直感力に優れ、霊的な感性があります。思いやりが深く、人の痛みに共感できる優しい魂の持ち主です。",
    strengths: ["豊かな感受性と共感力", "鋭い直感力", "芸術的・霊的な感性", "深い思いやり"],
    challenges: ["感情に流されやすい", "傷つきやすい", "現実逃避の傾向"],
    fortune:
      "繊細な感受性が人生を豊かに彩ります。人の心を理解する力が最大の武器です。カウンセリング、芸術、スピリチュアルな分野での活躍が運気を高めます。",
  },
};

function getElementBalance(pillars: Pillar[]): ElementBalance {
  const counts: Record<string, number> = { 木: 0, 火: 0, 土: 0, 金: 0, 水: 0 };
  pillars.forEach((p) => {
    counts[p.stemElement]++;
    counts[p.branchElement]++;
  });

  const sorted = Object.entries(counts).sort((a, b) => b[1] - a[1]);
  const dominant = sorted[0][0];
  const lacking = sorted[sorted.length - 1][0];

  const analyses: Record<string, string> = {
    木: "命式に木の気が強く、成長・創造・発展の力に恵まれています。",
    火: "命式に火の気が強く、情熱・表現・輝きのエネルギーに満ちています。",
    土: "命式に土の気が強く、安定・信頼・持続力に優れた基盤があります。",
    金: "命式に金の気が強く、精密さ・決断力・洗練された才能があります。",
    水: "命式に水の気が強く、知恵・適応力・深い直感力に恵まれています。",
  };

  return {
    counts,
    dominant,
    lacking,
    analysis: analyses[dominant],
  };
}

function getOverallFortune(
  dayMaster: string,
  yearBranch: number,
  elementBalance: ElementBalance
): string {
  const elementForce: Record<string, string> = {
    木: "成長と飛躍の時期が巡ってきています。新しいことへの挑戦が吉。",
    火: "情熱と創造力が実を結ぶ時期です。人前に出る機会を積極的に活かしましょう。",
    土: "安定と充実が続く時期です。基盤を固め、長期的な計画に取り組むと吉。",
    金: "実力が認められ、結果が出やすい時期です。決断と行動が運を開きます。",
    水: "知識・経験が積み重なる時期です。学びと内省が次なる飛躍の準備になります。",
  };
  return elementForce[elementBalance.dominant] || "バランスの取れた命式で、総合的な運の強さがあります。";
}

function getYearFortune(currentYear: number, dayPillar: Pillar): string {
  const yearStem = (currentYear - 4) % 10;
  const yearBranch = (currentYear - 4) % 12;
  const interaction = (yearStem + dayPillar.stemIndex) % 5;
  const fortunes = [
    "今年は日主を助ける運気が巡り、自信を持って行動できる年です。新しい出会いや機会を積極的に掴みましょう。",
    "今年は財の気が高まり、金銭運・仕事運ともに上昇傾向にあります。努力が報われる一年です。",
    "今年は表現力・発信力が高まる年です。自分の才能をアピールするチャンスが訪れます。",
    "今年は基盤を固める時期です。焦らず着実に積み重ねることが来年以降の飛躍に繋がります。",
    "今年は変化と転換の年です。古いものを手放し、新しい流れに乗ることで運が開けます。",
  ];
  return fortunes[interaction];
}

export function calculateFourPillars(
  year: number,
  month: number,
  day: number,
  hour?: number
): FourPillarsResult {
  const yearPillar = getYearPillar(year);
  const monthPillar = getMonthPillar(month, day, yearPillar.stemIndex);
  const dayPillar = getDayPillar(year, month, day);
  const hourPillar = hour !== undefined ? getHourPillar(hour, dayPillar.stemIndex) : null;

  const allPillars = [yearPillar, monthPillar, dayPillar, ...(hourPillar ? [hourPillar] : [])];
  const elementBalance = getElementBalance(allPillars);

  const dayMaster = DAY_MASTER_READINGS[dayPillar.stem];
  const overallFortune = getOverallFortune(dayPillar.stem, yearPillar.branchIndex, elementBalance);
  const currentYear = new Date().getFullYear();
  const yearFortune = getYearFortune(currentYear, dayPillar);

  return {
    year: yearPillar,
    month: monthPillar,
    day: dayPillar,
    hour: hourPillar,
    dayMaster,
    elementBalance,
    overallFortune,
    yearFortune,
  };
}
