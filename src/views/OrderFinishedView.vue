<template>
    <TopBar></TopBar>
    <div class="text-center  mt-12 p-4">
    <h1 class="text-3xl font-bold text-black-500 mb-2">Dziękujemy za złożenie zamówienia!</h1>
    <p class="text-sm text-gray-500">Twoje zamówienie jest w realizacji.</p>
    <img :src="logo" alt="Logo" class="mx-auto w-1/4 object-cover" />
  </div>
  </template>
<script setup>
  import TopBar from '@/components/TopBar.vue';
  import logo from '@/assets/dzieki.png';
  import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

onMounted(() => {
  const cookies = document.cookie.split(';').map(cookie => cookie.trim());
  const orderFinished = cookies.find(cookie => cookie.startsWith('order_finished='));

  if (!orderFinished || orderFinished.split('=')[1] !== 'true') {
    router.push('/');
  } else {
    document.cookie = "order_finished=; path=/; max-age=0";
  }
});
</script>