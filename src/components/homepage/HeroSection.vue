<template>
  <div class="relative overflow-hidden bg-white">
    <div class="pb-80 pt-16 sm:pb-40 sm:pt-24 lg:pb-48 lg:pt-40">
      <div class="relative mx-auto max-w-7xl px-4 sm:static sm:px-6 lg:px-8">
        <div class="sm:max-w-lg">
          <h1 class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">Geeked.tech</h1>
          <p class="mt-4 text-xl text-gray-500">
            Odkryj najnowsze podzespoły, komputery i akcesoria na Geeked.tech. Twój sklep dla graczy i pasjonatów technologii – sprzęt najwyższej jakości w zasięgu ręki!
          </p>
        </div>
        <div>
          <div class="mt-10">
            <div aria-hidden="true" class="pointer-events-none lg:absolute lg:inset-y-0 lg:mx-auto lg:w-full lg:max-w-7xl">
              <div class="absolute transform sm:left-1/2 sm:top-0 sm:translate-x-8 lg:left-1/2 lg:top-1/2 lg:-translate-y-1/2 lg:translate-x-8">
                <div class="flex items-center space-x-6 lg:space-x-8">
                  <div class="grid shrink-0 grid-cols-1 gap-y-6 lg:gap-y-8">
                    <div class="h-64 w-44 overflow-hidden rounded-lg sm:opacity-0 lg:opacity-100">
                      <img :src="image1Src" alt="" class="size-full object-cover" />
                    </div>
                    <div class="h-64 w-44 overflow-hidden rounded-lg">
                      <img :src="image2Src" alt="" class="size-full object-cover" />
                    </div>
                  </div>
                  <div class="grid shrink-0 grid-cols-1 gap-y-6 lg:gap-y-8">
                    <div class="h-64 w-44 overflow-hidden rounded-lg">
                      <img :src="image3Src" alt="" class="size-full object-cover" />
                    </div>
                    <div class="h-64 w-44 overflow-hidden rounded-lg">
                      <img :src="image4Src" alt="" class="size-full object-cover" />
                    </div>
                    <div class="h-64 w-44 overflow-hidden rounded-lg">
                      <img :src="image5Src" alt="" class="size-full object-cover" />
                    </div>
                  </div>
                  <div class="grid shrink-0 grid-cols-1 gap-y-6 lg:gap-y-8">
                    <div class="h-64 w-44 overflow-hidden rounded-lg">
                      <img :src="image6Src" alt="" class="size-full object-cover" />
                    </div>
                    <div class="h-64 w-44 overflow-hidden rounded-lg">
                      <img :src="image7Src" alt="" class="size-full object-cover" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <RouterLink to="/produkty" class="inline-block rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-center font-medium text-white hover:bg-indigo-700">Przeglądaj produkty</RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import image1Src from '@/assets/o1.jpg';
import image2Src from '@/assets/o2.jpg';
import image3Src from '@/assets/o3.jpg';
import image4Src from '@/assets/o5.jpg';
import image5Src from '@/assets/kartygraficzne.jpg';
import image6Src from '@/assets/o4.jpg';
import image7Src from '@/assets/strefa.jpg';


</script>
