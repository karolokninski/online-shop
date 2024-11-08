<template>
  <TopBar></TopBar>
  <div class="bg-white pt-16">
    <div v-if="productsStore.loading" class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
      <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        <div v-for="n in 8" :key="n" class="animate-pulse group relative">
          <ProductListItemSkeleton></ProductListItemSkeleton>
        </div>
      </div>
    </div>

    <div v-else-if="productsStore.products.length" class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
      <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        <div v-for="product in productsStore.products" :key="product.id" class="group relative">
          <ProductListItem :product="{ id: product.id, name: product.name, price: product.price, description: product.description, mainImage: product.main_image, imageAlt: product.name }"></ProductListItem>
        </div>
      </div>
    </div>

    <h2 v-else class="pt-24 text-black">Brak wyników</h2>
  </div>
</template>

<script setup>
import TopBar from '@/components/TopBar.vue';
import ProductListItem from '@/components/product/ProductListItem.vue';
import ProductListItemSkeleton from '@/components/product/ProductListItemSkeleton.vue';
import { useRoute } from 'vue-router';
import { computed, watch } from 'vue';
import { useProductsStore } from '@/stores/products';

const productsStore = useProductsStore();
const router = useRoute();
const query = computed(() => router.query.q);

watch(
  query,
  (query) => {
    productsStore.fetchProducts(query);
  },
  { immediate: true }
);
</script>
