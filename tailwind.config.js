/** @type {import('tailwindcss').Config} */
console.log('CONFIG OK')
module.exports = {
    content: [
      "./ccmtj/templates/ccmtj/**/*.html",       
      "./ccmtj/static/ccmtj/js/**/*.js"        
    ],
    theme: {
      extend: {
        fontFamily: {
          FuturaMedium: ['FuturaMedium', 'sans-serif'],
          FuturaLight: ['FuturaLight', 'sans-serif'],
          FuturaBold: ['FuturaBold', 'sans-serif'],
          FuturaBook: ['FuturaBook', 'sans-serif'],
          FuturaDemi: ['FuturaDemi', 'sans-serif'],
          FuturaExtraBold: ['FuturaExtraBold', 'sans-serif'],
        }
      },
    },
    plugins: [],
  }
  