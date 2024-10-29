<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Parametry Produktów</h1>

    <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden mb-4">
      <thead class="bg-indigo-600 text-white">
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Nazwa Parametru</th>
          <th class="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">Akcje</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="parameter in parameters" :key="parameter.id" class="hover:bg-gray-100 transition duration-200">
          <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ parameter.name }}</td>
          <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
            <button @click="handleEditButton(parameter.id)"
              class="text-indigo-600 hover:text-indigo-900 mr-3"><PencilSquareIcon class="h-5 w-5 inline-block" aria-hidden="true" /></button>
            <button @click="handleDeleteButton(parameter.id)" class="text-red-600 hover:text-red-900"><TrashIcon class="h-5 w-5 inline-block" aria-hidden="true" /></button>
          </td>
        </tr>
      </tbody>
    </table>
    <button
      class="mt-4 inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      @click="addParameterOpen = true">
      Dodaj parametr
    </button>

    <TransitionRoot as="addParameter" :show="addParameterOpen">
      <Dialog class="relative z-10" @close="addParameterOpen = false">
        <TransitionChild as="addParameter" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
          leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>

        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="addParameter" enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel
                class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                <form @submit.prevent="submitAddParameterForm">
                  <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                    <div class="sm:flex sm:items-start">
                      <div
                        class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-green-100 sm:mx-0 sm:h-10 sm:w-10">
                        <PlusCircleIcon class="h-6 w-6 text-green-600" aria-hidden="true" />
                      </div>
                      <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                        <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Dodaj parametr
                        </DialogTitle>
                        <div class="mt-2">
                          <p class="text-sm text-gray-500">Upewnij się, że wszystkie pola są wypełnione.</p>
                          <div class="border-b border-gray-900/10 pb-8">
                            <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                              <div class="sm:col-span-6">
                                <label for="parameter-name"
                                  class="block text-sm font-medium leading-6 text-gray-900">Nazwa Parametru</label>
                                <div class="mt-2">
                                  <input v-model="form.add.name" type="text" id="parameter-name" @blur="validateName('add')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form.add.errors.name" class="text-red-500 text-xs mt-1">{{
                                    form.add.errors.name }}</p>
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
                      @click="handleAddParameter"
                      class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto">
                      Dodaj
                    </button>
                    <button type="button"
                      class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                      @click="addParameterOpen = false">
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

    <TransitionRoot as="deleteParameter" :show="deleteParameterOpen">
      <Dialog class="relative z-10" @close="deleteParameterOpen = false">
        <TransitionChild as="deleteParameter" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
          leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="deleteParameter" enter="ease-out duration-300"
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
                      <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Usuń parametr</h3>
                      <div class="mt-2">
                        <p class="text-sm text-gray-500">Czy na pewno chcesz usunąć parametr <b>{{ currentDeleteName }}</b>? Ta czynność jest nieodwracalna.</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                  <button @click="submitDeleteParameter" type="button" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto">Usuń</button>
                  <button @click="deleteParameterOpen = false" type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto">Anuluj</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <TransitionRoot as="editProduct" :show="editParameterOpen">
      <Dialog class="relative z-10" @close="editParameterOpen = false">
        <TransitionChild as="editParameter" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
          leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>

        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="editParameter" enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel
                class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                <form @submit.prevent="submitEditProductForm">
                  <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                    <div class="sm:flex sm:items-start">
                      <div
                        class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                        <PencilSquareIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                      </div>
                      <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                        <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Edytuj parametr
                        </DialogTitle>
                        <div class="mt-2">
                          <p class="text-sm text-gray-500">
                            Upewnij się, że wszystkie pola są wypełnione.
                          </p>
                          <div class="border-b border-gray-900/10 pb-8">
                            <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                              <div class="sm:col-span-6">
                                <label for="edit-name"
                                  class="block text-sm font-medium leading-6 text-gray-900">Nazwa</label>
                                <div class="mt-2">
                                  <input v-model="form.edit.name" type="text" name="edit-name" id="edit-name"
                                    autocomplete="name" @blur="validatename('edit')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form.edit.errors.name" class="text-red-500 text-xs mt-1">{{
                                    form.edit.errors.name }}</p>
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
                      @click="submitEditParameterForm">
                      Edytuj
                    </button>
                    <button type="button"
                      class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                      @click="editParameterOpen = false">
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
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from 'axios';
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from "@headlessui/vue";
import { PlusCircleIcon ,PencilSquareIcon, TrashIcon } from "@heroicons/vue/24/outline";

const API_URL = import.meta.env.VITE_API_URL;

const addParameterOpen = ref(false);
const editParameterOpen = ref(false);
const deleteParameterOpen = ref(false);

const currentEditId = ref(null);
const currentDeleteId = ref(null);
const currentDeleteName = ref("");

const parameters = ref([]);

const form = ref({
  add: {
    name: "",
    errors: { name: "" }
  },
  edit: {
    name: "",
    errors: { name: "" }
  }
});

const validateName = (type) => {
  const formInstance = type === 'add' ? form.value.add : form.value.edit;
  formInstance.errors.name = !formInstance.name ? 'To pole jest wymagane' : '';
};

const fetchParameters = async () => {
  try {
    const response = await axios.get(`${API_URL}/parameters`);
    parameters.value = response.data.map(parameter => ({
      ...parameter,
      name: parameter.parameter_name
    }));
  } catch (error) {
    console.error('Błąd podczas pobierania kategorii:', error);
  }
};

const handleAddParameter = () => {
  validateName('add');
  if (!form.value.add.errors.name) {
    submitAddParameterForm();
  }
};
const checkIfParameterExists = async (name) => {
  form.value.add.errors.name = '';
  try {
    const response = await axios.get(`${API_URL}/parameters?name=${name}`);
    return response.data.exists;
  } catch (error) {
    console.error('Error checking parameter existence:', error);
    return false;
  }
};
const submitAddParameterForm = async () => {
  try {

    const parameterExists = await checkIfParameterExists(form.value.add.name);

if (parameterExists) {
  form.value.add.errors.name = 'Parametr o tej nazwie już istnieje.';
  return;
}
    
    await axios.post(`${API_URL}/parameters`, { parameter_name: form.value.add.name });
    fetchParameters();
    form.value.add.name = "";
    addParameterOpen.value = false;
  } catch (error) {
    console.error('Error adding parameter:', error);
  }
};

const handleEditButton = (id) => {
  const parameter = parameters.value.find(p => p.id === id);
  if (parameter) {
    currentEditId.value = id;
    form.value.edit.name = parameter.name;
    editParameterOpen.value = true;
  }
};

const submitEditParameterForm = async () => {
  validateName('edit');
  if (!form.value.edit.errors.name) {
    try {
      await axios.put(`${API_URL}/parameters/${currentEditId.value}`, { parameter_name: form.value.edit.name });
      fetchParameters();
      form.value.edit.name = "";
      editParameterOpen.value = false;
    } catch (error) {
      console.error('Error editing parameter:', error);
    }
  }
};

const handleDeleteButton = (id) => {
  const parameter = parameters.value.find(p => p.id === id);
  if (parameter) {
    currentDeleteId.value = id;
    currentDeleteName.value = parameter.name;
    deleteParameterOpen.value = true;
  }
};

const submitDeleteParameter = async () => {
  try {
    if (!currentDeleteId.value) {
      console.error('No ID selected for deletion');
      return;
    }
    
    await axios.delete(`${API_URL}/parameters/${currentDeleteId.value}`);
    fetchParameters();
    deleteParameterOpen.value = false;
    currentDeleteId.value = null;
  } catch (error) {
    console.error('Error deleting parameter:', error);
  }
};
onMounted(fetchParameters);
</script>