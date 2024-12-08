<template>
	<TopBar></TopBar>
  <div v-if="product">
    <nav aria-label="Breadcrumb">
      <ol role="list" class="mx-auto flex max-w-2xl items-center space-x-2 px-4 sm:px-6 lg:max-w-7xl lg:px-8">
        <li v-for="breadcrumb in product.breadcrumbs" :key="breadcrumb.id">
          <div class="flex items-center">
            <RouterLink :to="breadcrumb.href" class="mr-2 text-sm font-medium text-gray-900">{{ breadcrumb.name }}</RouterLink>
            <svg width="16" height="20" viewBox="0 0 16 20" fill="currentColor" aria-hidden="true" class="h-5 w-4 text-gray-300">
              <path d="M5.697 4.34L8.98 16.532h1.327L7.025 4.341H5.697z" />
            </svg>
          </div>
        </li>
        <li class="text-sm">
          <a :href="product.href" aria-current="page" class="font-medium text-gray-500 hover:text-gray-600">{{ product.name }}</a>
        </li>
      </ol>
    </nav>

    <div class="mx-auto mt-6 max-w-2xl sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:gap-x-8 lg:px-8">
      <div class="aspect-h-4 aspect-w-3 hidden overflow-hidden rounded-lg lg:block">
        <img :src="formatImage(product.main_image)" :alt="product.name" class="h-full w-full object-cover object-center" />
      </div>
      <div class="mx-auto mt-6 max-w-2xl sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:gap-x-8 lg:px-8">
        <div v-if="product.additional_images && product.additional_images.length > 1" class="hidden lg:grid lg:grid-cols-1 lg:gap-y-8">
          <div v-if="product.additional_images[1]" class="aspect-h-2 aspect-w-3 overflow-hidden rounded-lg">
            <img :src="product.additional_images[1].src" :alt="product.additional_images[1].alt" class="h-full w-full object-cover object-center" />
          </div>
          <div v-if="product.additional_images[2]" class="aspect-h-2 aspect-w-3 overflow-hidden rounded-lg">
            <img :src="product.additional_images[2].src" :alt="product.additional_images[2].alt" class="h-full w-full object-cover object-center" />
          </div>
        </div>
        <div v-if="product.additional_images && product.additional_images.length > 3" class="aspect-h-5 aspect-w-4 lg:aspect-h-4 lg:aspect-w-3 sm:overflow-hidden sm:rounded-lg">
          <img :src="product.additional_images[3].src" :alt="product.additional_images[3].alt" class="h-full w-full object-cover object-center" />
        </div>
      </div>
    </div>

    <div class="mx-auto max-w-2xl px-4 pb-16 pt-10 sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:grid-rows-[auto,auto,1fr] lg:gap-x-8 lg:px-8 lg:pb-24 lg:pt-16">
      <div class="lg:col-span-2 lg:border-r lg:border-gray-200 lg:pr-8">
        <h1 class="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">{{ product.name }}</h1>
      </div>

      <div class="mt-4 lg:row-span-3 lg:mt-0">

        <p class="text-3xl tracking-tight text-gray-900">{{ product.price }} PLN</p>


      

        <button @click="addToCart" class="mt-10 flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">Dodaj do koszyka</button>
      </div>

      <div class="py-10 lg:col-span-2 lg:col-start-1 lg:border-r lg:border-gray-200 lg:pb-16 lg:pr-8 lg:pt-6">
        <div>
          <h3 class="sr-only">Description</h3>
          <div class="space-y-6">
            <p class="text-base text-gray-900">{{ product.description }}</p>
          </div>
        </div>

        <div class="mt-10">
          <h3 class="text-sm font-medium text-gray-900">Parametry</h3>
          <div class="mt-4">
            <ul role="list" class="list-disc space-y-2 pl-4 text-sm">
              <li v-for="(parameter, index) in parameters" :key="index" class="text-gray-600">
        <strong>{{ parameter.name }}:</strong> {{ parameter.value }}
          </li>
            </ul>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>
  
<script setup>
  import TopBar from '@/components/TopBar.vue';
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router';
  import { RadioGroup, RadioGroupOption } from '@headlessui/vue'
  import { useShoppingCartStore } from '@/stores/shoppingCart'
  import { useProductsStore } from '@/stores/products'
  import axios from 'axios';

  const API_URL = import.meta.env.VITE_API_URL;
  const shoppingCartStore = useShoppingCartStore()
  const productsStore = useProductsStore()
  const router = useRoute()
  
  const id = ref()
  const product = ref()
  const category = ref()
  const parameters=ref();

  const addToCart = () => {
    shoppingCartStore.addProduct(id.value)
    shoppingCartStore.open = true
  }

  const formatImage = (image) => {
		return `data:image/jpeg;base64,${image}`
	}

  const additionalData = {
    href: '#',
    breadcrumbs: [
      { id: 1, name: 'Produkty', href: '/produkty' },
    ],
    
  };
  const fetchParameters = async (id) => {
    try {
      const response = await axios.get(`${API_URL}/product-parameters/${id}`);
      const parameterDetails = await Promise.all(
        response.data.map(async (param) => {
          const paramResponse = await axios.get(`${API_URL}/parameters/${param.parameter_id}`);
          return {
            name: paramResponse.data.parameter_name,
            value: param.value,
          };
        })
      );
      parameters.value = parameterDetails;
    } catch (error) {
      console.error('Błąd podczas pobierania parametrów:', error);
    }
  };
  const fetchCategory = async (id) => {
    try {
      const response = await axios.get(`${API_URL}/categories/${id}`);
      category.value = response.data;
    } catch (error) {
      console.error('Błąd podczas pobierania kategorii:', error);
    }
  };

  onMounted(async () => {
    id.value = router.params.id;
    if (productsStore.products.find(p => p.id == id.value)) {
      product.value = productsStore.products.find(p => p.id == id.value);
    }
    else {
      await productsStore.fetchProducts(undefined, undefined, undefined, id.value);
      product.value = productsStore.products.find(p => p.id == id.value);
    }
    product.value = {
      ...product.value,
      ...additionalData,
    };
    await fetchParameters(id.value);
    await fetchCategory(product.value.category_id);
    product.value.breadcrumbs.push({id: 2, name: category.value.category_name, href: '/produkty/' + category.value.category_name });
  })
</script>