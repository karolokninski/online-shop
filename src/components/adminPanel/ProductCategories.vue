<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Kategorie</h1>
    <div>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">ID Kategorii</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Nazwa Kategorii</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="category in categories" :key="category.id" class="hover:bg-gray-100 transition duration-200">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ category.id }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm font-medium text-gray-900">{{ category.name }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="openEditModal(category)" class="text-indigo-600 hover:text-indigo-900 mr-3">Edytuj</button>
              <button @click="handleDeleteButton(category.id)" class="text-red-600 hover:text-red-900">Usuń</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="mt-4">
        <div class="flex space-x-2">
          <input v-model="newCategoryName" type="text" placeholder="Wpisz nazwę kategorii"
            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            
            <button 
            @click="addCategory" 
            class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Dodaj Kategorię
          </button>
          
        </div>
        <p v-if="categorynameerror2" class="text-red-500 text-xs mt-1">{{ categorynameerror2 }}</p>
      </div>
    </div>

    <TransitionRoot as="editCategory" :show="editCategoryOpen">
      <Dialog class="relative z-10" @close="editCategoryOpen = false">
        <TransitionChild as="editCategory" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
          leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="editCategory" enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel
                class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="sm:flex sm:items-start">
                    <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-green-100 sm:mx-0 sm:h-10 sm:w-10">
                      <PlusCircleIcon class="h-6 w-6 text-green" aria-hidden="true" />
                    </div>
                    <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                      <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Edytuj kategorię</DialogTitle>
                      <div class="mt-2">
                        <input v-model="currentEditName" type="text" placeholder="Wpisz nową nazwę kategorii"
                          class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                          <p v-if="categorynameerror" class="text-red-500 text-xs mt-1">{{ categorynameerror }}</p>
                        </div>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                  <button @click="updateCategory" type="button"
                    class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto">
                    Zapisz
                  </button>
                  <button type="button"
                    class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                    @click="editCategoryOpen = false">
                    Anuluj
                  </button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <TransitionRoot as="deleteCategory" :show="deleteCategoryOpen">
      <Dialog class="relative z-10" @close="deleteCategoryOpen = false">
        <TransitionChild as="deleteCategory" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
          leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="deleteCategory" enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel
                class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="sm:flex sm:items-start">
                    <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                      <svg class="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" aria-hidden="true" data-slot="icon">
                        <path stroke-linecap="round" stroke-linejoin="round"
                          d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z" />
                      </svg>
                    </div>
                    <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                      <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Usuń kategorię</h3>
                      <div class="mt-2">
                        <p class="text-sm text-gray-500">Czy na pewno chcesz usunąć kategorię <b>{{ currentDeletename }}</b>? Ta czynność jest nieodwracalna.</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                  <button @click="deleteCategory" type="button"
                    class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto">Usuń</button>
                  <button @click="deleteCategoryOpen = false" type="button"
                    class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Anuluj</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from 'axios';
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from "@headlessui/vue";

const API_URL = import.meta.env.VITE_API_URL;

const editCategoryOpen = ref(false);
const deleteCategoryOpen = ref(false);
const currentEditId = ref(null);
const currentDeleteId = ref(null);
const currentDeletename = ref('');
const newCategoryName = ref('');
const currentEditName = ref('');
const categories = ref([]);

const categorynameerror = ref('');
const categorynameerror2 = ref('');

const validateCategory = () => {
  let isValid = true;
  categorynameerror.value = ''; 
  if (currentEditName.value.trim() === '') {
    categorynameerror.value = 'Nazwa jest wymagana';
    isValid = false;
  }
  return isValid;
};

const validateNewCategory = () => {
  let isValid = true;
  categorynameerror2.value = ''; 

  if (newCategoryName.value.trim() === '') {
    categorynameerror2.value = 'Nazwa kategorii jest wymagana';
    isValid = false;
  }

  return isValid;
};



const fetchCategories = async () => {
  try {
    const response = await axios.get(`${API_URL}/categories`);
    categories.value = response.data.map(category => ({
      ...category,
      name: category.category_name,
    }));
    console.log(categories.value)
  } catch (error) {
    console.error('Błąd podczas pobierania kategorii:', error);
  }
};

const addCategory = async () => {
  if (!validateNewCategory()) return;
  if (newCategoryName.value.trim() === '') return;
  try {
    await axios.post(`${API_URL}/categories`, {
      category_name: newCategoryName.value.trim(),
    });
    fetchCategories();
    newCategoryName.value = '';
  } catch (error) {
    console.error('Błąd podczas dodawania kategorii:', error);
  }
};

const openEditModal = (category) => {
  currentEditId.value = category.id;
  currentEditName.value = category.name;
  editCategoryOpen.value = true;
};

const updateCategory = async () => {
  if (!validateCategory()) return;
  if (currentEditName.value.trim() === '') return;
  try {
    await axios.put(`${API_URL}/categories/${currentEditId.value}`, {
      category_name: currentEditName.value.trim(),
    });
    fetchCategories();
    editCategoryOpen.value = false;
  } catch (error) {
    console.error('Błąd podczas edytowania kategorii:', error);
  }
};

const handleDeleteButton = (id) => {
  currentDeleteId.value = id;
  currentDeletename.value = categories.value.find(cat => cat.id === id).name;
  deleteCategoryOpen.value = true;
};

const deleteCategory = async () => {
  try {
    await axios.delete(`${API_URL}/categories/${currentDeleteId.value}`);
    categories.value = categories.value.filter(cat => cat.id !== currentDeleteId.value);
    deleteCategoryOpen.value = false;
  } catch (error) {
    console.error('Błąd podczas usuwania kategorii:', error);
  }
};

onMounted(fetchCategories);
</script>