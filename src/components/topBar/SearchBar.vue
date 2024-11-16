<template>
  <div class="flex flex-row items-center justify-between py-2 px-6 lg:px-8">
    <div class="relative flex items-center mx-auto h-12 w-80 bg-white"> 
      <label for="product-search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Szukaj</label>
      <div class="relative w-full">
        <input
          type="text"
          id="product-search" 
          v-model="searchStore.query"
          @keyup.enter="handleSearch"
          class="block w-full h-12 p-4 pe-20 text-md font-semibold text-black border border-gray-400 rounded-xl bg-gray-50 focus:ring-gray-400 focus:border-gray-400"
          style="width: calc(100% - 1px);"
          placeholder="Czego szukasz?" />
        <XCircleIcon v-show="showCancelButton" @click="searchStore.query = ''" class="text-black absolute end-12 bottom-3 h-6 w-6 mr-1"></XCircleIcon>
        <button type="submit" @click="handleSearch" class="text-white absolute h-12 w-12 px-3 py-auto end-0 bottom-0 rounded-xl bg-gray-400 hover:bg-gray-500 focus:outline-none active:bg-gray-400">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="black">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue'
  import { useRouter } from 'vue-router'
  import { useSearchStore } from '@/stores/search'
  import { XCircleIcon } from '@heroicons/vue/24/outline'

  const router = useRouter()
  const searchStore = useSearchStore()

  const handleSearch = () => {
    router.push({
      name: 'products',
      query: { q: searchStore.query }
    })
  }

  const showCancelButton = computed(() => {
    return searchStore.query.length
  })
</script>
