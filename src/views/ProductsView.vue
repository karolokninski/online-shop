<template>
	<TopBar></TopBar>
	<div class="bg-white pt-16">
		<div v-if="productsStore.products.length" class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
      <h2 v-if="query" class="text-2xl font-bold tracking-tight text-gray-900">Wyniki dla: "{{ query }}"</h2>
      <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        <div v-for="product in productsStore.products" :key="product.id" class="group relative">
					<ProductListItem :product="{ id: product.id, name: product.name, price: product.price, color: product.color, imageSrc: product.imageSrc, imageAlt: product.imageAlt }"></ProductListItem>
				</div>
			</div>
    </div>
		<h2 v-else class="pt-16">Brak wyników</h2>
	</div>
</template>
  
<script setup>
  import TopBar from '@/components/TopBar.vue';
  import ProductListItem from '@/components/product/ProductListItem.vue';
  import { useRoute } from 'vue-router';
  import { computed } from 'vue';
  import { useProductsStore } from '@/stores/products';

  const productsStore = useProductsStore();
	const router = useRoute();
	const query = computed(() => router.query.q);
</script>
  