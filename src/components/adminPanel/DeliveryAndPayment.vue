<template>
  <div class="flex justify-around gap-8 mt-8">

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
      <button class="bg-indigo-600 text-white px-4 py-2 rounded" @click="addProviderOpen = true">Dodaj dostawcę</button>
    </div>


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
      <button class="bg-indigo-600 text-white px-4 py-2 rounded" @click="addPaymentMethodOpen = true">Dodaj formę płatności</button>
    </div>


    <div class="text-black">
      <h2 class="text-2xl font-bold mb-4">Zamówienia</h2>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden mb-4">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">ID Zamówienia</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">ID Formy Płatności</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">ID Dostawcy</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="order in orders" :key="order.id" class="hover:bg-gray-100 transition">
            <td class="px-6 py-4">{{ order.id }}</td>
            <td class="px-6 py-4">{{ order.paymentMethodId }}</td>
            <td class="px-6 py-4">{{ order.providerId }}</td>
            <td class="px-6 py-4 text-right">
              <button @click="editOrder(order.id)" class="text-indigo-600 mr-2">Edytuj</button>
              <button @click="deleteOrder(order.id)" class="text-red-600">Usuń</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>


  <TransitionRoot as="template" :show="addProviderOpen">
    <Dialog class="relative z-10" @close="addProviderOpen = false">

    </Dialog>
  </TransitionRoot>

  <TransitionRoot as="template" :show="addPaymentMethodOpen">
    <Dialog class="relative z-10" @close="addPaymentMethodOpen = false">

    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref } from "vue";
import { Dialog, TransitionRoot } from "@headlessui/vue";


const addProviderOpen = ref(false);
const providers = ref([
  { id: 1, name: "InPost" },
  { id: 2, name: "DHL" },
]);


const addPaymentMethodOpen = ref(false);
const paymentMethods = ref([
  { id: 1, name: "Przelewy24" },
  { id: 2, name: "PayU" },
]);

const orders = ref([
  { id: 1, paymentMethodId: 1, providerId: 2 },
  { id: 2, paymentMethodId: 2, providerId: 1 },
]);

const editProvider = (id) => { /* Kod edycji dostawcy */ };
const deleteProvider = (id) => { /* Kod usuwania dostawcy */ };

const editPaymentMethod = (id) => { /* Kod edycji formy płatności */ };
const deletePaymentMethod = (id) => { /* Kod usuwania formy płatności */ };

const editOrder = (id) => { /* Kod edycji zamówienia */ };
const deleteOrder = (id) => { /* Kod usuwania zamówienia */ };
</script>
