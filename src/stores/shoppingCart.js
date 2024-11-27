import { defineStore } from 'pinia'
import { useProductsStore } from '@/stores/products';

export const useShoppingCartStore = defineStore('shoppingCart', {
  state: () => ({
    open: false,
    products: [],
    isOrderFinished: false
  }),
  actions: {
    addProduct(id) {
      const productsStore = useProductsStore()
      const product = productsStore.products.find(product => product.id == id)

      if (product) {
        const existingProduct = this.products.find(p => p.id === product.id)

        if (existingProduct) {
          existingProduct.quantity += 1
          existingProduct.totalPrice += product.price
        } else {
          this.products.unshift({
            ...product,
            quantity: 1,
            totalPrice: product.price
          })
        }
      }
    },
    productsSum() {
      var sum = 0

      for (const product of this.products) {
        sum = sum + product.totalPrice
      }

      return sum
    },
    removeProduct(id) {
      this.products = this.products.filter(product => product.id !== id)
    },
    updateQuantity() {
      for (const product of this.products) {
        product.totalPrice = product.price * product.quantity
      }
    }
  },
  persist: {
    enabled: true,
    strategies: [
      {
        key: 'shoppingCart',
        storage: localStorage
      },
    ],
  }
});
