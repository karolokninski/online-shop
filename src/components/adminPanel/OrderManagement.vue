<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Zamówienia</h1>
    <div>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">ID Zamówienia</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">ID Klienta</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Miasto</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Kod Pocztowy</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Ulica</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Nr Domu</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Data Zamówienia</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Dostawa</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Płatność</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="order in orders" :key="order.order_id" class="hover:bg-gray-100 transition duration-200">
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm font-medium text-gray-900">{{ order.order_id }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ order.customer_id }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ order.city }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ order.postal_code }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ order.street }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ order.house_number }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ order.order_date }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ order.shipment }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ order.payment }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="editOrder(order.id)" class="text-indigo-600 hover:text-indigo-900 mr-3">Edytuj</button>
              <button @click="deleteOrder(order.id)" class="text-red-600 hover:text-red-900">Usuń</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const orders = ref([
  {
    order_id: 1,
    customer_id: 101,
    city: "Warszawa",
    postal_code: "00-001",
    street: "Marszałkowska",
    house_number: "1A",
    order_date: "2024-10-25",
    shipment: "DHL",
    payment: "Przelewy24",
  },
  {
    order_id: 2,
    customer_id: 102,
    city: "Kraków",
    postal_code: "30-002",
    street: "Floriańska",
    house_number: "2B",
    order_date: "2024-10-26",
    shipment: "DHL",
    payment: "Przelewy24",
  },
]);
</script>
