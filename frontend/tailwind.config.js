// frontend/tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}", // Include all relevant file types
  ],
  theme: {
    extend: {
      // Add custom theme settings here if needed (colors, fonts, etc.)
      backgroundImage: {
        // Example for hero background
        "hero-pattern": "url('/img/hero-background.jpg')", // Path relative to public folder
      },
    },
  },
  plugins: [],
};
