<template>
  <div class="flex flex-row items-center justify-between w-full py-2 px-6 sm:px-0">
    <div class="relative flex items-center mx-auto h-12 w-full bg-white"> 
      <label for="product-search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Szukaj</label>
      <div class="relative w-full">
        <input
          type="text"
          id="product-search" 
          v-model="searchStore.query"
          @keyup.enter="handleSearch"
          class="block w-full h-10 px-4 pe-20 text-md text-black border border-gray-400 rounded-xl bg-gray-50 focus:ring-gray-400 focus:border-gray-400"
          style="width: calc(100% - 1px);"
          placeholder="Czego szukasz?" />
        <XCircleIcon v-show="showCancelButton" @click="searchStore.query = ''" class="text-black absolute end-12 bottom-2 h-6 w-6"></XCircleIcon>
        <button type="submit" @click="handleSearch" class="text-gray-900 absolute h-10 w-10 px-2.5 py-auto end-0 bottom-0 rounded-xl bg-gray-400 hover:bg-gray-500 focus:outline-none active:bg-gray-400">
          <MagnifyingGlassIcon></MagnifyingGlassIcon>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue'
  import { useRouter } from 'vue-router'
  import { useSearchStore } from '@/stores/search'
  import { XCircleIcon, MagnifyingGlassIcon } from '@heroicons/vue/24/outline'

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
