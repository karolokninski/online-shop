<template>
  <header class="bg-white inset-x-0 sticky top-0 z-40" style="margin-bottom: 1rem;">
    <nav class="flex flex-col" aria-label="Global">
      <div class="flex flex-row items-center gap-4 md:gap-16 lg:gap-12 xl:gap-32 py-2 px-6 lg:px-8">
        <div class="flex h-12">
          <ShopLogo></ShopLogo>
        </div>
        <div class="hidden lg:flex text md:gap-x-2 lg:gap-x-6 xl:gap-x-12">
          <RouterLink v-for="item in navigation" :key="item.name" :to="item.href" class="my-auto text-sm font-semibold leading-6 text-black">{{ item.name }}</RouterLink>
          <SubpageMenu class="text-sm font-semibold leading-none text-black"></SubpageMenu>
        </div>
        <div class="flex-1">
          <SearchBar class="hidden sm:flex"></SearchBar>
        </div>
        <div class="hidden lg:flex lg:justify-end gap-2">
          <RouterLink to="/logowanie" v-if="!userStore.isAuthenticated" class="text-sm font-semibold leading-6 text-black flex flex-row">
            <UserIcon class="h-8 w-6" aria-hidden="true" />
          </RouterLink>
          <UserMenu v-else class="text-sm font-semibold leading-none text-black"></UserMenu>
          <ShoppingCartIcon @click="shoppingCartStore.open = true" class="font-semibold my-auto text-black w-6 h-6" />
        </div>
        <div class="flex lg:hidden gap-3">
          <ShoppingCartIcon @click="shoppingCartStore.open = true" class="font-semibold leading-6 text-black w-6 h-6" />
          <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-black" @click="mobileMenuOpen = true">
            <span class="sr-only">Otwórz koszyk</span>
            <Bars3Icon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
      </div>
      <SearchBar class="sm:hidden"></SearchBar>
    </nav>
    <Dialog class="lg:hidden" @close="mobileMenuOpen = false" :open="mobileMenuOpen">
      <DialogPanel class="fixed inset-y-0 right-0 z-40 w-full overflow-y-auto bg-white px-6 py-4 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
        <div class="flex items-center justify-between">
          <div class="flex lg:flex-1 h-12">
            <ShopLogo></ShopLogo>
          </div>
          <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-700" @click="mobileMenuOpen = false">
            <span class="sr-only">Zamknij menu</span>
            <XMarkIcon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="flex-1 mt-6 h-auto">
          <div class="flex-1 -my-6 h-auto divide-y-2 divide-gray-500">
            <div class="py-3">
              <a v-for="item in navigation" :key="item.name" :href="item.href" class="-mx-3 block rounded-lg px-3 py-1 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">{{ item.name }}</a>
            </div>
            <div v-if="!userStore.isAuthenticated" class="py-6">
              <RouterLink to="/logowanie" class="text-sm font-semibold leading-6 text-gray-900">Zaloguj się</RouterLink>
            </div>
            <div v-else class="flex-auto text-sm leading-6">
              <div class="flex flex-row py-4 gap-1">
                <div class="flex flex-col text-left">
                  <span class=" font-light leading-none text-black">Cześć,</span>
                  <span class="text-xl font-semibold leading-none text-black">{{ userStore.name }}</span>
                </div>
              </div>
              <div class="py-2">
                <div v-for="item in menuItems" :key="item.name" class="group relative flex gap-x-6 rounded-lg py-2 hover:bg-gray-50">
                  <div class="mt-1 flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
                    <component :is="item.icon" class="h-6 w-6 text-gray-600 group-hover:text-indigo-600" aria-hidden="true" />
                  </div>
                  <div>
                    <RouterLink :to="item.href" class="font-semibold text-gray-900">
                      {{ item.name }}
                      <span class="absolute inset-0" />
                    </RouterLink>
                    <p class="mt-1 text-gray-600">{{ item.description }}</p>
                  </div>
                </div>
              </div>
              <div class="grid grid-cols-1 divide-x divide-gray-900/5 bg-gray-50">
                <button @click="userStore.logout" class="flex items-center justify-center gap-x-2.5 p-3 font-semibold text-gray-900 hover:bg-gray-100 text-center">
                  <component :is="ArrowLeftStartOnRectangleIcon" class="h-5 w-5 flex-none text-black" aria-hidden="true" />
                  Wyloguj się
                </button>
              </div>
            </div>
          </div>
        </div>
      </DialogPanel>
    </Dialog>
  </header>
  <ShoppingCart class="fixed bottom-0 right-0 z-40"></ShoppingCart>
</template>

<script setup>
  import { ref } from 'vue'
  import { useShoppingCartStore } from '@/stores/shoppingCart'
  import { useUserStore } from '@/stores/user'
  import { Dialog, DialogPanel } from '@headlessui/vue'
  import { Bars3Icon, XMarkIcon, ShoppingCartIcon, UserIcon, ClipboardDocumentCheckIcon, HeartIcon, ArrowLeftStartOnRectangleIcon } from '@heroicons/vue/24/outline'
  import ShoppingCart from './ShoppingCart.vue'
  import UserMenu from './topBar/UserMenu.vue'
  import SubpageMenu from './topBar/SubpageMenu.vue'
  import SearchBar from './topBar/SearchBar.vue'
import ShopLogo from './LogoButton.vue'
  
  const shoppingCartStore = useShoppingCartStore()
  const userStore = useUserStore()
  const navigation = [
    { name: 'Produkty', href: '/produkty' },
    { name: 'Nasze sklepy', href: '/sklepy' },
  ]
  const menuItems = [
    { name: 'Twoje konto', description: 'Ustawienia Twojego konta', href: '/konto/ustawienia', icon: UserIcon },
    { name: 'Zamówienia', description: 'Zrealizowane zamówienia', href: '/konto/zamowienia', icon: ClipboardDocumentCheckIcon },
    { name: 'Ulubione', description: "Ulubione produkty", href: '/konto/ulubione', icon: HeartIcon },
  ]

  if (userStore.role === 'admin') {
    menuItems.push({
      name: 'Admin panel', description: "Panel administracyjny", href: '/admin', icon: UserIcon
    })
  }

  const mobileMenuOpen = ref(false)
</script>
