<template>
	<div class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 lg:aspect-none group-hover:opacity-75 lg:h-80">
		<img :src="product.imageSrc" :alt="product.imageAlt" class="h-full w-full object-cover object-center lg:h-full lg:w-full" />
	</div>
	<div class="mt-4 flex justify-between">
		<div>
			<h3 class="text-lg text-gray-700">
				<RouterLink :to="`/produkt/${product.id}`">
					<span aria-hidden="true" class="absolute inset-0" />
					{{ product.name }}
				</RouterLink>
			</h3>
			<p class="mt-1 text-sm text-gray-500">{{ product.color }}</p>
		</div>
		<p class="text-sm font-medium text-gray-900">{{ product.price }} PLN</p>
	</div>
</template>

<script setup>
	defineProps({
		product: Object
	})
</script>