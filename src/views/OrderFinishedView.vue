<template>
  <TopBar></TopBar>
  <div class="text-center mt-12 p-4 text-gray-900">
    <h1 class="text-3xl font-bold text-black-500 mb-12">Dziękujemy za złożenie zamówienia!</h1>
    <!-- <p class="text-md font-bold text-gray-900 mb-8">Twoje zamówienie jest w realizacji.</p> -->
    <ShoppingBagIcon class="mx-auto w-40 object-cover" />
    <div class="mt-10 flex items-center justify-center gap-x-6">
      <RouterLink to="/"> <button class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Powrót do strony głównej</button></RouterLink>
    </div>
  </div>
</template>
<script setup>
import TopBar from '@/components/TopBar.vue';
import { ShoppingBagIcon } from '@heroicons/vue/24/outline';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useShoppingCartStore } from '@/stores/shoppingCart';

const router = useRouter();

onMounted(() => {
  const shoppingCartStore = useShoppingCartStore();
  if (!shoppingCartStore.isOrderFinished) {
    router.push('/');
  } else {
    shoppingCartStore.products = [];
  }
});
</script>