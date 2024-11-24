<template>
  
  <div class="pb-6">
    <h2 class="text-2xl font-bold mb-6 text-center">Ulubione produkty</h2>
    <div v-if="productsStore.loading">
      <div class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:gap-x-8">
        <div v-for="n in 8" :key="n" class="animate-pulse group relative">
          <ProductListItemSkeleton />
        </div>
      </div>
    </div>


    <div v-else-if="productsStore.products.length">
      <div class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:gap-x-8">
        <div v-for="product in productsStore.products" :key="product.id" class="group relative">
          <ProductListItem
            :product="{
              id: product.id,
              name: product.name,
              price: product.price,
              description: product.description,
              mainImage: product.main_image,
              imageAlt: product.name
            }"
          />
        </div>
      </div>
    </div>

    <h3 v-else class="text-2xl font-bold mb-6 text-center">Brak ulubionych produktów</h3>
  </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import ProductListItem from "@/components/product/ProductListItem.vue";
import ProductListItemSkeleton from "@/components/product/ProductListItemSkeleton.vue";
import { useRoute } from "vue-router";
import { useProductsStore } from "@/stores/products";

const productsStore = useProductsStore();
const router = useRoute();
const query = computed(() => router.query.q);
const favProducts = [4, 5];


watch(
  query,
  async (query) => {
    await productsStore.fetchProducts(0, undefined, query, undefined); 
    productsStore.products = productsStore.products.filter((product) =>
      favProducts.includes(product.id)
    ); 
    console.log(productsStore.products); 
  },
  { immediate: true }
);
</script>
