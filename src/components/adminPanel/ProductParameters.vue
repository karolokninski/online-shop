<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Parametry Produktów</h1>

    <!-- Tabela Parametrów -->
    <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden mb-4">
      <thead class="bg-indigo-600 text-white">
        <tr>
          <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">ID Parametru</th>
          <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Nazwa Parametru</th>
          <th class="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">Akcje</th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="parameter in parameters" :key="parameter.id" class="hover:bg-gray-100 transition duration-200">
          <td class="px-6 py-4 whitespace-nowrap">{{ parameter.id }}</td>
          <td class="px-6 py-4 whitespace-nowrap">{{ parameter.name }}</td>
          <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
            <button @click="editParameter(parameter.id)"
              class="text-indigo-600 hover:text-indigo-900 mr-3">Edytuj</button>
            <button @click="deleteParameter(parameter.id)" class="text-red-600 hover:text-red-900">Usuń</button>
          </td>
        </tr>
      </tbody>
    </table>
    <button
      class="mt-4 inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      @click="addParameterOpen = true">
      Dodaj parametr
    </button>

    <!-- Modal do dodawania parametrów -->
    <TransitionRoot as="template" :show="addParameterOpen">
      <Dialog class="relative z-10" @close="addParameterOpen = false">
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
                    <div
                      class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-green-100 sm:mx-0 sm:h-10 sm:w-10">
                      <PlusCircleIcon class="h-6 w-6 text-green" aria-hidden="true" />
                    </div>
                    <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                      <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Dodaj parametr
                      </DialogTitle>
                      <div class="mt-2">
                        <p class="text-sm text-gray-500">Upewnij się, że wszystkie pola są wypełnione.</p>

                        <form method="POST" onsubmit="return false">
                          <div class="border-b border-gray-900/10 pb-8">
                            <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                              <div class="sm:col-span-3">
                                <label for="product-id"
                                  class="block text-sm font-medium leading-6 text-gray-900">Produkt</label>
                                <div class="mt-2">
                                  <select v-model="newParameter.productId" id="product-id"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600">
                                    <option disabled value="">Wybierz produkt</option>
                                    <option v-for="product in products" :key="product.id" :value="product.id">
                                      {{ product.name }}
                                    </option>
                                  </select>
                                </div>
                              </div>

                              <div class="sm:col-span-3">
                                <label for="parameter-name"
                                  class="block text-sm font-medium leading-6 text-gray-900">Nazwa Parametru</label>
                                <div class="mt-2">
                                  <input v-model="newParameter.name" type="text" id="parameter-name"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600" />
                                </div>
                              </div>

                              <div class="sm:col-span-3">
                                <label for="parameter-value"
                                  class="block text-sm font-medium leading-6 text-gray-900">Wartość</label>
                                <div class="mt-2">
                                  <input v-model="newParameter.value" type="text" id="parameter-value"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600" />
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
                    @click="handleAddParameter">
                    Dodaj
                  </button>
                  <button type="button"
                    class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                    @click="addParameterOpen = false">
                    Anuluj
                  </button>
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
import { PlusCircleIcon } from "@heroicons/vue/24/outline";

const API_URL = import.meta.env.VITE_API_URL;

const parameters = ref([]);

const products = ref([
  { id: 101, name: "Produkt A" },
  { id: 102, name: "Produkt B" },
  { id: 103, name: "Produkt C" },
]);


const addParameterOpen = ref(false);
const newParameter = ref({
  productId: null,
  name: "",
  value: "",
});

const handleAddParameter = () => {
  if (newParameter.value.productId && newParameter.value.name && newParameter.value.value) {
    parameters.value.push({
      id: parameters.value.length + 1,
      productId: newParameter.value.productId,
      name: newParameter.value.name,
      value: newParameter.value.value,
    });
    
    newParameter.value = { productId: null, name: "", value: "" };
    addParameterOpen.value = false;
  }
};

const editParameter = (id) => {
  console.log("Edytuj parametr o ID:", id);
  // Logika edytowania parametru
};

const deleteParameter = (id) => {
  parameters.value = parameters.value.filter(param => param.id !== id);
  console.log("Usunięto parametr o ID:", id);
};

const fetchParameters = async () => {
  try {
    const response = await axios.get(API_URL + '/parameters')
    parameters.value = response.data.map((parameter) => ({
      ...parameter,
      name: parameter.parameter_name,
    }))
    console.log(parameters.value)
  } catch (error) {
    console.error('Błąd podczas pobierania kategorii:', error)
  }
}

onMounted(fetchParameters);
</script>
