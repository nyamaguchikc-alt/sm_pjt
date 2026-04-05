import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        gold: {
          100: "#fef9e7",
          200: "#fdefc4",
          300: "#fad56a",
          400: "#f5c518",
          500: "#c9a227",
          600: "#a07820",
          700: "#7a5a18",
          800: "#523c10",
          900: "#2a1e08",
        },
        cosmic: {
          900: "#04040f",
          800: "#080820",
          700: "#0d0d32",
          600: "#141450",
          500: "#1a1a6e",
        },
      },
      fontFamily: {
        sans: [
          "Noto Sans JP",
          "Hiragino Sans",
          "Hiragino Kaku Gothic ProN",
          "Yu Gothic",
          "sans-serif",
        ],
        serif: [
          "Noto Serif JP",
          "Hiragino Mincho ProN",
          "Yu Mincho",
          "serif",
        ],
      },
      backgroundImage: {
        "cosmic-gradient":
          "radial-gradient(ellipse at top, #1a1a6e 0%, #080820 50%, #04040f 100%)",
      },
      animation: {
        twinkle: "twinkle 3s ease-in-out infinite",
        "float-up": "floatUp 0.6s ease-out forwards",
        shimmer: "shimmer 2s linear infinite",
      },
      keyframes: {
        twinkle: {
          "0%, 100%": { opacity: "1", transform: "scale(1)" },
          "50%": { opacity: "0.3", transform: "scale(0.7)" },
        },
        floatUp: {
          "0%": { opacity: "0", transform: "translateY(20px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
        shimmer: {
          "0%": { backgroundPosition: "-200% center" },
          "100%": { backgroundPosition: "200% center" },
        },
      },
    },
  },
  plugins: [],
};

export default config;
