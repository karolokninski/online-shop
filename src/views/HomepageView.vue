<template>
  <TopBar></TopBar>
  <HeroSection></HeroSection>
  <CategoryPrieview></CategoryPrieview>

  <NewsletterAndShops></NewsletterAndShops>
  <Footer></Footer>
</template>
  
<script setup>
  import TopBar from '@/components/TopBar.vue';
  import HeroSection from '@/components/homepage/HeroSection.vue';
  import CategoryPrieview from '@/components/homepage/CategoryPrieview.vue';
  import Sale from '@/components/homepage/Sales.vue';
  import NewsletterAndShops from '@/components/homepage/NewsletterAndShops.vue';
  import Footer from '@/components/Footer.vue';
</script>
<style>
  .tlo{
    background-image: url('@/assets/tlo.jpg');
    background-size: cover;
    background-position: center;
  }
</style>