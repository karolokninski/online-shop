<template>
	<TopBar></TopBar>
	<div class="bg-white pt-16">
		<div v-if="products.length" class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
      <h2 v-if="query" class="text-2xl font-bold tracking-tight text-gray-900">Wyniki dla: "{{ query }}"</h2>

      <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        <div v-for="product in products" :key="product.id" class="group relative">
					<ProductListItem :product="{ id: product.id, name: product.name, price: product.price, color: product.color, imageSrc: product.imageSrc, imageAlt: product.imageAlt }"></ProductListItem>
				</div>
			</div>
    </div>

		<h2 v-else class="pt-16">Brak wyników</h2>


		<!-- <ul v-if="filteredProducts.length">
		<li v-for="product in filteredProducts" :key="product.id">{{ product.name }}</li>
		</ul> -->

	</div>
</template>
  
<script setup>
  import TopBar from '@/components/TopBar.vue';
  import ProductListItem from '@/components/product/ProductListItem.vue';
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

	const products = [
		{
			id: 1,
			name: 'Basic Tee',
			imageSrc: 'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-01.jpg',
			imageAlt: "Front of men's Basic Tee in black.",
			price: '$35',
			color: 'Black',
		},
		{
			id: 2,
			name: 'Plus Fit Tee',
			imageSrc: 'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-02.jpg',
			imageAlt: "Front of men's Plus Fit Tee in white.",
			price: '$45',
			color: 'White',
		},
		{
			id: 3,
			name: 'Curved Hem Tee',
			imageSrc: 'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-03.jpg',
			imageAlt: "Front of men's Curved Hem Tee in charcoal grey.",
			price: '$45',
			color: 'Charcoal grey',
		},
		{
			id: 4,
			name: 'Long Sleeve Tee',
			imageSrc: 'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-04.jpg',
			imageAlt: "Front of men's Long Sleeve Tee in charcoal grey.",
			price: '$55',
			color: 'Charcoal grey',
		},
		{
			id: 5,
			name: 'Plus Fit Tee',
			imageSrc: 'https://tailwindui.com/img/ecommerce-images/product-page-01-related-product-02.jpg',
			imageAlt: "Front of men's Plus Fit Tee in white.",
			price: '$45',
			color: 'White',
		},
	]
</script>
  