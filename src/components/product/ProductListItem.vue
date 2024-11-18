<template>
	<div class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 lg:aspect-none group-hover:opacity-75 lg:h-80">
		<img v-if="product.mainImage" :src="formatImage(product.mainImage)" :alt="product.imageAlt" class="h-full w-full object-cover object-center lg:h-full lg:w-full" />
		<PhotoIcon v-else class="p-8 rounded-md object-cover text-gray-300" aria-hidden="true" />
	</div>
	<div class="mt-4 flex justify-between">
		<div>
			<h3 class="text-lg text-gray-700">
				<RouterLink :to="`/produkt/${product.id}`">
					<span aria-hidden="true" class="absolute inset-0" />
					{{ product.name }}
				</RouterLink>
			</h3>
			<p class="mt-1 text-sm text-gray-500">{{ truncateDescription(product.description) }}</p>
		</div>
		<p class="text-md font-medium text-gray-900">{{ product.price }} PLN</p>
	</div>
</template>

<script setup>
	import { PhotoIcon } from "@heroicons/vue/24/outline"

	defineProps({
		product: Object
	})

	const formatImage = (image) => {
		return `data:image/jpeg;base64,${image}`
	}

	const truncateDescription = (description) => {
		return description?.length > 24 ? description.substring(0, 24) + '...' : description
	}
</script>