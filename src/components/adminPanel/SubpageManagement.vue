<template>
  <div class="text-black">
    <h1 class=" text-3xl mb-8">Podstrony</h1>
    
    <table class="w-auto table-auto bg-white rounded-md shadow-lg">
      <thead class="bg-gray-50">
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Nazwa
          </th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Ścieżka
          </th>
          <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Aktywna
          </th>
          <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
            Akcje
          </th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="product in products" :key="product.id">
          <td class="px-6 py-4 whitespace-nowrap">
            <div class="text-sm font-medium text-gray-900">{{ product.title }}</div>
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            <div class="text-sm text-gray-900">{{ product.path }}</div>
          </td>
          <td class="px-6 py-4 whitespace-nowrap">
            <div v-if="product.active" class="text-sm text-gray-900">Tak</div>
            <div v-else class="text-sm text-gray-900">Nie</div>
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
            <button 
              @click="handleEditButton(product.id)" 
              class="text-indigo-600 hover:text-indigo-900 mr-3">
              Edit
            </button>
            <button 
              @click="deleteProduct(product.id)" 
              class="text-red-600 hover:text-red-900">
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <button
      @click="addSubpageOpen = true"
      class="text-indigo-600 hover:text-indigo-900">
      Dodaj podstronę
    </button>
  </div>

  <TransitionRoot as="template" :show="addSubpageOpen">
    <Dialog class="relative z-10" @close="addSubpageOpen = false">
      <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                <div class="sm:flex sm:items-start">
                  <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-green-100 sm:mx-0 sm:h-10 sm:w-10">
                    <DocumentPlusIcon class="h-6 w-6 text-green" aria-hidden="true" />
                  </div>
                  <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                    <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Dodaj nową podstronę</DialogTitle>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">Upewnij się, że wszystkie pola są wypełnione poprawnie, aby dodać nową podstronę do swojej witryny.</p>
                      
                      <form method="POST" onsubmit="return false">
                        <div class="border-b border-gray-900/10 pb-8">
                          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                            <div class="sm:col-span-2">
                              <label for="first-name" class="block text-sm font-medium leading-6 text-gray-900">Nazwa</label>
                              <div class="mt-2">
                                <input v-model="title" type="text" name="first-name" id="first-name" autocomplete="given-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>

                            <div class="sm:col-span-4">
                              <label for="last-name" class="block text-sm font-medium leading-6 text-gray-900">Ścieżka URL</label>
                              <div class="mt-2 flex">
                                <span class="mt-2 mr-1 text-black text-sm font-bold">geeked.tech/info/</span>
                                <input v-model="path" type="text" name="last-name" id="last-name" autocomplete="family-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>

                            <!-- <div class="sm:col-span-3">
                              <label for="country" class="block text-sm font-medium leading-6 text-gray-900">Country</label>
                              <div class="mt-2">
                                <select id="country" name="country" autocomplete="country-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                                  <option>United States</option>
                                  <option>Canada</option>
                                  <option>Mexico</option>
                                </select>
                              </div>
                            </div> -->

                            <div class="col-span-full">
                              <label for="about" class="block text-sm font-medium leading-6 text-gray-900">Treść</label>
                              <div class="mt-2">
                                <textarea v-model="content" id="about" name="about" rows="3" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>

                            <div class="col-span-full">
                              <label class="inline-flex items-center cursor-pointer">
                                <span class="mr-3 text-sm font-medium text-black">Aktywna</span>
                                <input v-model="is_active" type="checkbox" value="" class="sr-only peer">
                                <div class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600"></div>
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
                <button type="button" class="inline-flex w-full justify-center rounded-md bg-primary-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-primary-600 sm:ml-3 sm:w-auto" @click="handleAddButton">Dodaj</button>
                <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="addSubpageOpen = false" ref="cancelButtonRef">Cancel</button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
  import { DocumentPlusIcon } from '@heroicons/vue/24/outline'
  
  const API_URL = import.meta.env.VITE_API_URL
  const addSubpageOpen = ref(false)
  const products = ref([])

  const title = ref('')
  const path = ref('')
  const content = ref('')
  const is_active = ref(false)

  const handleAddButton = () => {
    addProduct(title.value, content.value, path.value, is_active.value)
    addSubpageOpen.value = false
    fetchSubpages
  }
  const handleEditButton = (id) => {
    const product = this.products.find(p => p.id === id)
    if (product) {
      editProduct(id, product.title, product.content, product.path, !product.is_active)
    }
    fetchSubpages
  }
  const fetchSubpages = async () => {
    try {
      const response = await axios.get(API_URL + '/subpages')
      products.value = response.data
    } catch (error) {
      console.error('Error fetching subpages:', error)
    }
  }
  const addProduct = async (title, content, path, is_active) => {
    try {
      const response = await axios.post(API_URL + '/subpages', {
        title: title,
        content: content,
        path: path,
        is_active: is_active,
      })
    } catch (error) {
      console.error('Error adding subpage:', error)
    }
  }
  const editProduct = async (id, title, content, path, is_active) => {
    const product = products.value.find(p => p.id === id)
    if (product) {
      try {
        const response = await axios.put(API_URL + `/subpages/${id}`, {
          title: title,
          content: content,
          path: path,
          is_active: is_active,
        })
      } catch (error) {
        console.error('Error editing subpage:', error)
      }
    }
  }
  const deleteProduct = async (id) => {
    try {
      await axios.delete(API_URL + `/subpages/${id}`)
      products.value = products.value.filter(p => p.id !== id)
    } catch (error) {
      console.error('Error deleting subpage:', error)
    }
  }

  onMounted(fetchSubpages)
</script>

