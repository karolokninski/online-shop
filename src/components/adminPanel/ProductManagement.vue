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
            <th class="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">Opis</th>
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
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ product.caption }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="handleEditButton(product.id)" class="text-indigo-600 hover:text-indigo-900 mr-3">Edytuj</button>
              <button @click="handleDeleteButton(product.id)" class="text-red-600 hover:text-red-900">Usuń</button>
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

  <TransitionRoot as="deleteSubpage" :show="deleteProductOpen">
    <Dialog class="relative z-10" @close="deleteProductOpen = false">
      <TransitionChild as="deleteSubpage" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
        leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>
      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="deleteSubpage" enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel
              class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                <div class="sm:flex sm:items-start">
                  <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                    <svg class="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z" />
                    </svg>
                  </div>
                  <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                    <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Usuń produkt</h3>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">Czy na pewno chcesz usunąć produkt <b>{{ currentDeletename }}</b>? Ta czynność jest nieodwracalna.</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                <button @click="deleteProduct(currentDeleteId); deleteProductOpen=false" type="button" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto">Usuń</button>
                <button @click="deleteProductOpen = false" type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Anuluj</button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>



  <TransitionRoot as="editProduct" :show="editProductOpen">
    <Dialog class="relative z-10" @close="editProductOpen = false">
      <TransitionChild as="editSubpage" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
        leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="editSubpage" enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel
              class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <form @submit.prevent="submitEditProductForm">
                <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="sm:flex sm:items-start">
                    <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                      <PencilSquareIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                    </div>
                    <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                      <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Edytuj produkt</DialogTitle>
                      <div class="mt-2">
                        <p class="text-sm text-gray-500">
                          Upewnij się, że wszystkie pola są wypełnione.
                        </p>
                        <div class="border-b border-gray-900/10 pb-8">
                          <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                            <div class="sm:col-span-2">
                              <label for="edit-name" class="block text-sm font-medium leading-6 text-gray-900">Nazwa</label>
                              <div class="mt-2">
                                <input 
                                  v-model="form.edit.name" 
                                  type="text" 
                                  name="edit-name" 
                                  id="edit-name" 
                                  autocomplete="name"
                                  @blur="validatename('edit')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                />
                                <p v-if="form.edit.errors.name" class="text-red-500 text-xs mt-1">{{ form.edit.errors.name }}</p>
                              </div>
                            </div>
                            <div class="sm:col-span-4">
                              <label for="edit-path" class="block text-sm font-medium leading-6 text-gray-900">Cena</label>
                              <div class="mt-2">
                                <div class="flex">
                                    <input 
                                      v-model="form.edit.price" 
                                      type="number" 
                                      name="price" 
                                      id="edit-price"
                                      @blur="validatePath('edit')"
                                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                    />
                                  </div>
                                <p v-if="form.edit.errors.price" class="text-red-500 text-xs mt-1">{{ form.edit.errors.price }}</p>
                              </div>
                            </div>

                            <div class="sm:col-span-4">
                          <label for="edit-price" class="block text-sm font-medium leading-6 text-gray-900">Kategoria</label>
                          <div class="mt-2">
                            <div class="flex">
                              <select 
                                v-model="form.edit.category" 
                                id="edit-category" 
                                    @blur="validateCategory('edit')"
                                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                              >
                                <option value="" disabled selected>Wybierz opcję</option> <!-- Domyślna opcja -->
                                <option v-for="kategorie in kategorie" :key="kategorie.id" :value="kategorie.name">
                                  {{ kategorie.name }}
                                </option>
                              </select>
                            </div>
                            <p v-if="form.edit.errors.price" class="text-red-500 text-xs mt-1">{{ form.edit.errors.price }}</p>
                          </div>
                        </div>

                            <div class="sm:col-span-4">
                              <label for="edit-path" class="block text-sm font-medium leading-6 text-gray-900">Opis</label>
                              <div class="mt-2">
                                <div class="flex">
                                    <textarea
                                      v-model="form.edit.caption" 
                                      type="text" 
                                      name="caption" 
                                      id="edit-caption"
                                      rows="3"
                                      @blur="validateCaption('edit')"
                                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                    ></textarea>
                                  </div>
                                <p v-if="form.edit.errors.caption" class="text-red-500 text-xs mt-1">{{ form.edit.errors.caption }}</p>
                              </div>
                            </div>
                            <div class="sm:col-span-6">
                              <label for="edit-content" class="block text-sm font-medium leading-6 text-gray-900">Ilość w magazynie</label>
                              <div class="mt-2">
                                <input
                                  v-model="form.edit.stock" 
                                  type="text"
                                  name="content" 
                                  id="edit-stock" 

                                  @blur="validateContent('edit')"
                                  class="block w-full max-h-48 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                              </input>
                                <p v-if="form.edit.errors.stock" class="text-red-500 text-xs mt-1">{{ form.edit.errors.stock }}</p>
                              </div>
                            </div>
                           
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                  <button type="submit"
                    class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-700 sm:ml-3 sm:w-auto"
                    @click="submitEditProductForm">
                    Edytuj
                  </button>
                  <button type="button"
                    class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                    @click="editProductOpen = false">
                    Anuluj
                  </button>
                </div>
              </form>
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
const addProductOpen = ref(false)
const editProductOpen = ref(false)
const deleteProductOpen = ref(false)
const currentEditId = ref()
const currentDeleteId = ref()
const currentDeletename = ref()
const name = ref("");
const price = ref("");
const caption = ref("");
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
    caption: "blebleble",
  },
  {
    id: 2,
    name: "Product 2",
    price: 49.99,
    stock: 0,
    image: "https://via.placeholder.com/150",
    category: "procesory",
    caption: "blebleble",
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
  console.log("Dodaj produkt", { name: name.value, price: price.value, quantity: quantity.value, images: images.value });
  addProductOpen.value = false;
};
const handleDeleteButton = (id) => {
    currentDeleteId.value = id
    currentDeletename.value = products.value.find(p => p.id === id).name
    deleteProductOpen.value = true
  }
  const handleEditButton = (id) => {
    const product = products.value.find(p => p.id === id)
    form.value.edit.name = product.name
    form.value.edit.price = product.price
    form.value.edit.stock = product.stock
    form.value.edit.image = product.image
    form.value.edit.caption = product.caption
    form.value.edit.category = product.category
    currentEditId.value = id
    editProductOpen.value = true
  }
  const form = ref({
    add: {
      title: '',
      path: '',
      content: '',
      isActive: false,
      errors: {
        title: '',
        path: '',
        content: ''
      }
    },
    edit: {
      title: '',
      path: '',
      content: '',
      isActive: false,
      errors: {
        title: '',
        path: '',
        content: ''
      }
    }
  })
  const kategorie = ref([
  { id: 1, name: 'Procesory' },
  { id: 2, name: 'Zasilacze' },
  { id: 3, name: 'Karty graficzne' },
  { id: 4, name: 'Obudowy' },
]);
</script>
