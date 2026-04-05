import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "星命占い — 四柱推命・西洋占星術で人生を読む",
  description:
    "生年月日と性別を入力するだけで、四柱推命と西洋占星術があなたの人生・運命・性格を鑑定します。",
  openGraph: {
    title: "星命占い",
    description: "四柱推命・西洋占星術であなたの運命を読み解きます",
    locale: "ja_JP",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>
        <div className="stars-bg" aria-hidden="true" />
        <div className="relative z-10">{children}</div>
      </body>
    </html>
  );
}
