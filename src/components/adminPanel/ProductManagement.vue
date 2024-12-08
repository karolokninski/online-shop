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
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Opis</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="product in products" :key="product.id" class="hover:bg-gray-100 transition duration-200">
            <td class="px-6 py-4">
              <img v-if="product.main_image" :src="formatImage(product.main_image)" alt="Product Image"
                class="w-12 h-12 rounded-md object-cover" />
              <PhotoIcon v-else class="w-12 h-12 rounded-md object-cover" aria-hidden="true" />
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm font-medium text-gray-900">{{ product.name }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm font-medium text-gray-900">{{ getCategoryById(product.category_id)?.name || '' }}
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">${{ product.price }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span :class="product.stock > 0 ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'"
                class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                {{ product.stock > 0 ? "In Stock" : "Out of Stock" }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ product.description ? truncateDescription(product.description) : '' }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="handleEditButton(product.id)" class="text-indigo-600 hover:text-indigo-900 mr-3">
                <PencilSquareIcon class="h-5 w-5 inline-block" aria-hidden="true" />
              </button>
              <button @click="handleDeleteButton(product.id)" class="text-red-600 hover:text-red-900">
                <TrashIcon class="h-5 w-5 inline-block" aria-hidden="true" />
              </button>
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

  <TransitionRoot as="addProduct" :show="addProductOpen">
    <Dialog class="relative z-10" @close="addProductOpen = false">
      <TransitionChild as="addProduct" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
        leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="addProduct" enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel
              class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                <div class="sm:flex sm:items-start">
                  <div
                    class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-green-100 sm:mx-0 sm:h-10 sm:w-10">
                    <PlusCircleIcon class="h-6 w-6 text-green" aria-hidden="true" />
                  </div>
                  <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                    <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Dodaj produkt
                    </DialogTitle>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">Upewnij się, że wszystkie pola są wypełnione.</p>
                      <form @submit.prevent="">
                        <div class="border-b border-gray-900/10 pb-8">
                          <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                            <div class="sm:col-span-3">
                              <label for="name" class="block text-sm font-medium leading-6 text-gray-900">Nazwa</label>
                              <div class="mt-2">
                                <input 
                                  v-model="form.add.name" 
                                  type="text" 
                                  name="name" 
                                  id="name"
                                  autocomplete="given-name"
                                  @blur="validateName('add')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                />
                                <p v-if="form.add.errors.name" class="text-red-500 text-xs mt-1">{{ form.add.errors.name }}</p>
                              </div>
                            </div>

                            <div class="sm:col-span-3">
                              <label for="price" class="block text-sm font-medium leading-6 text-gray-900">Cena</label>
                              <div class="mt-2">
                                <input 
                                  v-model="form.add.price" 
                                  type="number" 
                                  name="price" 
                                  id="price"
                                  autocomplete="given-name"
                                  @blur="validatePrice('add')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                />
                                <p v-if="form.add.errors.price" class="text-red-500 text-xs mt-1">{{ form.add.errors.price }}</p>
                              </div>
                            </div>

                            <div class="sm:col-span-3">
                              <label for="quantity" class="block text-sm font-medium leading-6 text-gray-900">Ilość w magazynie</label>
                              <div class="mt-2">
                                <input 
                                  v-model="form.add.stock" 
                                  type="number" 
                                  name="quantity" 
                                  id="quantity"
                                  autocomplete="given-name"
                                  @blur="validateStock('add')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                />
                                <p v-if="form.add.errors.stock" class="text-red-500 text-xs mt-1">{{ form.add.errors.stock }}</p>
                              </div>
                            </div>

                            <div class="sm:col-span-3">
                              <label for="category" class="block text-sm font-medium leading-6 text-gray-900">Kategoria</label>
                              <div class="mt-2">
                                <select 
                                  v-model="form.add.category_id" 
                                  id="category" 
                                  name="category"
                                  autocomplete="category-name"
                                  @blur="validateCategory('add')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                                  <option value="" disabled>Wybierz opcję</option>
                                  <option v-for="category in categories" :key="category.id" :value="category.id">
                                    {{ category.name }}
                                  </option>
                                </select>
                                <p v-if="form.add.errors.category_id" class="text-red-500 text-xs mt-1">{{ form.add.errors.category_id }}</p>
                              </div>
                            </div>

                            <div class="col-span-full">
                              <label for="about" class="block text-sm font-medium leading-6 text-gray-900">Opis produktu</label>
                              <div class="mt-2">
                                <textarea 
                                  v-model="form.add.description" 
                                  id="about" 
                                  name="about" 
                                  rows="6"
                                  @blur="validateDescription('add')"
                                  class="block w-full max-h-48 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                </textarea>
                                <p v-if="form.add.errors.description" class="text-red-500 text-xs mt-1">{{ form.add.errors.description }}</p>
                              </div>
                            </div>

                            <div class="col-span-full">
                              <label for="images" class="block text-sm font-medium leading-6 text-gray-900">Dodaj zdjęcia</label>
                              <div class="mt-2">
                                <input 
                                  @change="handleImageUpload" 
                                  type="file" 
                                  name="images" 
                                  id="images" 
                                  accept="image/*"
                                  multiple
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                />
                                <p v-if="form.add.errors.image" class="text-red-500 text-xs mt-1">{{ form.add.errors.image }}</p>
                              </div>
                              <div class="mt-4 grid grid-cols-3 gap-4">
                                <!-- <div v-for="image in previewImages" :key="image" class="w-full">
                                  <img :src="image" class="w-full h-auto rounded-md object-cover" alt="Preview" />
                                </div> -->
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

  <TransitionRoot as="deleteProduct" :show="deleteProductOpen">
    <Dialog class="relative z-10" @close="deleteProductOpen = false">
      <TransitionChild as="deleteProduct" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
        leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>
      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="deleteProduct" enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel
              class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                <div class="sm:flex sm:items-start">
                  <div
                    class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                    <svg class="h-6 w-6 text-red-600" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                      stroke="currentColor" aria-hidden="true" data-slot="icon">
                      <path stroke-linecap="round" stroke-linejoin="round"
                        d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z" />
                    </svg>
                  </div>
                  <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                    <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Usuń produkt</h3>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">Czy na pewno chcesz usunąć produkt <b>{{ currentDeletename
                          }}</b>? Ta czynność jest nieodwracalna.</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                <button @click="deleteProduct(currentDeleteId)" type="button"
                  class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto">Usuń</button>
                <button @click="deleteProductOpen = false" type="button"
                  class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Anuluj</button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>

  <TransitionRoot as="editProduct" :show="editProductOpen">
    <Dialog class="relative z-10" @close="editProductOpen = false">
      <TransitionChild as="editProduct" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
        leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="editProduct" enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel
              class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <form @submit.prevent="">
                <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="sm:flex sm:items-start">
                    <div
                      class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                      <PencilSquareIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                    </div>
                    <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                      <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Edytuj produkt
                      </DialogTitle>
                      <div class="mt-2">
                        <p class="text-sm text-gray-500">
                          Upewnij się, że wszystkie pola są wypełnione.
                        </p>
                        <div class="border-b border-gray-900/10 pb-8">
                          <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                            <!-- Name Field -->
                            <div class="sm:col-span-4">
                              <label for="edit-name" class="block text-sm font-medium leading-6 text-gray-900">Nazwa</label>
                              <div class="mt-2">
                                <input 
                                  v-model="form.edit.name" 
                                  type="text" 
                                  name="edit-name" 
                                  id="edit-name"
                                  autocomplete="name" 
                                  @blur="validateName('edit')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                />
                                <p v-if="form.edit.errors.name" class="text-red-500 text-xs mt-1">{{ form.edit.errors.name }}</p>
                              </div>
                            </div>

                            <!-- Price Field -->
                            <div class="sm:col-span-2">
                              <label for="edit-price" class="block text-sm font-medium leading-6 text-gray-900">Cena</label>
                              <div class="mt-2">
                                <input 
                                  v-model="form.edit.price" 
                                  type="number" 
                                  step="0.01" 
                                  name="edit-price"
                                  id="edit-price" 
                                  @blur="validatePrice('edit')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                />
                                <p v-if="form.edit.errors.price" class="text-red-500 text-xs mt-1">{{ form.edit.errors.price }}</p>
                              </div>
                            </div>

                            <!-- Category Field -->
                            <div class="sm:col-span-6">
                              <label for="edit-category" class="block text-sm font-medium leading-6 text-gray-900">Kategoria</label>
                              <div class="mt-2">
                                <select 
                                  v-model="form.edit.category_id" 
                                  id="edit-category"
                                  @blur="validateCategory('edit')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                  <option value="" disabled>Wybierz opcję</option>
                                  <option v-for="category in categories" :key="category.id" :value="category.id">
                                    {{ category.name }}
                                  </option>
                                </select>
                                <p v-if="form.edit.errors.category_id" class="text-red-500 text-xs mt-1">{{ form.edit.errors.category_id }}</p>
                              </div>
                            </div>

                            <!-- Description Field -->
                            <div class="sm:col-span-6">
                              <label for="edit-description" class="block text-sm font-medium leading-6 text-gray-900">Opis</label>
                              <div class="mt-2">
                                <textarea 
                                  v-model="form.edit.description" 
                                  id="edit-description" 
                                  name="description"
                                  rows="3" 
                                  @blur="validateDescription('edit')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                </textarea>
                                <p v-if="form.edit.errors.description" class="text-red-500 text-xs mt-1">{{ form.edit.errors.description }}</p>
                              </div>
                            </div>

                            <!-- Stock Field -->
                            <div class="sm:col-span-6">
                              <label for="edit-stock" class="block text-sm font-medium leading-6 text-gray-900">Ilość w magazynie</label>
                              <div class="mt-2">
                                <input 
                                  v-model="form.edit.stock" 
                                  type="number" 
                                  name="edit-stock" 
                                  id="edit-stock"
                                  @blur="validateStock('edit')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                />
                                <p v-if="form.edit.errors.stock" class="text-red-500 text-xs mt-1">{{ form.edit.errors.stock }}</p>
                              </div>
                            </div>

                            <!-- Image Upload Field -->
                            <div class="sm:col-span-6">
                              <label for="edit-image" class="block text-sm font-medium leading-6 text-gray-900">Zdjęcie</label>
                              <div class="mt-2">
                                <input 
                                  type="file" 
                                  id="edit-image" 
                                  @change="handleImageUpload" 
                                  accept="image/*"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                />
                                <p class="text-sm text-gray-500 mt-1">Wybierz zdjęcie do edycji.</p>
                                <!-- <div v-if="form.edit.image" class="mt-2">
                                  <img :src="form.edit.image" alt="Image Preview" class="h-24 w-24 object-cover rounded-md" />
                                </div> -->
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
import { ref, onMounted } from "vue";
import axios from 'axios';
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from "@headlessui/vue";
import { PlusCircleIcon, PhotoIcon, TrashIcon, PencilSquareIcon } from "@heroicons/vue/24/outline";

const API_URL = import.meta.env.VITE_API_URL;
const addProductOpen = ref(false)
const editProductOpen = ref(false)
const deleteProductOpen = ref(false)
const currentEditId = ref()
const currentDeleteId = ref()
const currentDeletename = ref()
const mainImage = ref();
const additionalImages = ref([]);
const previewImages = ref([]);

const categories = ref([]);
const products = ref([]);

const form = ref({
  add: {
    name: '',
    price: null,
    description: '',
    stock: '',
    category_id: null,
    image: '',
    errors: {
      name: '',
      price: '',
      description: '',
      stock: '',
      category_id: '',
      image: ''
    }
  },
  edit: {
    name: '',
    price: null,
    description: '',
    stock: '',
    category_id: null,
    image: '',
    errors: {
      name: '',
      price: '',
      description: '',
      stock: '',
      category_id: '',
      image: ''
    }
  }
});

const validateName = (formType) => {
    form.value[formType].errors.name = form.value[formType].name.trim() ? '' : 'Nazwa jest wymagana.';
}

const validatePrice = (formType) => {
    const price = form.value[formType].price;
    form.value[formType].errors.price = price > 0 ? '' : 'Cena musi być większa niż zero.';
}

const validateStock = (formType) => {
    const stock = form.value[formType].stock;
    form.value[formType].errors.stock = stock >= 0 ? '' : 'Ilość w magazynie nie może być ujemna.';
}

const validateCategory = (formType) => {
    form.value[formType].errors.category_id = form.value[formType].category_id ? '' : 'Kategoria jest wymagana.';
}

const validateDescription = (formType) => {
    form.value[formType].errors.description = form.value[formType].description.trim() ? '' : 'Opis produktu jest wymagany.';
}

const validateImage = (formType) => {
    const images = form.value[formType].image || [];
    form.value[formType].errors.image = images.length > 0 ? '' : 'Dodanie co najmniej jednego zdjęcia jest wymagane.';
}

const handleImageUpload = async (event) => {
  const files = Array.from(event.target.files);
  previewImages.value.push(...files.map((file) => URL.createObjectURL(file)));

  const binaryImages = await Promise.all(files.map(async (file) => {
    const arrayBuffer = await file.arrayBuffer();
    return new Uint8Array(arrayBuffer);
  }));

  if (binaryImages.length > 0) {
    mainImage.value = binaryImages[0];
    additionalImages.value.push(...binaryImages.slice(1));
  }
};

const formatImage = (image) => {
  return `data:image/jpeg;base64,${image}`;
}

const toBase64 = (input) => {
  return new Promise((resolve, reject) => {
    if (input instanceof Blob || input instanceof File) {
      const reader = new FileReader();
      reader.readAsArrayBuffer(input);
      reader.onload = () => {
        const arrayBuffer = reader.result;
        const uint8Array = new Uint8Array(arrayBuffer);
        let binary = '';
        for (let i = 0; i < uint8Array.byteLength; i++) {
          binary += String.fromCharCode(uint8Array[i]);
        }
        resolve(btoa(binary));
      };
      reader.onerror = (error) => reject(error);
    } else if (input instanceof Uint8Array) {
      let binary = '';
      for (let i = 0; i < input.byteLength; i++) {
        binary += String.fromCharCode(input[i]);
      }
      resolve(btoa(binary));
    } else {
      reject(new TypeError("Input must be a File, Blob, or Uint8Array"));
    }
  });
};


const handleAddButton = async () => {
  form.value.add.image = mainImage.value;
  while(previewImages.value.length > 0) {
    previewImages.value.pop();
  }

  validateImage('add');
  validateName('add');
  validateCategory('add');
  validatePrice('add');
  validateStock('add');
  validateDescription('add');

  const hasErrors = Object.values(form.value.add.errors).some(error => error);

  if (!hasErrors) {
    await addProduct(
      form.value.add.name,
      form.value.add.category_id,
      form.value.add.price,
      form.value.add.stock,
      form.value.add.description,
      form.value.add.image,
      additionalImages
    );
    await fetchProducts();
    addProductOpen.value = false;
    resetAddForm();
  } else {
    console.error("Form validation errors:", form.value.add.errors);
  }
};

const addProduct = async (productName, categoryId, price, stockQuantity, description, mainImage, additionalImages) => {
  try {
    // additionalImages = [mainImage]

    const mainImageBase64 = mainImage ? await toBase64(mainImage) : null
    // const additionalImagesBase64 = additionalImages 
    //   ? await Promise.all(additionalImages.map(image => toBase64(image)))
    //   : null

    await axios.post(API_URL + '/products', {
      product_name: productName,
      category_id: categoryId,
      price: price,
      stock_quantity: stockQuantity || 0,
      description: description,
      main_image: mainImageBase64
      // additional_images: additionalImagesBase64
    });
  } catch (error) {
    console.error('Error adding product:', error);
  }
};

const resetAddForm = () => {
  form.value.add.title = '';
  form.value.add.category_id = null;
  form.value.add.price = null;
  form.value.add.stock = '';
  form.value.add.description = '';
  form.value.add.image = '';
  form.value.add.errors.title = '';
  form.value.add.errors.price = '';
  form.value.add.errors.stock = '';
  form.value.add.errors.description = '';
  mainImage.value = null;
  additionalImages.value = null;
};

const handleDeleteButton = (id) => {
  currentDeleteId.value = id
  currentDeletename.value = products.value.find(p => p.id === id).name
  deleteProductOpen.value = true
}

const handleEditButton = (id) => {
  const product = products.value.find(p => p.id === id)
  while(previewImages.value.length > 0) {
    previewImages.value.pop();
  }
  form.value.edit.name = product.name
  form.value.edit.price = product.price
  form.value.edit.stock = product.stock
  form.value.edit.image = product.image
  form.value.edit.description = product.description
  form.value.edit.category_id = product.category_id
  currentEditId.value = id
  editProductOpen.value = true
}

const submitEditProductForm = async () => {
  form.value.edit.image = mainImage.value

  validateImage('edit');
  validateName('edit');
  validateCategory('edit');
  validatePrice('edit');
  validateStock('edit');
  validateDescription('edit');

  const hasErrors = Object.values(form.value.edit.errors).some(error => error);

  if (!hasErrors) {
    await editProduct(
      currentEditId.value,
      form.value.edit.name,
      form.value.edit.category_id,
      form.value.edit.price,
      form.value.edit.stock,
      form.value.edit.description,
      form.value.edit.image
    );
    await fetchProducts();
    editProductOpen.value = false;

    form.value.edit.name = '';
    form.value.edit.price = null;
    form.value.edit.stock = '';
    form.value.edit.description = '';
    form.value.edit.category_id = null;
    form.value.edit.image = '';
  } else {
    console.error("Form validation errors:", form.value.edit.errors);
  }
};

const editProduct = async (id, productName, categoryId, price, stockQuantity, description, mainImage) => {
  const product = products.value.find(p => p.id === id);
  if (product) {
    try {
      const mainImageBase64 = mainImage ? await toBase64(mainImage) : null

      await axios.put(API_URL + `/products/${id}`, {
        product_name: productName,
        category_id: categoryId,
        price: price,
        stock_quantity: stockQuantity,
        description: description,
        main_image: mainImageBase64
      });
    } catch (error) {
      console.error('Error updating product:', error);
    }
  }
}

const deleteProduct = async () => {
  try {
    await axios.delete(`${API_URL}/products/${currentDeleteId.value}`);
    fetchProducts();
    deleteProductOpen.value = false;
  } catch (error) {
    console.error('Błąd podczas usuwania produktu:', error);
  }
};

const getCategoryById = (id) => {
  return categories.value.find((category) => category.id === id);
};

const truncateDescription = (description) => {
  return description.length > 15 ? description.substring(0, 15) + '...' : description;
}

const fetchCategories = async () => {
  try {
    const response = await axios.get(API_URL + '/categories')
    categories.value = response.data.map((category) => ({
      ...category,
      name: category.category_name,
    }))
  } catch (error) {
    console.error('Błąd podczas pobierania kategorii:', error)
  }
}

const fetchProducts = async () => {
  try {
    const response = await axios.get(API_URL + '/products')
    products.value = response.data.map((product) => ({
      ...product,
      name: product.product_name,
      stock: product.stock_quantity
    }))
  } catch (error) {
    console.error('Błąd podczas pobierania produktów:', error)
  }
}

onMounted(() => {
  fetchCategories();
  fetchProducts();
});
</script>
