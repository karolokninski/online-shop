<template>
  <div class="bg-white">
    <TopBar></TopBar>
    
    <div class="tlo relative isolate px-6 pt-14 lg:px-8">
      <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
        <div class="hidden sm:mb-8 sm:flex sm:justify-center">
          
        </div>
        <div class="text-center">
          <h1 class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">Tech-bay</h1>
          <p class="mt-6 text-lg leading-8 text-gray-600">W naszym sklepie znajdziesz najwyższej jakości sprzęt komputerowy i podzepoły.</p>

        </div>
      </div>
      
      
    </div>
    



 


<Sale></Sale>

<News></News>
  </div>
  <Footer></Footer>
</template>
  
<script setup>
  import TopBar from '@/components/TopBar.vue';
  import Footer from '@/components/Footer.vue';
  import News from '@/components/newsletterisklepy.vue';
  import Sale from '@/components/sale.vue';
</script>
<style>
.tlo{
background-image: url('@/assets/tlo.jpg');
 background-size: cover;
background-position: center;
}
</style>