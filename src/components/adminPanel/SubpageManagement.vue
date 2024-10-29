<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Podstrony</h1>
    <div>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Tytuł</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Ścieżka URL</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Aktywna</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="product in products" :key="product.id" class="hover:bg-gray-100 transition duration-200">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ product.title }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ product.path }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span :class="product.isActive ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                {{ product.isActive ? 'Tak' : 'Nie' }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="handleEditButton(product.id)" class="text-indigo-600 hover:text-indigo-900 mr-3">
                Edytuj
              </button>
              <button @click="handleDeleteButton(product.id)" class="text-red-600 hover:text-red-900">
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

  <TransitionRoot as="addSubpage" :show="addSubpageOpen">
    <Dialog class="relative z-10" @close="addSubpageOpen = false">
      <TransitionChild as="addSubpage" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
        leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="addSubpage" enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel
              class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <form @submit.prevent="">
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
                          <div class="border-b border-gray-900/10 pb-8">
                            <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                              <div class="sm:col-span-2">
                                <label for="add-title" class="block text-sm font-medium leading-6 text-gray-900">Tytuł</label>
                                <div class="mt-2">
                                  <input 
                                    v-model="form.add.title" 
                                    type="text" 
                                    name="add-title" 
                                    id="add-title" 
                                    autocomplete="title"
                                    @blur="validateTitle('add')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                  />
                                  <p v-if="form.add.errors.title" class="text-red-500 text-xs mt-1">{{ form.add.errors.title }}</p>
                                </div>
                              </div>
                              <div class="sm:col-span-4">
                                <label for="add-path" class="block text-sm font-medium leading-6 text-gray-900">Ścieżka URL</label>
                                <div class="mt-2">
                                  <div class="flex">
                                    <span class="mt-2 mr-1 text-black text-sm font-medium">geeked.tech/info/</span>
                                      <input 
                                        v-model="form.add.path" 
                                        type="text" 
                                        name="path" 
                                        id="add-path"
                                        @blur="validatePath('add')"
                                        class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                      />
                                    </div>
                                  <p v-if="form.add.errors.path" class="text-red-500 text-xs mt-1">{{ form.add.errors.path }}</p>
                                </div>
                              </div>
                              <div class="sm:col-span-6">
                                <label for="add-content" class="block text-sm font-medium leading-6 text-gray-900">Treść</label>
                                <div class="mt-2">
                                  <textarea 
                                    v-model="form.add.content" 
                                    name="content" 
                                    id="add-content" 
                                    rows="3"
                                    @blur="validateContent('add')"
                                    class="block w-full max-h-48 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                  </textarea>
                                  <p v-if="form.add.errors.content" class="text-red-500 text-xs mt-1">{{ form.add.errors.content }}</p>
                                </div>
                              </div>
                              <div class="sm:col-span-6">
                                <label class="inline-flex items-center cursor-pointer">
                                  <input 
                                    v-model="form.add.isActive" 
                                    type="checkbox" 
                                    id="is-active" 
                                    class="sr-only peer"
                                  />
                                  <div class="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600"></div>
                                  <span class="ms-3 text-sm font-medium text-black">Aktywa</span>
                                </label>
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
                    @click="submitAddProductForm">
                    Dodaj
                  </button>
                  <button type="button"
                    class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                    @click="addSubpageOpen = false">
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

  <TransitionRoot as="editSubpage" :show="editSubpageOpen">
    <Dialog class="relative z-10" @close="editSubpageOpen = false">
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
              <form @submit.prevent="">
                <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                  <div class="sm:flex sm:items-start">
                    <div class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                      <PencilSquareIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                    </div>
                    <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                      <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Edytuj podstronę</DialogTitle>
                      <div class="mt-2">
                        <p class="text-sm text-gray-500">
                          Upewnij się, że wszystkie pola są wypełnione.
                        </p>
                        <div class="border-b border-gray-900/10 pb-8">
                          <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                            <div class="sm:col-span-2">
                              <label for="edit-title" class="block text-sm font-medium leading-6 text-gray-900">Tytuł</label>
                              <div class="mt-2">
                                <input 
                                  v-model="form.edit.title" 
                                  type="text" 
                                  name="edit-title" 
                                  id="edit-title" 
                                  autocomplete="title"
                                  @blur="validateTitle('edit')"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                />
                                <p v-if="form.edit.errors.title" class="text-red-500 text-xs mt-1">{{ form.edit.errors.title }}</p>
                              </div>
                            </div>
                            <div class="sm:col-span-4">
                              <label for="edit-path" class="block text-sm font-medium leading-6 text-gray-900">Ścieżka URL</label>
                              <div class="mt-2">
                                <div class="flex">
                                  <span class="mt-2 mr-1 text-black text-sm font-medium">geeked.tech/info/</span>
                                    <input 
                                      v-model="form.edit.path" 
                                      type="text" 
                                      name="path" 
                                      id="edit-path"
                                      @blur="validatePath('edit')"
                                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" 
                                    />
                                  </div>
                                <p v-if="form.edit.errors.path" class="text-red-500 text-xs mt-1">{{ form.edit.errors.path }}</p>
                              </div>
                            </div>
                            <div class="sm:col-span-6">
                              <label for="edit-content" class="block text-sm font-medium leading-6 text-gray-900">Treść</label>
                              <div class="mt-2">
                                <textarea 
                                  v-model="form.edit.content" 
                                  name="content" 
                                  id="edit-content" 
                                  rows="3"
                                  @blur="validateContent('edit')"
                                  class="block w-full max-h-48 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                </textarea>
                                <p v-if="form.edit.errors.content" class="text-red-500 text-xs mt-1">{{ form.edit.errors.content }}</p>
                              </div>
                            </div>
                            <div class="sm:col-span-6">
                              <label class="inline-flex items-center cursor-pointer">
                                <input 
                                  v-model="form.edit.isActive" 
                                  type="checkbox" 
                                  id="is-active" 
                                  class="sr-only peer"
                                />
                                <div class="relative w-11 h-6 bg-gray-200 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600"></div>
                                <span class="ms-3 text-sm font-medium text-black">Aktywa</span>
                              </label>
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
                    @click="editSubpageOpen = false">
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
  
  <TransitionRoot as="deleteSubpage" :show="deleteSubpageOpen">
    <Dialog class="relative z-10" @close="deleteSubpageOpen = false">
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
                    <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Usuń podstronę</h3>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">Czy na pewno chcesz usunąć podstronę <b>{{ currentDeleteTitle }}</b>? Wszystkie zapisane dane na jej temat zostaną utraconę. Ta czynność jest nieodwracalna.</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                <button @click="deleteProduct(currentDeleteId); deleteSubpageOpen=false" type="button" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto">Usuń</button>
                <button @click="deleteSubpageOpen = false" type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Anuluj</button>
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
  import { PlusCircleIcon, PencilSquareIcon } from '@heroicons/vue/24/outline'

  const API_URL = import.meta.env.VITE_API_URL
  const addSubpageOpen = ref(false)
  const editSubpageOpen = ref(false)
  const deleteSubpageOpen = ref(false)
  const currentEditId = ref()
  const currentDeleteId = ref()
  const currentDeleteTitle = ref()
  const products = ref([])

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
  
  const handleEditButton = (id) => {
    const product = products.value.find(p => p.id === id)
    form.value.edit.title = product.title
    form.value.edit.path = product.path.replace(/^\/info\//, '')
    form.value.edit.content = product.content
    form.value.edit.isActive = product.isActive
    currentEditId.value = id
    editSubpageOpen.value = true
  }

  const handleDeleteButton = (id) => {
    currentDeleteId.value = id
    currentDeleteTitle.value = products.value.find(p => p.id === id).title
    deleteSubpageOpen.value = true
  }

  const validateTitle = (formType) => {
    form.value[formType].errors.title = form.value[formType].title.trim() ? '' : 'Tytuł jest wymagany.';
  }
  const validatePath = (formType) => {
    const regex = /^[a-zA-Z0-9\-_/]*$/;
    const path = form.value[formType].path.trim();

    if (path) {
      form.value[formType].errors.path = regex.test(path) ? '' : 'Nieprawidłowa ścieżka URL.';
    } else {
      form.value[formType].errors.path = 'Ścieżka URL jest wymagana.';
    }
  }
  const validateContent = (formType) => {
    form.value[formType].errors.content = form.value[formType].content.trim() ? '' : 'Treść jest wymagana.';
  }

  const submitAddProductForm = () => {
    validateTitle('add')
    validatePath('add')
    validateContent('add')

    if (!form.value.add.errors.title && !form.value.add.errors.path && !form.value.add.errors.content) {
      addProduct(form.value.add.title, '/info/' + form.value.add.path, form.value.add.content, form.value.add.isActive)
      fetchSubpages
      addSubpageOpen.value = false
      form.value.add.title.value = ''
      form.value.add.path.value = ''
      form.value.add.content.value = ''
      form.value.add.isActive.value = false
    }
  }

  const submitEditProductForm = () => {
    validateTitle('edit')
    validatePath('edit')
    validateContent('edit')
    if (!form.value.edit.errors.title && !form.value.edit.errors.path && !form.value.edit.errors.content) {
      editProduct(currentEditId.value, form.value.edit.title, '/info/' + form.value.edit.path, form.value.edit.content, form.value.edit.isActive)
      fetchSubpages
      editSubpageOpen.value = false
      form.value.edit.title.value = ''
      form.value.edit.path.value = ''
      form.value.edit.content.value = ''
      form.value.edit.isActive.value = false
    }
  }

  const fetchSubpages = async () => {
    try {
      const response = await axios.get(API_URL + '/subpages')
      products.value = response.data.map((product) => ({
        ...product,
        isActive: product.is_active,
      }))

    } catch (error) {
      console.error('Błąd podczas pobierania podstron:', error)
    }
  }

  const addProduct = async (title, path, content, isActive) => {
    try {
      await axios.post(API_URL + '/subpages', {
        title: title,
        content: content,
        path: path,
        is_active: isActive
      })
      
      products.value.push({
        title: title,
        content: content,
        path: path,
        isActive: isActive
      })
    } catch (error) {
      console.error('Błąd podczas dodawania podstrony:', error)
    }
  }

  const editProduct = async (id, title, path, content, isActive) => {
    const product = products.value.find(p => p.id === id)
    if (product) {
      try {
        await axios.put(API_URL + `/subpages/${id}`, {
          title: title,
          content: content,
          path: path,
          is_active: isActive,
        })

        product.title = title;
        product.content = content;
        product.path = path;
        product.isActive = isActive;
      } catch (error) {
        console.error('Błąd podczas aktualizacji podstrony:', error)
      }
    }
  }

  const deleteProduct = async (id) => {
    try {
      await axios.delete(`${API_URL}/subpages/${id}`)
      products.value = products.value.filter(product => product.id !== id)
    } catch (error) {
      console.error('Błąd podczas usuwania podstrony:', error)
    }
  };

  onMounted(fetchSubpages)
</script>
