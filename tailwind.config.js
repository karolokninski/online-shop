/** @type {import('tailwindcss').Config} */

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
        primary: {
          DEFAULT: '#1170ED',
          500: '#0E70ED',
          600: '#0552b3'
        },
        'blue': '#1fb6ff',
        'purple': '#7e5bef',
        'pink': '#ff49db',
        'orange': '#ff7849',
        'green': '#13ce66',
        'yellow': '#ffc82c',
        'gray-dark': '#273444',
        'gray-light': '#d3dce6',
        gray: {
          DEFAULT: '#8a99b0',
          100: '#f9fafb',
          200: '#f1f5f9',
          300: '#e5eaf1',
          400: '#cfd6e1',
          500: '#a6b0c2',
          600: '#7c8699',
          700: '#586174',
          800: '#3b4557',
          900: '#262d3a',
        }
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

