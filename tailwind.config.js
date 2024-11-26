/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ["./templates/**/" , 'node_modules/preline/dist/*.js'],
  theme: {
    extend: {
      fontFamily: {
        gummy: ['Sour Gummy']
      }
    },
  },
  plugins: [require('preline/plugin'),],
}

