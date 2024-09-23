<template>
  <header class="absolute bg-white inset-x-0 top-0 z-50" style="margin-bottom: 1rem;">
    <nav class="flex flex-col" aria-label="Global">
      <div class="flex flex-row items-center justify-between py-2 px-6 lg:px-8">
        <div class="flex lg:flex-1">
          <RouterLink to="/" class="-m-1.5 p-1.5">
            <span class="sr-only">Tech-Bay</span>
            <img class="h-12 w-auto" src="@/assets/logo.png" alt="" />
          </RouterLink>
        </div>
        <div class="flex lg:hidden gap-3">
          <ShoppingCartIcon @click="shoppingCartStore.open = true" class="font-semibold leading-6 text-black w-6 h-6" />
          <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-black" @click="mobileMenuOpen = true">
            <span class="sr-only">Open main menu</span>
            <Bars3Icon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="hidden lg:flex lg:gap-x-12">
          <RouterLink v-for="item in navigation" :key="item.name" :to="item.href" class="text-sm font-semibold leading-6 text-black">{{ item.name }}</RouterLink>
        </div>
        <div class="hidden lg:flex lg:flex-1 lg:justify-end gap-2">
          <RouterLink to="/logowanie" v-if="!userStore.isAuthenticated" class="text-sm font-semibold leading-6 text-black flex flex-row">
            <UserIcon class="h-8 w-6" aria-hidden="true" />
          </RouterLink>
          <UserMenu v-else class="text-sm font-semibold leading-none text-black"></UserMenu>
          <ShoppingCartIcon @click="shoppingCartStore.open = true" class="font-semibold my-auto text-black w-6 h-6" />
        </div>
      </div>
      <div class="flex flex-row items-center justify-between py-2 px-6 lg:px-8">
        <div class="relative flex items-center w-80 mx-auto h-12 bg-white">
          <input
            class="peer h-full w-full outline-none text-sm text-black pr-2"
            type="text"
            id="search"
            v-model="searchStore.query"
            @keyup.enter="handleSearch"
            placeholder="Szukaj..." /> 
          
          <div class="grid place-items-center h-full w-12 text-gray-300 border border-black">
            <button @click="handleSearch">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="black">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </nav>
    <Dialog class="lg:hidden" @close="mobileMenuOpen = false" :open="mobileMenuOpen">
      <DialogPanel class="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-black px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
        <div class="flex items-center justify-between">
          <a href="#" class="-m-1.5 p-1.5">
            <span class="sr-only">Your Company</span>
            <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="" />
          </a>
          <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-700" @click="mobileMenuOpen = false">
            <span class="sr-only">Close menu</span>
            <XMarkIcon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="mt-6 flow-root">
          <div class="-my-6 divide-y divide-gray-500/10">
            <div class="space-y-2 py-6">
              <a v-for="item in navigation" :key="item.name" :href="item.href" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">{{ item.name }}</a>
            </div>
            <div class="py-6">
              <RouterLink to="/logowanie" class="text-sm font-semibold leading-6 text-gray-900">Zaloguj się</RouterLink>
            </div>
          </div>
        </div>
      </DialogPanel>
    </Dialog>
  </header>
  <ShoppingCart class="fixed bottom-0 right-0 z-50"></ShoppingCart>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { useSearchStore } from '@/stores/search'
  import { useShoppingCartStore } from '@/stores/shoppingCart'
  import { useUserStore } from '@/stores/user'
  import { Dialog, DialogPanel } from '@headlessui/vue'
  import { Bars3Icon, XMarkIcon, ShoppingCartIcon, UserIcon } from '@heroicons/vue/24/outline'
  import ShoppingCart from './ShoppingCart.vue'
  import UserMenu from './topBar/UserMenu.vue'
  
  const searchStore = useSearchStore()
  const shoppingCartStore = useShoppingCartStore()
  const userStore = useUserStore()
  const router = useRouter()
  const navigation = [
    { name: 'Product', href: '/produkty' },
    { name: 'Features', href: '#' },
    { name: 'Marketplace', href: '#' },
    { name: 'Company', href: '#' },
  ]
  const mobileMenuOpen = ref(false)

  const handleSearch = () => {
    if (searchStore.query.trim()) {
        // searchStore.performSearch(searchStore.query);
        router.push({
          name: 'products',
          query: { q: searchStore.query }
        });
      }
  };
</script>