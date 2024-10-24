<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Podstrony</h1>
    <div>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Tytuł</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Ścieżka</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Aktywna</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="product in products" :key="product.id" class="hover:bg-gray-100 transition duration-200">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ product.title }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ product.path }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span :class="product.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                {{ product.is_active ? 'Tak' : 'Nie' }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="handleEditButton(product.id)" class="text-indigo-600 hover:text-indigo-900 mr-3">
                Edytuj
              </button>
              <button @click="deleteProduct(product.id)" class="text-red-600 hover:text-red-900">
                Usuń
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <button @click="addSubpageOpen = true" class="mt-4 inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        Dodaj podstronę
      </button>
    </div>
  </div>

  <TransitionRoot as="template" :show="addSubpageOpen">
    <Dialog class="relative z-10" @close="addSubpageOpen = false">
      <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
        leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="template" enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel
              class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                <div class="sm:flex sm:items-start">
                  <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                    <PlusCircleIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                  </div>
                  <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                    <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Dodaj podstronę</DialogTitle>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">
                        Upewnij się, że wszystkie pola są wypełnione.
                      </p>

                      <form method="POST" onsubmit="return false">
                        <div class="border-b border-gray-900/10 pb-8">
                          <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                            <div class="sm:col-span-3">
                              <label for="title" class="block text-sm font-medium leading-6 text-gray-900">Tytuł</label>
                              <div class="mt-2">
                                <input v-model="title" type="text" name="title" id="title"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>

                            <div class="sm:col-span-3">
                              <label for="path" class="block text-sm font-medium leading-6 text-gray-900">Ścieżka</label>
                              <div class="mt-2">
                                <input v-model="path" type="text" name="path" id="path"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>

                            <div class="sm:col-span-6">
                              <label for="content" class="block text-sm font-medium leading-6 text-gray-900">Treść</label>
                              <div class="mt-2">
                                <textarea v-model="content" name="content" id="content" rows="3"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"></textarea>
                              </div>
                            </div>

                            <div class="sm:col-span-6">
                              <label for="is_active" class="flex items-center">
                                <input v-model="is_active" type="checkbox" id="is_active" class="mr-2" />
                                Aktywna
                              </label>
                            </div>
                          </div>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
              <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                <button type="button"
                  class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-700 sm:ml-3 sm:w-auto"
                  @click="handleAddButton">
                  Dodaj
                </button>
                <button type="button"
                  class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                  @click="addSubpageOpen = false" ref="cancelButtonRef">
                  Anuluj
                </button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue';
import { PlusCircleIcon } from '@heroicons/vue/24/outline';

const API_URL = import.meta.env.VITE_API_URL;
const addSubpageOpen = ref(false);
const products = ref([]);

const title = ref('');
const path = ref('');
const content = ref('');
const is_active = ref(false);

const handleAddButton = async () => {
  try {
    const newProduct = {
      title: title.value,
      content: content.value,
      path: path.value,
      is_active: is_active.value,
    };
    const response = await axios.post(`${API_URL}/subpages`, newProduct);
    products.value.push(response.data);
    addSubpageOpen.value = false;
    console.log('Dodano podstronę:', response.data);
  } catch (error) {
    console.error('Błąd podczas dodawania podstrony:', error);
  }
};

const deleteProduct = async (id) => {
  try {
    await axios.delete(`${API_URL}/subpages/${id}`);
    products.value = products.value.filter(product => product.id !== id);
    console.log('Usunięto podstronę o id:', id);
  } catch (error) {
    console.error('Błąd podczas usuwania podstrony:', error);
  }
};

const handleEditButton = (id) => {
  console.log('Edytuj podstronę o id:', id);
};

// Fetch subpages when component mounts
onMounted(async () => {
  try {
    const response = await axios.get(`${API_URL}/subpages`);
    products.value = response.data;
  } catch (error) {
    console.error('Błąd podczas pobierania podstron:', error);
  }
});
</script>

<style scoped>
/* Optional: add any additional styles here */
</style>
