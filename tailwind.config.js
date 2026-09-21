/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        'cinema-bg': '#FAF9F6',
        'cinema-blue': '#1D4ED8',
        'cinema-blue-dark': '#1e3a8a',
        'cinema-yellow': '#FBBF24',
        'cinema-yellow-dark': '#d97706',
        'rating-d': '#EF4444',   // Red for Dewasa
        'rating-r': '#FBBF24',   // Yellow for Remaja
        'rating-su': '#22C55E'    // Green for Semua Umur/Anak
      },
      fontFamily: {
        sans: ['Outfit', 'Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
