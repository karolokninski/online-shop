<template>
  <Popover class="relative">
    <PopoverButton class="remove-border inline-flex items-center gap-x-1 text-sm font-semibold leading-6 text-gray-900">
      <div class="flex flex-row gap-1">
        <div class="flex flex-col text-right">
          <span class="text-xs font-light leading-none text-black">Cześć,</span>
          <span class="text-sm font-semibold leading-none text-black">{{ userStore.username }}</span>
        </div>
        <UserIcon class="h-8 w-6 pb-1" aria-hidden="true" />
      </div>
    </PopoverButton>

    <transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
      <PopoverPanel class="absolute z-10 mt-5 flex w-screen max-w-max -translate-x-3/4 px-4">
        <div class="w-screen max-w-md flex-auto overflow-hidden rounded-3xl bg-white text-sm leading-6 shadow-lg ring-1 ring-gray-900/5">
          <div class="p-4">
            <div v-for="item in menuItems" :key="item.name" class="group relative flex gap-x-6 rounded-lg p-4 hover:bg-gray-50">
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
      </PopoverPanel>
    </transition>
  </Popover>
</template>

<script setup>
  import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
  import {
    UserIcon,
    ClipboardDocumentCheckIcon,
    HeartIcon,
    ArrowLeftStartOnRectangleIcon
  } from '@heroicons/vue/24/outline'
  import { useUserStore } from '@/stores/user'

  const userStore = useUserStore()

  const menuItems = [
    { name: 'Twoje konto', description: 'Ustawienia Twojego konta', href: '/konto/ustawienia', icon: UserIcon },
    { name: 'Zamówienia', description: 'Zrealizowane zamówienia', href: '/konto/zamowienia', icon: ClipboardDocumentCheckIcon },
    { name: 'Ulubione', description: "Ulubione produkty", href: '/konto/ulubione', icon: HeartIcon },
  ]
</script>

<style setup>
  .remove-border {
    outline:none; 
    border:0px;
    -webkit-box-shadow: 0px;
    box-shadow: 0px;
  }
</style>