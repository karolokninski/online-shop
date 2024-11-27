import { defineStore } from 'pinia';
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL;

export const useProductsStore = defineStore('products', {
  state: () => ({
    products: [],
    loading: false,
  }),
  actions: {
    async fetchProducts(skip, limit, name, id) {
      this.loading = true;
      let NEW_API_URL = API_URL + '/products';
      const queryParams = [];

      if (skip) {
        queryParams.push(`skip=${encodeURIComponent(skip)}`);
      }
      if (limit) {
        queryParams.push(`limit=${encodeURIComponent(limit)}`);
      }
      if (name && name.trim() !== '') {
        queryParams.push(`name=${encodeURIComponent(name)}`);
      }
      if (id) {
        queryParams.push(`id=${encodeURIComponent(id)}`);
      }

      if (queryParams.length > 0) {
        NEW_API_URL += `?${queryParams.join('&')}`;
      }

      try {
        const response = await axios.get(NEW_API_URL);
        this.products = response.data.map((product) => ({
          ...product,
          name: product.product_name,
          stock: product.stock_quantity,
        }));
        this.errorMessage = '';


      } catch (error) {
        console.error('Błąd podczas pobierania produktów:', error);
      } finally {
        this.loading = false;
      }
    },
  },
});
