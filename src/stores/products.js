import { defineStore } from 'pinia'

export const useProductsStore = defineStore('products', {
  state: () => ({
    products: [
      {
        id: 1,
        name: 'Basic Tee',
        imageSrc: 'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-01.jpg',
        imageAlt: "Front of men's Basic Tee in black.",
        price: '35',
        color: 'Black',
      },
      {
        id: 2,
        name: 'Plus Fit Tee',
        imageSrc: 'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-02.jpg',
        imageAlt: "Front of men's Plus Fit Tee in white.",
        price: '45',
        color: 'White',
      },
      {
        id: 3,
        name: 'Curved Hem Tee',
        imageSrc: 'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-03.jpg',
        imageAlt: "Front of men's Curved Hem Tee in charcoal grey.",
        price: '45',
        color: 'Charcoal grey',
      },
      {
        id: 4,
        name: 'Long Sleeve Tee',
        imageSrc: 'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-04.jpg',
        imageAlt: "Front of men's Long Sleeve Tee in charcoal grey.",
        price: '55',
        color: 'Charcoal grey',
      },
      {
        id: 5,
        name: 'Plus Fit Tee',
        imageSrc: 'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-02.jpg',
        imageAlt: "Front of men's Plus Fit Tee in white.",
        price: '45',
        color: 'White',
      },
      {
        id: 6,
        name: 'Throwback Hip Bag',
        href: '#',
        color: 'Salmon',
        price: '90',
        imageSrc: 'https://tailwindui.com/img/ecommerce-images/shopping-cart-page-04-product-01.jpg',
        imageAlt: 'Salmon orange fabric pouch with match zipper, gray zipper pull, and adjustable hip belt.',
      },
      {
        id: 7,
        name: 'Medium Stuff Satchel',
        href: '#',
        color: 'Blue',
        price: '32',
        imageSrc: 'https://tailwindui.com/img/ecommerce-images/shopping-cart-page-04-product-02.jpg',
        imageAlt:
          'Front of satchel with blue canvas body, black straps and handle, drawstring top, and front zipper pouch.',
      }
    ]
  }),
  actions: {
  }
});
