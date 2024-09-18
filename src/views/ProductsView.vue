<template>
	<div>
		<TopBar></TopBar>
		<h1 class="mt-64">Produkty</h1>
		<p v-if="query">Wyniki dla: "{{ query }}"</p>

		<!-- <ul v-if="filteredProducts.length">
		<li v-for="product in filteredProducts" :key="product.id">{{ product.name }}</li>
		</ul> -->

		<p v-else>Brak wyników</p>
	</div>
</template>
  
<script setup>
  import TopBar from '@/components/TopBar.vue';
  import { useRoute } from 'vue-router';
  import { computed } from 'vue';
  // import { useProductStore } from '../stores/products';
  // const productStore = useProductStore();
  
	const route = useRoute();
	const query = computed(() => route.query.q);
  
	// const filteredProducts = computed(() => {
	// 	return productStore.products.filter(product =>
	// 		product.name.toLowerCase().includes(query.value.toLowerCase())
	// 	);
	// });

	// return {
	// 	query,
	// 	filteredProducts
	// };
</script>
  