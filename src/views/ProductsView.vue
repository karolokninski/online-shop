<template>
  <TopBar></TopBar>
  <div class="pt-10">
    <ProductCategoryFilter></ProductCategoryFilter>
  </div>
</template>

<script setup>
import { computed, watch } from "vue";
import TopBar from '@/components/TopBar.vue';
import ProductCategoryFilter from '@/components/product/ProductCategoryFilter.vue';
import { useRoute } from 'vue-router';
import { useProductsStore } from '@/stores/products';

const productsStore = useProductsStore();
const router = useRoute();
const query = computed(() => router.query.q);

const productsPerPage = 12;

watch(query, (query) => {
  productsStore.fetchProducts(0, productsPerPage, query, undefined);
}, { immediate: true });
</script>
