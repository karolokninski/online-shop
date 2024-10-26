<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Produkty</h1>
    <div>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Zdjęcie</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Nazwa</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Kategoria</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Cena</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Status</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="product in products" :key="product.id" class="hover:bg-gray-100 transition duration-200">
            <td class="px-6 py-4">
              <img :src="product.image" alt="Product Image" class="w-12 h-12 rounded-md object-cover" />
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm font-medium text-gray-900">{{ product.name }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm  font-medium text-gray-900">{{ product.category }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">${{ product.price }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span :class="product.stock > 0 ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                {{ product.stock > 0 ? "In Stock" : "Out of Stock" }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="editProduct(product.id)" class="text-indigo-600 hover:text-indigo-900 mr-3">Edytuj</button>
              <button @click="deleteProduct(product.id)" class="text-red-600 hover:text-red-900">Usuń</button>
            </td>
          </tr>
        </tbody>
      </table>
      <button 
        class="mt-4 inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500" 
        @click="addProductOpen = true">
        Dodaj produkt
      </button>
    </div>
  </div>

  <TransitionRoot as="template" :show="addProductOpen">
    <Dialog class="relative z-10" @close="addProductOpen = false">
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
                  <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-green-100 sm:mx-0 sm:h-10 sm:w-10">
                    <PlusCircleIcon class="h-6 w-6 text-green" aria-hidden="true" />
                  </div>
                  <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                    <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Dodaj produkt</DialogTitle>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">Upewnij się, że wszystkie pola są wypełnione.</p>

                      <form method="POST" onsubmit="return false">
                        <div class="border-b border-gray-900/10 pb-8">
                          <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                            <div class="sm:col-span-3">
                              <label for="name" class="block text-sm font-medium leading-6 text-gray-900">Nazwa</label>
                              <div class="mt-2">
                                <input v-model="title" type="text" name="name" id="name" autocomplete="given-name"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>
                            <div class="sm:col-span-3">
                              <label for="price" class="block text-sm font-medium leading-6 text-gray-900">Cena</label>
                              <div class="mt-2">
                                <input v-model="price" type="text" name="price" id="price" autocomplete="given-name"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>
                            <div class="sm:col-span-3">
                              <label for="quantity" class="block text-sm font-medium leading-6 text-gray-900">Ilość w magazynie</label>
                              <div class="mt-2">
                                <input v-model="quantity" type="number" name="quantity" id="quantity"
                                  autocomplete="given-name"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>

                            <div class="sm:col-span-3">
                              <label for="country" class="block text-sm font-medium leading-6 text-gray-900">Kategoria</label>
                              <div class="mt-2">
                                <select id="category" name="category" autocomplete="category-name"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                                  <option>Obudowy</option>
                                  <option>Procesory</option>
                                  <option>Karty graficzne</option>
                                </select>
                              </div>
                            </div>

                            <div class="col-span-full">
                              <label for="about" class="block text-sm font-medium leading-6 text-gray-900">Opis produktu</label>
                              <div class="mt-2">
                                <textarea v-model="about" id="about" name="about" rows="6"
                                  class="block w-full max-h-48 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>
                            <div class="col-span-full">
                              <label for="images" class="block text-sm font-medium leading-6 text-gray-900">Dodaj zdjęcia</label>
                              <div class="mt-2">
                                <input @change="handleFileUpload" type="file" name="images" id="images" accept="image/*" multiple
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                              <div class="mt-4 grid grid-cols-3 gap-4">
                                <div v-for="image in previewImages" :key="image" class="w-full">
                                  <img :src="image" class="w-full h-auto rounded-md object-cover" alt="Preview" />
                                </div>
                              </div>
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
                  class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto"
                  @click="handleAddButton">
                  Dodaj
                </button>
                <button type="button"
                  class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                  @click="addProductOpen = false" ref="cancelButtonRef">
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
import { ref } from "vue";
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from "@headlessui/vue";
import { PlusCircleIcon } from "@heroicons/vue/24/outline";

const addProductOpen = ref(false);
const title = ref("");
const price = ref("");
const quantity = ref(0);
const category = ref("");
const about = ref("");
const products = ref([
  {
    id: 1,
    name: "Product 1",
    price: 29.99,
    stock: 15,
    image: "https://via.placeholder.com/150",
    category: "zasilacze",
  },
  {
    id: 2,
    name: "Product 2",
    price: 49.99,
    stock: 0,
    image: "https://via.placeholder.com/150",
    category: "procesory",
  },
]);

const images = ref([]);
const previewImages = ref([]);

const handleFileUpload = (event) => {
  const files = Array.from(event.target.files);
  images.value.push(...files); 
  previewImages.value.push(...files.map((file) => URL.createObjectURL(file))); 
};

const handleAddButton = () => {
  console.log("Dodaj produkt", { title: title.value, price: price.value, quantity: quantity.value, images: images.value });
  addProductOpen.value = false;
};
</script>
