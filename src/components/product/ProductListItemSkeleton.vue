<template>
  <div class="flex flex-col">
      <div class="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 lg:aspect-none group-hover:opacity-75 lg:h-80">
        <PhotoIcon class="p-8 rounded-md object-cover text-gray-300" aria-hidden="true" />
      </div>
    <div class="mt-6 flex flex-row justify-between">
      <div class="w-1/3 h-4 bg-gray-300 rounded dark:bg-gray-300"></div>
      <div class="w-1/5 h-4 bg-gray-300 rounded dark:bg-gray-300"></div>
    </div>
    <div class="mt-3 w-2/3 h-4 bg-gray-200 rounded dark:bg-gray-200"></div>
  </div>
</template>

<script setup>
	import { PhotoIcon } from "@heroicons/vue/24/outline"
</script>