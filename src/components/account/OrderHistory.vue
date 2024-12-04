<template>
  <div class="max-w-6xl mx-auto p-6 bg-gray-100 rounded-lg shadow-lg text-gray-900">
    <h2 class="text-2xl font-bold text-center">Historia zamówień</h2>
    <p class="text-lg font-semibold mb-6">Kliknij na zamówienie, aby zobaczyć jego szczegóły</p>

    <div v-if="orders.length > 0" v-for="(order, index) in orders" :key="index">
      <div 
        class="bg-white p-4 rounded-lg shadow mb-4 cursor-pointer" 
        @click="openModal(order)"
      >
        <p class="text-lg font-semibold mb-2"><strong>Data zamówienia:</strong> {{ formatDate(order.date) }}</p>
        <p class="text-lg font-semibold mb-2"><strong>Status zamówienia:</strong> {{ order.status }}</p>
        <p class="text-lg font-semibold"><strong>Łączna kwota:</strong> {{ order.total }} PLN</p>
      </div>
    </div>
    
  
    <div v-else class="text-center text-gray-500">
      Brak zamówień do wyświetlenia.
    </div>
    <transition name="modal">
      <div v-if="isModalOpen" class="fixed inset-0 bg-gray-500 bg-opacity-50 flex justify-center items-center">
        <div class="bg-white p-6 rounded-lg shadow-lg max-w-2xl w-full">
          <h3 class="text-2xl font-bold mb-4">Szczegóły zamówienia</h3>

          <div>
            <p class="mb-2"><strong>Data zamówienia:</strong> {{ formatDate(selectedOrder.date) }}</p>
            <p class="mb-2"><strong>Status:</strong> {{ selectedOrder.status }}</p>
            <p class="mb-4"><strong>Łączna kwota:</strong> {{ selectedOrder.total }} PLN</p>

            <h2 class="text-2xl font-bold mb-4">Przedmioty w zamówieniu:</h2>
            <ul>
              <li v-for="item in selectedOrder.items" :key="item.id">
                <p><strong>Produkt:</strong> {{ item.name }}  <strong>Ilość:</strong> {{ item.quantity }}    <strong>Cena:</strong>  {{ item.price }}</p>
              </li>
            </ul>
          </div>

          <button @click="closeModal" class="mt-4 bg-blue-500 text-white p-2 rounded">Zamknij</button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import { ref, reactive, onMounted } from "vue";
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL;
const userStore = useUserStore();
const userId = userStore.id;
console.log('User ID:', userId);

const orders = reactive([]);


const isModalOpen = ref(false);
const selectedOrder = reactive({
  date: "",
  status: "",
  total: "",
  items: []
});


const fetchOrders = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/orders/${id}`);
    const orderData = response.data;

    console.log("Order data received:", orderData); 

    orders.length = 0; 

    if (Array.isArray(orderData)) {

      orderData.forEach(order => {
        orders.push({
          date: order.order_date,
          status: order.order_status,
          total: order.total_amount,
          id: order.id,
          items: order.order_items
        });
      });
    } else if (typeof orderData === 'object') {
      orders.push({
        date: orderData.order_date,
        status: orderData.order_status,
        total: orderData.total_amount,
        id: orderData.id,
        items: orderData.order_items
      });
    } else {
      console.log("Unexpected data structure:", orderData);
    }
  } catch (error) {
    console.error('Error fetching orders:', error);
  }
};
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toISOString().split('T')[0];
};

const fetchProductName = async (productId) => {
  try {
    const response = await axios.get(`${API_URL}/products/${productId}`);
    return response.data.product_name; 
  } catch (error) {
    console.error(`Error fetching product name for ID ${productId}:`, error);
    return "Unknown Product"; 
  }
};
const openModal = async (order) => {
  selectedOrder.date = order.date;
  selectedOrder.status = order.status;
  selectedOrder.total = order.total;
  selectedOrder.items = await Promise.all(order.items.map(async (item) => {
    const name = await fetchProductName(item.product_id);
    return {
      name,
      quantity: item.quantity,
      price: item.price
    };
  }));

  console.log("Order items with names:", selectedOrder.items);
  isModalOpen.value = true;
};
const closeModal = () => {
  isModalOpen.value = false;
};

onMounted(() => {
  if (userId) {
    fetchOrders(userId);
  } else {
    console.error("Brak ID użytkownika.");
  }
});
</script>