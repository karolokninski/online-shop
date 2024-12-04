<template>
	<div class="bg-black aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 lg:aspect-none group-hover:opacity-75 lg:h-80">
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
		<div class="flex flex-col gap-1">
			<p class="text-md font-medium text-gray-900 text-right">{{ product.price }} PLN</p>
			<div class="flex flex-row gap-1 z-0 ml-auto opacity-0 group-hover:opacity-100">
				<div v-if="userStore.isAuthenticated" class="add-to-btn" @click="handleAddToFavorite(product.id)">
					<HeartIconSolid v-if="favoriteProductsStore.products.some(p => p.id === product.id)" class="h-6 w-6 text-gray-700"></HeartIconSolid>
					<HeartIcon v-else class="h-6 w-6 text-gray-700"></HeartIcon>
				</div>
				<RouterLink v-else to="/logowanie" class="add-to-btn">
					<HeartIcon class="h-6 w-6 text-gray-700"></HeartIcon>
				</RouterLink>
				<div class="add-to-btn" @click="handleAddToCart(product.id)">
					<ShoppingCartIcon class="h-6 w-6 text-black"></ShoppingCartIcon>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { PhotoIcon, HeartIcon, ShoppingCartIcon } from "@heroicons/vue/24/outline"
	import { HeartIcon as HeartIconSolid } from "@heroicons/vue/24/solid"
  import { useShoppingCartStore } from '@/stores/shoppingCart'
  import { useUserStore } from '@/stores/user'
  import { useFavoriteProductsStore } from '@/stores/favoriteProducts'

  const shoppingCartStore = useShoppingCartStore()
  const userStore = useUserStore()
  const favoriteProductsStore = useFavoriteProductsStore()

	defineProps({
		product: Object
	})

	const handleAddToFavorite = (productId) => {
		if (favoriteProductsStore.products.some(p => p.id === productId)) {
			favoriteProductsStore.removeProduct(productId)
		} else {
			favoriteProductsStore.addProduct(productId)
		}
	}

	const handleAddToCart = (productId) => {
    shoppingCartStore.addProduct(productId)
    shoppingCartStore.open = true
	}

	const formatImage = (image) => {
		return `data:image/jpeg;base64,${image}`
	}

	const truncateDescription = (description) => {
		return description?.length > 18 ? description.substring(0, 18) + '...' : description
	}
</script>

<style>
	.add-to-btn {
		border-radius: 0.5em;
		padding: 0.25em;
	}

	.add-to-btn:hover {
		background-color: rgb(240, 240, 240);
	}

	.add-to-btn:active {
		background-color: white;
	}
</style>