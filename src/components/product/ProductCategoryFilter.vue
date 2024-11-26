<template>
  <div class="bg-white">
    <div>
      <TransitionRoot as="template" :show="mobileFiltersOpen">
        <Dialog class="relative z-40 lg:hidden" @close="mobileFiltersOpen = false">
          <TransitionChild as="template" enter="transition-opacity ease-linear duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="transition-opacity ease-linear duration-300" leave-from="opacity-100" leave-to="opacity-0">
            <div class="fixed inset-0 bg-black/25" />
          </TransitionChild>

          <div class="fixed inset-0 z-40 flex">
            <TransitionChild as="template" enter="transition ease-in-out duration-300 transform" enter-from="translate-x-full" enter-to="translate-x-0" leave="transition ease-in-out duration-300 transform" leave-from="translate-x-0" leave-to="translate-x-full">
              <DialogPanel class="relative ml-auto flex size-full max-w-xs flex-col overflow-y-auto bg-white py-4 pb-12 shadow-xl">
                <div class="flex items-center justify-between px-4">
                  <h2 class="text-lg font-medium text-gray-900">Filtry</h2>
                  <button type="button" class="-mr-2 flex size-10 items-center justify-center rounded-md bg-white p-2 text-gray-400" @click="mobileFiltersOpen = false">
                    <span class="sr-only">Zamknij menu</span>
                    <XMarkIcon class="size-6" aria-hidden="true" />
                  </button>
                </div>

                <form @submit.prevent="" class="mt-4 border-t border-gray-200">
                  <h3 class="sr-only">Categories</h3>
                  <ul role="list" class="px-2 py-3 font-medium text-gray-900">
                    <li v-for="category in subCategories" :key="category.id">
                      <RouterLink :to="category.href" class="block px-2 py-3">{{ category.name }}</RouterLink>
                    </li>
                  </ul>

                  <Disclosure as="div" v-for="section in filters" :key="section.id" class="border-t border-gray-200 px-4 py-6" v-slot="{ open }">
                    <h3 class="-mx-2 -my-3 flow-root">
                      <DisclosureButton class="flex w-full items-center justify-between bg-white px-2 py-3 text-gray-400 hover:text-gray-500">
                        <span class="font-medium text-gray-900">{{ section.name }}</span>
                        <span class="ml-6 flex items-center">
                          <PlusIcon v-if="!open" class="size-5" aria-hidden="true" />
                          <MinusIcon v-else class="size-5" aria-hidden="true" />
                        </span>
                      </DisclosureButton>
                    </h3>
                    <DisclosurePanel class="pt-6">
                      <div class="space-y-6">
                        <div v-if="section.type == 'scope'" class="flex items-center space-x-2 w-full text-gray-900">
                          <div class="relative flex-1">
                            <input
                              v-model="minValue"
                              type="number"
                              placeholder="od"
                              class="w-full border rounded-lg px-3 pr-7 py-2 text-sm focus:outline-none focus:ring-2"
                              :class="minClass"
                            />
                            <span class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 text-sm">
                              zł
                            </span>
                          </div>
                          <span class="text-gray-500 text-sm">-</span>
                          <div class="relative flex-1">
                            <input
                              v-model="maxValue"
                              type="number"
                              placeholder="do"
                              class="w-full border rounded-lg px-3 pr-7 py-2 text-sm focus:outline-none focus:ring-2"
                              :class="maxClass"
                            />
                            <span class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 text-sm">
                              zł
                            </span>
                          </div>
                        </div>
                        <div v-else v-for="(option, optionIdx) in section.options" :key="option.value" class="flex items-center">
                          <input :id="`filter-mobile-${section.id}-${optionIdx}`" :name="`${section.id}[]`" :value="option.value" type="checkbox" :checked="option.checked" class="size-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                          <label :for="`filter-mobile-${section.id}-${optionIdx}`" class="ml-3 min-w-0 flex-1 text-gray-500">{{ option.label }}</label>
                        </div>
                      </div>
                    </DisclosurePanel>
                  </Disclosure>
                  <button @click="sortProducts" class="flex mx-auto bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-1.5 px-6 mt-2 rounded">Filtruj</button>
                </form>
              </DialogPanel>
            </TransitionChild>
          </div>
        </Dialog>
      </TransitionRoot>

      <main class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="flex items-baseline justify-between border-b border-gray-200 pb-6">
          <h1 v-if="currentCategory" class="text-3xl font-bold tracking-tight text-gray-900">{{ currentCategory }}</h1>
          <h1 v-else class="text-3xl font-bold tracking-tight text-gray-900">Produkty</h1>

          <div class="flex items-center">
            <Menu as="div" class="relative inline-block text-left">
              <div>
                <MenuButton class="group inline-flex justify-center text-sm font-medium text-gray-700 hover:text-gray-900">
                  Sortowanie
                  <ChevronDownIcon class="-mr-1 ml-1 size-5 shrink-0 text-gray-400 group-hover:text-gray-500" aria-hidden="true" />
                </MenuButton>
              </div>

              <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
                <MenuItems class="absolute right-0 z-10 mt-2 w-40 origin-top-right rounded-md bg-white shadow-2xl ring-1 ring-black/5 focus:outline-none">
                  <div class="py-1">
                    <MenuItem v-for="option in sortOptions" :key="option.id" v-slot="{ active }">
                      <a @click="handleSort(option.id)" :href="option.href" :class="[option.current ? 'font-medium text-gray-900' : 'text-gray-500', active ? 'bg-gray-100 outline-none' : '', 'block px-4 py-2 text-sm']">{{ option.name }}</a>
                    </MenuItem>
                  </div>
                </MenuItems>
              </transition>
            </Menu>

            <button type="button" class="-m-2 ml-4 p-2 text-gray-400 hover:text-gray-500 sm:ml-6 lg:hidden" @click="mobileFiltersOpen = true">
              <span class="sr-only">Filters</span>
              <FunnelIcon class="size-5" aria-hidden="true" />
            </button>
          </div>
        </div>

        <section aria-labelledby="products-heading" class="pb-24 pt-6">
          <h2 id="products-heading" class="sr-only">Products</h2>

          <div class="grid grid-cols-1 gap-x-8 gap-y-10 lg:grid-cols-4">
            <form @submit.prevent="" class="hidden lg:block">
              <h3 class="sr-only">Categories</h3>
              <ul role="list" class="space-y-4 border-b border-gray-200 pb-6 text-sm font-medium text-gray-900">
                <li v-for="category in subCategories" :key="category.id">
                  <RouterLink :to="category.href">{{ category.name }}</RouterLink>
                </li>
              </ul>

              <Disclosure as="div" v-for="section in filters" :key="section.id" class="border-b border-gray-200 py-6" v-slot="{ open }">
                <h3 class="-my-3 flow-root">
                  <DisclosureButton class="flex w-full items-center justify-between bg-white py-3 text-sm text-gray-400 hover:text-gray-500">
                    <span class="font-medium text-gray-900">{{ section.name }}</span>
                    <span class="ml-6 flex items-center">
                      <PlusIcon v-if="!open" class="size-5" aria-hidden="true" />
                      <MinusIcon v-else class="size-5" aria-hidden="true" />
                    </span>
                  </DisclosureButton>
                </h3>
                <DisclosurePanel class="pt-6">
                  <div class="space-y-4">
                    <div v-if="section.type == 'scope'" class="flex items-center space-x-2 w-full text-gray-900">
                      <div class="relative flex-1">
                        <input
                          v-model="minValue"
                          type="number"
                          placeholder="od"
                          class="w-full border rounded-lg px-3 pr-7 py-2 text-sm focus:outline-none focus:ring-2"
                          :class="minClass"
                        />
                        <span class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 text-sm">
                          zł
                        </span>
                      </div>
                      <span class="text-gray-500 text-sm">-</span>
                      <div class="relative flex-1">
                        <input
                          v-model="maxValue"
                          type="number"
                          placeholder="do"
                          class="w-full border rounded-lg px-3 pr-7 py-2 text-sm focus:outline-none focus:ring-2"
                          :class="maxClass"
                        />
                        <span class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 text-sm">
                          zł
                        </span>
                      </div>
                    </div>
                    <div v-else v-for="(option, optionIdx) in section.options" :key="option.value" class="flex items-center">
                      <input :id="`filter-${section.id}-${optionIdx}`" :name="`${section.id}[]`" :value="option.value" type="checkbox" :checked="option.checked" class="size-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500" />
                      <label :for="`filter-${section.id}-${optionIdx}`" class="ml-3 text-sm text-gray-600">{{ option.label }}</label>
                    </div>
                  </div>
                </DisclosurePanel>
              </Disclosure>
              <button @click="sortProducts" class="flex mr-auto bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-1.5 px-6 mt-4 rounded">Filtruj</button>
            </form>

            <div class="lg:col-span-3">
              <ProductList></ProductList>
            </div>
          </div>
        </section>
      </main>
    </div>
  </div>
</template>

<script setup>
import ProductList from '@/components/product/ProductList.vue';
import { ref, watch, computed } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { useProductsStore } from '@/stores/products';
import {
  Dialog,
  DialogPanel,
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
  TransitionChild,
  TransitionRoot,
} from '@headlessui/vue';
import { XMarkIcon } from '@heroicons/vue/24/outline';
import { ChevronDownIcon, FunnelIcon, MinusIcon, PlusIcon } from '@heroicons/vue/20/solid';

const API_URL = import.meta.env.VITE_API_URL;
const productsStore = useProductsStore();
const router = useRoute();

const rawMinValue = ref(null);
const rawMaxValue = ref(null);
const minValue = computed({
  get() {
    if (rawMinValue.value > 10000000) {
      return 10000000
    }
    return rawMinValue.value < 0 ? 0 : rawMinValue.value;
  },
  set(value) {
    rawMinValue.value = value;
  }
});
const maxValue = computed({
  get() {
    if (rawMaxValue.value > 10000000) {
      return 10000000
    }
    return rawMaxValue.value < 0 ? 0 : rawMaxValue.value;
  },
  set(value) {
    rawMaxValue.value = value;
  }
});
const minClass = computed(() => {
  if (minValue.value === null || minValue.value === '') return 'border-gray-300 focus:border-indigo-500';
  if (minValue.value < 0 || (maxValue.value !== null && minValue.value > maxValue.value)) {
    return 'border-2 border-red-500 focus:border-red-500 focus:ring-1 focus:ring-red-500';
  }
  return 'border-gray-300 focus:border-indigo-500';
});
const maxClass = computed(() => {
  if (maxValue.value === null || maxValue.value === '') return 'border-gray-300 focus:border-indigo-500';
  if (maxValue.value < 0 || (minValue.value !== null && maxValue.value < minValue.value)) {
    return 'border-2 border-red-500 focus:border-red-500 focus:ring-1 focus:ring-red-500';
  }
  return 'border-gray-300 focus:border-indigo-500';
});

const currentCategory = ref();
const sortOptions = [
  { id: 'relevance', name: 'Od najtrafniejszych', href: '#', current: false },
  { id: 'newest', name: 'Czas: od najnowszych', href: '#', current: false },
  { id: 'oldest', name: 'Czas: od najstarszych', href: '#', current: false },
  { id: 'price_low_to_high', name: 'Cena: od najtańszych', href: '#', current: false },
  { id: 'price_high_to_low', name: 'Cena: od najdroższych', href: '#', current: false },
];
const subCategories = ref();
const filters = [
  {
    id: 'price',
    name: 'Cena',
    type: 'scope'
  }
]

const mobileFiltersOpen = ref(false)

const sortOption = ref('relevance');
const handleSort = (sortOptionId) => {
  sortOption.value = sortOptionId
  sortProducts()
}
const sortProducts = () => {
  if (minValue.value < maxValue.value) {
    productsStore.products = productsStore.products.filter(product => product.price >= minValue.value && product.price <= maxValue.value)
  }

  switch (sortOption.value) {
    case 'relevance':
      productsStore.products.sort((a, b) => a.id - b.id);
      break;

    case 'newest':
      productsStore.products.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
      break;

    case 'oldest':
      productsStore.products.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
      break;

    case 'price_low_to_high':
      productsStore.products.sort((a, b) => a.price - b.price);
      break;

    case 'price_high_to_low':
      productsStore.products.sort((a, b) => b.price - a.price);
      break;

    default:
      console.warn('Unsupported sort option:', sortOption.value);
      break;
  }
}

const fetchCategories = async () => {
  try {
    const response = await axios.get(`${API_URL}/categories`);
    subCategories.value = response.data.map(category => ({
      ...category,
      name: category.category_name,
      href: "/produkty/" + category.category_name,
    }));
    subCategories.value = subCategories.value.filter(cat => cat.name !== currentCategory.value);
  } catch (error) {
    console.error('Błąd podczas pobierania kategorii:', error);
  }
};

watch(
  () => router.params.category, (newCategory) => {
    currentCategory.value = newCategory;
    fetchCategories();
  },
  { immediate: true }
);
</script>

<style scoped>
input[type="number"] {
  -moz-appearance: textfield;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>