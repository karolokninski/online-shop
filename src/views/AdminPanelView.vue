<template>
  <div class="bg-white flex min-h-full flex-1 flex-col mt-2">
    <header class="absolute inset-x-0 top-0 px-2 pt-5">
      <nav class="flex flex-col" aria-label="Global">
        <div class="flex flex-row items-center justify-between py-2 px-6 lg:px-8">
          <div class="flex lg:flex-1">
            <ShopLogo></ShopLogo>
          </div>
        </div>
      </nav>
    </header>
    <main class="flex flex-row mt-16 divide-x">
      <div v-show="$route.name==='adminPanel' || width > 480" class="flex-none p-4">
        <div class="flex flex-col p-4 text-left">
          <span class="text-xs font-light leading-none text-black">Cześć,</span>
          <span class="text-lg font-semibold leading-none text-black">{{ userStore.name }}</span>
        </div>
        <div v-for="item in menuItems" :key="item.name" class="group relative flex gap-x-6 rounded-lg p-4 hover:bg-gray-50">
          <RouterLink :to="item.href" class="flex">
            <div class="mt-1 flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
              <component :is="item.icon" class="h-6 w-6 text-gray-600 group-hover:text-indigo-600" aria-hidden="true" />
            </div>
            <div class="flex font-semibold text-gray-900 my-auto px-2">
                {{ item.name }}
            </div>
          </RouterLink>
        </div>
      </div>
      <div v-show="$route.name!=='adminPanel' || width > 480" class="flex p-4">
        <RouterLink to="/admin" v-show="$route.name!=='adminPanel'">
          <button class="hidden max-sm:flex text-black bg-gray-300 rounded-lg px-4 py-2 mb-4">
            <component :is="ChevronLeftIcon" class="h-5 w-5 my-auto mr-1" aria-hidden="true" />
            Wróć
          </button>
        </RouterLink>
        <RouterView class="flex-1"></RouterView>
        <div v-show="$route.name==='adminPanel'" class="text-black flex flex-col gap-8" style="width: 80%;">
          <h2 class="text-4xl">Panel Administracyjny sklepu Geeked.tech</h2>
          <p class="text-lg">Panel administracyjny sklepu internetowego to kompleksowy system zarządzania wszystkimi kluczowymi elementami sklepu. Umożliwia on sprawne zarządzanie produktami, kategoriami oraz parametrami produktów – każdy produkt można łatwo przypisać do różnych kategorii oraz dodać do niego specyficzne parametry.</p>
          <p class="text-lg">Panel zawiera także funkcjonalność zarządzania klientami, pozwalając na przeglądanie i edytowanie kont klientów oraz dodawanie do nich indywidualnych notatek. Obsługuje również zarządzanie zamówieniami, umożliwiając składanie ich zarówno przez zarejestrowanych, jak i niezarejestrowanych użytkowników.</p>
          <p class="text-lg">Panel administracyjny zapewnia pełną kontrolę nad sposobami i kosztami dostawy, jak również nad metodami płatności, co pozwala dostosować sklep do preferencji klientów. Dzięki opcji tworzenia podstron informacyjnych, administrator może z łatwością edytować i aktualizować ważne treści, takie jak regulamin, informacje o firmie czy warunki dostawy, które będą widoczne w menu sklepu.</p>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
  import { useUserStore } from '@/stores/user'
import ShopLogo from '@/components/LogoButton.vue'
  export default {
    beforeRouteEnter(to, from) {
      if (!useUserStore().isAuthenticated) {
        return { name: 'signIn' }
      }

      if (useUserStore().role !== 'admin') {
        return { name: 'homepage' }
      }
    },
  }
</script>

<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import { useRoute } from 'vue-router'
  import { useWindowSize } from '@vueuse/core'
  import {
    ChevronLeftIcon,
    ArchiveBoxIcon,
    TagIcon,
    AdjustmentsHorizontalIcon,
    UserIcon,
    ClipboardDocumentCheckIcon,
    TruckIcon,
    DocumentTextIcon
  } from '@heroicons/vue/24/outline'
  import { useUserStore } from '@/stores/user'

  const { width } = useWindowSize()
  const route = useRoute()
  const userStore = useUserStore()

  const menuItems = [
    { name: 'Produkty', description: '', href: '/admin/produkty', icon: ArchiveBoxIcon },
    { name: 'Kategorie', description: '', href: '/admin/kategorie', icon: TagIcon },
    { name: 'Parametry', description: '', href: '/admin/parametry', icon: AdjustmentsHorizontalIcon },
    { name: 'Użytkownicy', description: '', href: '/admin/uzytkownicy', icon: UserIcon },
    { name: 'Zamówienia', description: '', href: '/admin/zamowienia', icon: ClipboardDocumentCheckIcon },
    { name: 'Dostawa i płatność', description: '', href: '/admin/dostawa-i-platnosc', icon: TruckIcon },
    { name: 'Podstrony', description: '', href: '/admin/podstrony', icon: DocumentTextIcon }
  ]
</script>
