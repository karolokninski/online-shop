<template>
  <div class="flex justify-around gap-8 mt-8">
    <!-- Dostawcy -->
    <div class="text-black">
      <h2 class="text-2xl font-bold mb-4">Dostawcy</h2>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden mb-4">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">ID Dostawcy</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">Dostawca</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="provider in providers" :key="provider.id" class="hover:bg-gray-100 transition">
            <td class="px-6 py-4">{{ provider.id }}</td>
            <td class="px-6 py-4">{{ provider.name }}</td>
            <td class="px-6 py-4 text-right">
              <button @click="editProvider(provider.id)" class="text-indigo-600 mr-2">Edytuj</button>
              <button @click="deleteProvider(provider.id)" class="text-red-600">Usuń</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="mt-4">
        <div class="flex space-x-2">
          <input v-model="categoryName" type="text" placeholder="Nazwa dostawcy"
            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            <button class="bg-indigo-600 text-white px-4 py-2 rounded" @click="addProviderOpen = true">Dodaj dostawcę</button>
        </div>
      </div>
  
    </div>

    <!-- Formy Płatności -->
    <div class="text-black">
      <h2 class="text-2xl font-bold mb-4">Formy Płatności</h2>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden mb-4">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">ID Formy Płatności</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">Nazwa Formy Płatności</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="paymentMethod in paymentMethods" :key="paymentMethod.id" class="hover:bg-gray-100 transition">
            <td class="px-6 py-4">{{ paymentMethod.id }}</td>
            <td class="px-6 py-4">{{ paymentMethod.name }}</td>
            <td class="px-6 py-4 text-right">
              <button @click="editPaymentMethod(paymentMethod.id)" class="text-indigo-600 mr-2">Edytuj</button>
              <button @click="deletePaymentMethod(paymentMethod.id)" class="text-red-600">Usuń</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="mt-4">
        <div class="flex space-x-2">
          <input v-model="categoryName" type="text" placeholder="Nazwa formy płatności"
            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            <button class="bg-indigo-600 text-white px-4 py-2 rounded" @click="addPaymentMethodOpen = true">Dodaj formę płatności</button>
        </div>
      </div>
      
    </div>

  
  </div>

</template>

<script setup>
import { ref } from "vue";


// Data and state variables
const addProviderOpen = ref(false);
const addPaymentMethodOpen = ref(false);
const providers = ref([{ id: 1, name: "InPost" }, { id: 2, name: "DHL" }]);
const paymentMethods = ref([{ id: 1, name: "Przelewy24" }, { id: 2, name: "PayU" }]);



</script>
