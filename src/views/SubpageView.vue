<template>
	<TopBar></TopBar>
  <div class="flex flex-col bg-white text-black pt-6 mx-auto md:w-1/2">
    <h1 class="text-3xl text-center">{{ subpage.title }}</h1>
    <div class="mt-4 text-lg text-center whitespace-pre-line" v-html="subpage.content"></div>
  </div>
</template>

<script setup>
  import TopBar from '@/components/TopBar.vue';
  import { ref, onMounted, watch } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'

  const API_URL = import.meta.env.VITE_API_URL
  const subpage = ref({})
  const route = useRoute()

  const fetchSubpage = async () => {
    try {
      const response = await axios.get(API_URL + `/subpages/${route.meta.id}`)
      subpage.value = response.data
    } catch (error) {
      console.error('Error fetching subpage:', error)
    }
  }

  onMounted(fetchSubpage)
  watch(route, fetchSubpage)
</script>