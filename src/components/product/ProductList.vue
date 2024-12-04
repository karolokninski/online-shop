<template>
  <div class="pb-6">
    <div v-if="productsStore.loading" class="">
      <div class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:gap-x-8">
        <div v-for="n in 8" :key="n" class="animate-pulse group relative">
          <ProductListItemSkeleton></ProductListItemSkeleton>
        </div>
      </div>
    </div>

    <div v-else-if="productsStore.products.length" class="">
      <div class="grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:gap-x-8">
        <div v-for="product in paginatedProducts" :key="product.id" class="group relative">
          <ProductListItem
            :product="{
              id: product.id,
              name: product.name,
              price: product.price,
              description: product.description,
              mainImage: product.main_image,
              imageAlt: product.name
            }"
          />
        </div>
      </div>
    </div>

    <h2 v-else class="py-12 text-lg text-black text-center">Brak wyników</h2>
  </div>
  <div class="flex items-center justify-between border-t border-gray-200 bg-white py-3">
    <div class="flex flex-1 justify-between sm:hidden">
      <a
        @click.prevent="goToPage(currentPage - 1)"
        :class="[
          'relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50',
          { 'cursor-not-allowed opacity-0': currentPage === 1 }
        ]"
        :aria-disabled="currentPage === 1"
      >
        Poprzednia
      </a>
      <a
        @click.prevent="goToPage(currentPage + 1)"
        :class="[
          'relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50',
          { 'cursor-not-allowed opacity-0': (currentPage === totalPages) || !totalPages }
        ]"
        :aria-disabled="(currentPage === totalPages) || !totalPages"
      >
        Następna
      </a>
    </div>
    <div class="hidden sm:flex sm:flex-1 sm:items-center sm:justify-between">
      <div>
        <p class="text-sm text-gray-700">
          Produkty od
          {{ ' ' }}
          <span class="font-medium">{{ pageRecordRangeStart }}</span>
          {{ ' ' }}
          do
          {{ ' ' }}
          <span class="font-medium">{{ pageRecordNumEnd }}</span>
          {{ ' ' }}
          z
          {{ ' ' }}
          <span class="font-medium">{{ productsStore.products.length }}</span>
          {{ ' ' }}
          wyników
        </p>
      </div>
      <div>
        <nav class="isolate inline-flex -space-x-px rounded-md shadow-sm" aria-label="Pagination">
          <a
            @click.prevent="goToPage(currentPage - 1)"
            :class="[
              'relative inline-flex items-center rounded-l-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0',
              { 'cursor-not-allowed opacity-50': currentPage === 1 }
            ]"
            :aria-disabled="currentPage === 1"
          >
            <span class="sr-only">Poprzednia strona</span>
            <ChevronLeftIcon class="size-5" aria-hidden="true" />
          </a>

          <a
            v-for="(page, index) in paginatedPages"
            :key="index"
            @click.prevent="goToPage(page)"
            :class="[
              'w-10 h-10 relative inline-flex items-center text-sm font-semibold ring-1 ring-inset ring-gray-300 focus:z-20 focus:outline-offset-0',
              { 'bg-indigo-600 text-white z-10': page === currentPage, 'text-gray-900 hover:bg-gray-50': page !== currentPage }
            ]"
          >
            <template v-if="page === '...'">
              <input
                v-if="isInputVisible"
                @input="inputPageNumber = $event.target.value"  
                @keydown.enter.prevent="handlePageNumberInput"
                type="number"
                min="1"
                :max="totalPages"
                placeholder="..."
                class="inputPageNum w-10 h-10 text-center"
                @blur="handleInputBlur"
                autofocus
              />
              <span v-else @click="toggleInput"><span class="px-4 py-2">{{ page }}</span></span>
            </template>
            <template v-else><span class="mx-auto">{{ page }}</span></template>
          </a>

          <a
            @click.prevent="goToPage(currentPage + 1)"
            :class="[
              'relative inline-flex items-center rounded-r-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0',
              { 'cursor-not-allowed opacity-50': (currentPage === totalPages) || !totalPages }
            ]"
            :aria-disabled="(currentPage === totalPages) || !totalPages"
          >
            <span class="sr-only">Następna strona</span>
            <ChevronRightIcon class="size-5" aria-hidden="true" />
          </a>
        </nav>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from "vue";
import ProductListItem from '@/components/product/ProductListItem.vue';
import ProductListItemSkeleton from '@/components/product/ProductListItemSkeleton.vue';
import { useRoute } from 'vue-router';
import { useProductsStore } from '@/stores/products';
import { useFavoriteProductsStore } from '@/stores/favoriteProducts';
import { ChevronLeftIcon, ChevronRightIcon } from '@heroicons/vue/20/solid';

const productsStore = useProductsStore();
const favoriteProductsStore = useFavoriteProductsStore();
const router = useRoute();
const query = computed(() => router.query.q);

const productsPerPage = 12;
const currentPage = ref(1);

watch(query, (query) => {
  productsStore.fetchProducts(0, productsPerPage, query, undefined);
}, { immediate: true });

const totalPages = computed(() => Math.ceil(productsStore.products.length / productsPerPage));

const paginatedProducts = computed({
  get () {
    console.log(productsStore.products, productsStore.products.slice(pageRecordNumStart.value, pageRecordNumEnd.value))
    return productsStore.products.slice(pageRecordNumStart.value, pageRecordNumEnd.value);
  }
});

const pageRecordNumStart = computed({
  get() {
    return (currentPage.value - 1) * productsPerPage;
  }
});

const pageRecordNumEnd = computed({
  get() {
    if (pageRecordNumStart.value + productsPerPage > productsStore.products.length) {
      return productsStore.products.length;
    }

    return pageRecordNumStart.value + productsPerPage;
  }
});

const pageRecordRangeStart = computed({
  get() {
    return (paginatedPages.value.length > 0) ? pageRecordNumStart.value + 1 : 0;
  }
});

const goToPage = (page) => {
  if (page > 0 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

const isInputVisible = ref(false);
const inputPageNumber = ref('');

const toggleInput = () => {
  isInputVisible.value = !isInputVisible.value;
  if (isInputVisible.value) {
    inputPageNumber.value = '';
  }
};

const handlePageNumberInput = () => {
  const page = parseInt(inputPageNumber.value, 10);
  if (page >= 1 && page <= totalPages.value) {
    goToPage(page);
    isInputVisible.value = false;
  }
};

const handleInputBlur = () => {
  if (!inputPageNumber.value || inputPageNumber.value < 1 || inputPageNumber.value > totalPages.value) {
    isInputVisible.value = false;
  }
};

const paginatedPages = computed(() => {
  const total = totalPages.value;
  const pages = [];

  if (total <= 5) {
    for (let i = 1; i <= total; i++) {
      pages.push(i);
    }
  } else {
    pages.push(1);

    if (currentPage.value > 3) pages.push('...');
    if (currentPage.value > 2) pages.push(currentPage.value - 1);
    if (currentPage.value != 1 && currentPage.value != total) pages.push(currentPage.value);
    if (currentPage.value < total - 1) pages.push(currentPage.value + 1);
    if (currentPage.value < total - 2) pages.push('...');
    pages.push(total);
  }

  return pages;
});

onMounted(async () => {
  favoriteProductsStore.fetchProducts();
});
</script>

<style scoped>
.inputPageNum {
  padding: 0 8px !important;
}

.inputPageNum,
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.inputPageNum,
input[type="number"] {
  -moz-appearance: textfield;
}

.inputPageNum,
input[type="number"] {
  padding-right: 0;
}
</style>
