/** @type {import('tailwindcss').Config} */

const colors = require('tailwindcss/colors')

module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  enabled: false, //true for production build
  content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html',
          '../templates/*.html',
          '../templates/**/*.html'
      ],
  theme: {
    fontFamily: {
        display: ['Mitr', 'sans-serif'],
    },
    extend: {
      colors: {
        //just add this below and your all other tailwind colors willwork
      ...colors
 }
    },
  },
  variants: {},
  plugins: [],
}