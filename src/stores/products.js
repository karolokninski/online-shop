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

        for (let i = 1000; i < 1150; i++) {
          this.products.push({
            id: i,
            product_name: 'sigma',
            category_id: 1,
            price: i,
            stock_quantity: 1,
            description: 'sigma',
            main_image: null,
            additional_images: [],
            created_at: null,
            name: 'sigma',
            stock: 1,
          });
        }
      } catch (error) {
        console.error('Błąd podczas pobierania produktów:', error);
      } finally {
        this.loading = false;
        console.log(this.products);
      }
    },
  },
});
