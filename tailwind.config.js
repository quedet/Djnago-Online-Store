/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./shop/templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/line-clamp')
  ],
}
