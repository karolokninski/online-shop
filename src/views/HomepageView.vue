<template>
  <TopBar></TopBar>
  <div class="bg-white pt-16">
    <div class="tlo relative isolate px-6 lg:px-8">
      <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
        <div class="text-center">
          <h1 class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">Geeked.tech</h1>
          <p class="mt-6 text-lg leading-8 text-gray-800">W naszym sklepie znajdziesz najwyższej jakości sprzęt komputerowy i podzepoły.</p>
        </div>
      </div>
    </div>
    <Sale></Sale>
    <NewsletterAndShops></NewsletterAndShops>
  </div>
  <Footer></Footer>
</template>
  
<script setup>
  import TopBar from '@/components/TopBar.vue';
  import Sale from '@/components/Sales.vue';
  import NewsletterAndShops from '@/components/NewsletterAndShops.vue';
  import Footer from '@/components/Footer.vue';
</script>
<style>
  .tlo{
    background-image: url('@/assets/tlo.jpg');
    background-size: cover;
    background-position: center;
  }
</style>