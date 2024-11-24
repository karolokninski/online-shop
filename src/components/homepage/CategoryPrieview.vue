<template>
  <div class="bg-gray-100">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-2xl py-16 sm:py-24 lg:max-w-none lg:py-32">
        <h2 class="text-2xl font-bold text-gray-900">Kategorie</h2>

        <div class="mt-6 space-y-12 lg:grid lg:grid-cols-3 lg:gap-x-6 lg:space-y-0">
          <div v-for="callout in callouts" :key="callout.name" class="group relative">
            <img :src="callout.imageSrc" :alt="callout.imageAlt" class="w-full rounded-lg bg-white object-cover group-hover:opacity-75 max-sm:h-80 sm:aspect-[2/1] lg:aspect-square" />
            <h3 class="mt-6 text-sm text-gray-500">
              <a :href="callout.href">
                <span class="absolute inset-0" />
                {{ callout.name }}
              </a>
            </h3>
            <p class="text-base font-semibold text-gray-900">{{ callout.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import TelefonyImg from '@/assets/telefony.jpg';
import KartyImg from '@/assets/kartygraficzne.jpg';
import ProcesoryImg from '@/assets/procesory.jpeg';
const callouts = [
  {
    name: 'Telefony',
    description: 'Urządzenia mobilne',
    imageSrc: TelefonyImg,
    imageAlt: 'Prawa ręka człowieka',
    href: '/produkty/Telefony',
  },
  {
    name: 'Karty graficzne',
    description: 'Podzespoły',
    imageSrc: KartyImg,
    imageAlt: 'Dla graczy i profesjonalistów',
    href: '/produkty/Karty%20Graficzne',
  },
  {
    name: 'Procesory',
    description: 'Podzespoły',
    imageSrc: ProcesoryImg,
    imageAlt: 'Serce komputera',
    href: '/produkty/Procesory',
  },
]
</script>