import { defineStore } from 'pinia'
// import { useProductsStore } from '@/stores/products';
import { useUserStore } from '@/stores/user';
import axios from 'axios';

const userStore = useUserStore();
const API_URL = import.meta.env.VITE_API_URL;

export const useFavoriteProductsStore = defineStore('favoriteProducts', {
  state: () => ({
    products: []
  }),
  actions: {
    async fetchProducts() {
      const response = await axios.get(`${API_URL}/favorites/${userStore.id}`);
      this.products = response.data;

      console.log(response);
    },
    async addProduct(productId) {
      // const productsStore = useProductsStore()

      console.log(userStore.id);

      const response = await axios.post(`${API_URL}/favorites`, {
        user_id: userStore.id,
        product_id: productId
      });

      console.log(response);

      this.fetchProducts();

      // if (product) {
      //   const existingProduct = this.products.find(p => p.id === product.id)

      //   if (existingProduct) {
      //     existingProduct.quantity += 1
      //     existingProduct.totalPrice += product.price
      //   } else {
      //     this.products.unshift({
      //       ...product,
      //       quantity: 1,
      //       totalPrice: product.price
      //     })
      //   }
      // }
    },
    async removeProduct(productId) {
      const response = await axios.delete(`${API_URL}/favorites/${productId}`, {
        params: {
          user_id: userStore.id
        }
      });
      
      console.log(response);

      this.fetchProducts();
    },
  }
});
