"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

const currentYear = new Date().getFullYear();

const YEARS = Array.from({ length: currentYear - 1923 }, (_, i) => currentYear - i);
const MONTHS = Array.from({ length: 12 }, (_, i) => i + 1);
const HOURS_LIST = [
  { label: "不明（省略）", value: "" },
  { label: "子時（23:00〜01:00）", value: "0" },
  { label: "丑時（01:00〜03:00）", value: "1" },
  { label: "寅時（03:00〜05:00）", value: "3" },
  { label: "卯時（05:00〜07:00）", value: "5" },
  { label: "辰時（07:00〜09:00）", value: "7" },
  { label: "巳時（09:00〜11:00）", value: "9" },
  { label: "午時（11:00〜13:00）", value: "11" },
  { label: "未時（13:00〜15:00）", value: "13" },
  { label: "申時（15:00〜17:00）", value: "15" },
  { label: "酉時（17:00〜19:00）", value: "17" },
  { label: "戌時（19:00〜21:00）", value: "19" },
  { label: "亥時（21:00〜23:00）", value: "21" },
];

function getDaysInMonth(year: number, month: number) {
  return new Date(year, month, 0).getDate();
}

export default function HomePage() {
  const router = useRouter();
  const [year, setYear] = useState<number>(1990);
  const [month, setMonth] = useState<number>(1);
  const [day, setDay] = useState<number>(1);
  const [gender, setGender] = useState<string>("male");
  const [hour, setHour] = useState<string>("");
  const [days, setDays] = useState<number[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const maxDay = getDaysInMonth(year, month);
    setDays(Array.from({ length: maxDay }, (_, i) => i + 1));
    if (day > maxDay) setDay(maxDay);
  }, [year, month, day]);

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    const params = new URLSearchParams({
      year: String(year),
      month: String(month),
      day: String(day),
      gender,
      ...(hour !== "" ? { hour } : {}),
    });
    router.push(`/result?${params.toString()}`);
  }

  return (
    <main className="min-h-screen flex flex-col items-center justify-center px-4 py-16">
      {/* ヘッダー */}
      <div className="text-center mb-12 slide-up">
        <div className="text-5xl mb-4" style={{ filter: "drop-shadow(0 0 20px rgba(201,162,39,0.6))" }}>
          ✦
        </div>
        <h1
          className="text-gold-gradient font-serif text-4xl md:text-5xl font-bold mb-3 tracking-widest"
          style={{
            fontFamily: "'Noto Serif JP', serif",
            background: "linear-gradient(135deg, #f0d060 0%, #c9a227 50%, #f5e88a 100%)",
            WebkitBackgroundClip: "text",
            WebkitTextFillColor: "transparent",
            backgroundClip: "text",
          }}
        >
          星命占い
        </h1>
        <p className="text-sm tracking-[0.4em] text-amber-400/60 uppercase mb-4">
          Celestial Fortune
        </p>
        <p style={{ color: "var(--text-secondary)", fontSize: "0.95rem", lineHeight: 1.8 }}>
          四柱推命と西洋占星術が、あなたの命式と星座から<br className="hidden sm:block" />
          人生・性格・運命を読み解きます
        </p>
      </div>

      {/* フォームカード */}
      <div className="glass-card-strong w-full max-w-lg p-8 slide-up delay-200">
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* 生年月日 */}
          <div>
            <label className="block text-amber-300/80 text-sm font-medium mb-3 tracking-wider">
              生年月日
            </label>
            <div className="grid grid-cols-3 gap-3">
              {/* 年 */}
              <div className="col-span-1">
                <label className="block text-xs text-amber-400/40 mb-1 text-center">年</label>
                <select
                  className="form-select"
                  value={year}
                  onChange={(e) => setYear(Number(e.target.value))}
                >
                  {YEARS.map((y) => (
                    <option key={y} value={y}>{y}</option>
                  ))}
                </select>
              </div>
              {/* 月 */}
              <div>
                <label className="block text-xs text-amber-400/40 mb-1 text-center">月</label>
                <select
                  className="form-select"
                  value={month}
                  onChange={(e) => setMonth(Number(e.target.value))}
                >
                  {MONTHS.map((m) => (
                    <option key={m} value={m}>{m}</option>
                  ))}
                </select>
              </div>
              {/* 日 */}
              <div>
                <label className="block text-xs text-amber-400/40 mb-1 text-center">日</label>
                <select
                  className="form-select"
                  value={day}
                  onChange={(e) => setDay(Number(e.target.value))}
                >
                  {days.map((d) => (
                    <option key={d} value={d}>{d}</option>
                  ))}
                </select>
              </div>
            </div>
          </div>

          {/* 性別 */}
          <div>
            <label className="block text-amber-300/80 text-sm font-medium mb-3 tracking-wider">
              性別
            </label>
            <div className="grid grid-cols-2 gap-3">
              {[
                { value: "male", label: "男性", icon: "♂" },
                { value: "female", label: "女性", icon: "♀" },
              ].map(({ value, label, icon }) => (
                <label
                  key={value}
                  className={`flex items-center justify-center gap-2 py-3 rounded-xl border cursor-pointer transition-all duration-200 ${
                    gender === value
                      ? "border-amber-400/60 bg-amber-400/10 text-amber-300"
                      : "border-white/10 bg-white/3 text-white/50 hover:border-white/20"
                  }`}
                >
                  <input
                    type="radio"
                    name="gender"
                    value={value}
                    checked={gender === value}
                    onChange={() => setGender(value)}
                    className="sr-only"
                  />
                  <span className="text-lg">{icon}</span>
                  <span className="font-medium">{label}</span>
                </label>
              ))}
            </div>
          </div>

          {/* 出生時間（任意） */}
          <div>
            <label className="block text-amber-300/80 text-sm font-medium mb-1 tracking-wider">
              出生時間
              <span className="ml-2 text-xs text-white/30 font-normal">（任意・四柱推命の時柱に使用）</span>
            </label>
            <select
              className="form-select"
              value={hour}
              onChange={(e) => setHour(e.target.value)}
            >
              {HOURS_LIST.map(({ label, value }) => (
                <option key={value} value={value}>{label}</option>
              ))}
            </select>
          </div>

          {/* 占うボタン */}
          <button
            type="submit"
            className="btn-primary"
            disabled={loading}
          >
            {loading ? (
              <span className="flex items-center justify-center gap-2">
                <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24" fill="none">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                </svg>
                鑑定中...
              </span>
            ) : (
              "✦ 今すぐ占う ✦"
            )}
          </button>
        </form>
      </div>

      {/* フッター */}
      <div className="mt-10 text-center">
        <p className="text-xs tracking-wider" style={{ color: "var(--text-secondary)" }}>
          四柱推命 · 西洋占星術 · 五行分析
        </p>
      </div>
    </main>
  );
}
