import { defineStore } from 'pinia'
import { useProductsStore } from '@/stores/products';

export const useShoppingCartStore = defineStore('shoppingCart', {
  state: () => ({
    open: false,
    products: [
      {
        id: 1,
        name: 'Throwback Hip Bag',
        href: '#',
        color: 'Salmon',
        price: '90',
        imageSrc: 'https://tailwindui.com/img/ecommerce-images/shopping-cart-page-04-product-01.jpg',
        imageAlt: 'Salmon orange fabric pouch with match zipper, gray zipper pull, and adjustable hip belt.',
        quantity: 1
      }
    ]
  }),
  actions: {
    addProduct(id) {
      const productsStore = useProductsStore();
      const product = productsStore.products.find(product => product.id == id)

      if (product) {
        const existingProduct = this.products.find(p => p.id === product.id);

        if (existingProduct) {
          existingProduct.quantity += 1;
        } else {
          this.products.unshift({
            ...product,
            quantity: 1
          });
        }
      }
    }
  }
});
