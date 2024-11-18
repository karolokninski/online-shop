<template>
  <Menu as="div" class="relative inline-block text-left">
    <div>
      <MenuButton @click="handleOpenMenu" class="inline-flex w-full justify-center gap-x-1.5 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50">
        Informacje
        <ChevronUpIcon v-if="isMenuOpen" class="-mr-1 h-5 w-5 text-gray-400" aria-hidden="true" />
        <ChevronDownIcon v-else class="-mr-1 h-5 w-5 text-gray-400" aria-hidden="true" />
      </MenuButton>
    </div>

    <transition
      enter-active-class="transition ease-out duration-100"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <MenuItems class="absolute right-0 z-10 mt-2 w-auto origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
        <div class="py-1">
          <MenuItem v-for="subpage in subpages" :key="subpage.id" v-slot="{ active }">
            <router-link
              :to="subpage.path"
              :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
            >
              {{ subpage.title }}
            </router-link>
          </MenuItem>
        </div>
      </MenuItems>
    </transition>
  </Menu>
</template>

<script setup>
  import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
  import { ChevronDownIcon, ChevronUpIcon } from '@heroicons/vue/20/solid'
  import { ref, onMounted } from 'vue'
  import axios from 'axios'

  const API_URL = import.meta.env.VITE_API_URL
  const subpages = ref([])
  const isMenuOpen = ref(false)

  const handleOpenMenu = () => {
    isMenuOpen.value = !isMenuOpen.value
  }

  const fetchSubpages = async () => {
    try {
      const response = await axios.get(API_URL + '/subpages')
      subpages.value = response.data.filter((subpage) => subpage.is_active === true)
    } catch (error) {
      console.error('Error fetching subpages:', error)
    }
  }

  onMounted(fetchSubpages)
</script>
