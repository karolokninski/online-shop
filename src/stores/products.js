import { defineStore } from 'pinia'
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL;

export const useProductsStore = defineStore('products', {
  state: () => ({
    products: [],
    loading: false
  }),
  actions: {
    async fetchProducts(name) {
      this.loading = true;
      let NEW_API_URL = API_URL + '/products';
      
      if (name && name.trim() !== '') {
        NEW_API_URL += `?name=${encodeURIComponent(name)}`;
      }
      
      try {
        const response = await axios.get(NEW_API_URL);
        this.products = response.data.map((product) => ({
          ...product,
          name: product.product_name,
          stock: product.stock_quantity
        }));
        this.errorMessage = '';
      } catch (error) {
        console.error('Błąd podczas pobierania produktów:', error)
      } finally {
        this.loading = false; // End loading
      }
    }
  }
});
