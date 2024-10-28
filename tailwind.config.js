/** @type {import('tailwindcss').Config} */

import colors from 'tailwindcss/colors'
import aspectRatio from '@tailwindcss/aspect-ratio'
import forms from '@tailwindcss/forms'


export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      screens: {
        sm: '480px',
        md: '768px',
        lg: '976px',
        xl: '1440px',
      },
      colors: {
        ...colors,
        primary: {
          DEFAULT: '#1170ED',
          500: '#0E70ED',
          600: '#0552b3'
        },
      },
      fontFamily: {
        sans: ['Graphik', 'sans-serif'],
        serif: ['Merriweather', 'serif'],
      },
      spacing: {
        '128': '32rem',
        '144': '36rem',
      },
      borderRadius: {
        '4xl': '2rem',
      },
      gridTemplateRows: {
        '[auto,auto,1fr]': 'auto auto 1fr',
      }
    }
  },
  plugins: [
    aspectRatio,
    forms
  ],
}

