import { defineStore } from 'pinia'

export const useSearchStore = defineStore('search', {
  state: () => ({
    query: '',
    results: [],
    loading: false,
    error: null,
  }),
  actions: {
    async performSearch(query) {
      this.query = query;
      this.loading = true;
      this.error = null;
      try {
        const response = await fetch(`https://api.example.com/search?q=${query}`);
        const data = await response.json();
        this.results = data.results;
      } catch (err) {
        this.error = 'Error fetching search results.';
      } finally {
        this.loading = false;
      }
    }
  }
});
