<template>
  <div class="pb-6 text-gray-900">
    <div v-if="productsStore.loading">
      <div class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:gap-x-8">
        <div v-for="n in 8" :key="n" class="animate-pulse group relative">
          <ProductListItemSkeleton/>
        </div>
      </div>
    </div>

    <div v-else-if="productsStore.products.length">
      <h2 class="text-2xl font-bold mb-6 text-center text-gray-900">Ulubione produkty</h2>
      <div class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:gap-x-8">
        <div v-for="product in favProducts" :key="product.id" class="group relative">
          <ProductListItem
            :product="{
              id: product.id,
              name: product.name,
              price: product.price,
              description: product.description,
              mainImage: product.main_image,
              imageAlt: product.name
            }"
            :noCart="true"
          />
        </div>
      </div>
    </div>

    <h3 v-else class="text-2xl font-bold mb-6 text-center">Brak ulubionych produktów</h3>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from "vue";
import ProductListItem from "@/components/product/ProductListItem.vue";
import ProductListItemSkeleton from "@/components/product/ProductListItemSkeleton.vue";
import { useProductsStore } from "@/stores/products";
import { useFavoriteProductsStore } from '@/stores/favoriteProducts';

const productsStore = useProductsStore();
const favoriteProductsStore = useFavoriteProductsStore();
const favProducts = ref([]);
const loading = ref(false);

async function fetchProductById(productId) {
  try {
    await productsStore.fetchProducts(undefined, undefined, undefined, productId);
    const product = productsStore.products[0];
    console.log("produkt: ", product)
    return product;
  } catch (error) {
    console.error("Error fetching product by ID:", error);
    throw error;
  }
}

async function fetchFavoriteProducts() {
  if (loading.value) return;
  loading.value = true;

  try {
    await favoriteProductsStore.fetchProducts();
    const favoriteProductData = favoriteProductsStore.products;
    console.log("fav prod:",favoriteProductsStore.products);
    let products = [];

    for (const product of favoriteProductData) {
      const productId = product.id;
      const fetchedProduct = await fetchProductById(productId);
      products.push(fetchedProduct);
    }
    return products;
  } catch (error) {
      console.error("Error fetching favorite products:", error);
  } finally {
    loading.value = false;
  }
}

watch(
  () => favoriteProductsStore.products,
  async () => {
    if (!loading.value) {
      favProducts.value = await fetchFavoriteProducts();
    }
  },
  { immediate: true }
);

onMounted(async () => {
  if (favProducts.value.length === 0 && !loading.value) {
    favProducts.value = await fetchFavoriteProducts();
  }
});
</script>
