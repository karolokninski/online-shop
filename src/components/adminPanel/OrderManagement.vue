<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Zamówienia</h1>
    <div>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">ID</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">User Name</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Order Date</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Delivery Method</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Payment Method</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Total Amount</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Status</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Produkty</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Actions</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="order in orders" :key="order.id" class="hover:bg-gray-100 transition duration-200">
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm font-medium text-gray-900">{{ order.id }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">
                {{ users.find(user => user.id === order.user_id)?.first_name }} {{ users.find(user => user.id === order.user_id)?.last_name }}
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ new Date(order.order_date).toLocaleDateString() }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">
                {{ deliveryMethods.find(method => method.id === order.delivery_method_id)?.method_name }}
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">
                {{ paymentMethods.find(method => method.id === order.payment_method_id)?.method_name }}
              </div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ order.total_amount.toFixed(2) }} PLN</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">{{ order.order_status }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <table class="min-w-full bg-gray-100 mt-4 rounded-lg shadow-lg overflow-hidden">
                <thead class="bg-indigo-200 text-gray-900">
                  <tr>
                    <th class="px-4 py-2 text-left text-xs font-medium uppercase tracking-wider">Product ID</th>
                    <th class="px-4 py-2 text-left text-xs font-medium uppercase tracking-wider">Quantity</th>
                    <th class="px-4 py-2 text-left text-xs font-medium uppercase tracking-wider">Price</th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="item in order.order_items" :key="item.id">
                    <td class="px-4 py-2 whitespace-nowrap text-sm text-gray-900">{{ item.product_id }}</td>
                    <td class="px-4 py-2 whitespace-nowrap text-sm text-gray-900">{{ item.quantity }}</td>
                    <td class="px-4 py-2 whitespace-nowrap text-sm text-gray-900">{{ (item.price * item.quantity).toFixed(2) }} PLN</td>
                  </tr>
                </tbody>
              </table>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="openEditOrderModal(order)" class="text-indigo-600 hover:text-indigo-900">
                <PencilSquareIcon class="h-5 w-5 inline-block" aria-hidden="true" />
              </button>
              <button @click="openDeleteOrderModal(order)" class="text-red-600 hover:text-red-900 ml-2">
                <TrashIcon class="h-5 w-5 inline-block" aria-hidden="true" />
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- Add modal and other components go here -->
  </div>
</template>


<script setup>
import { ref, onMounted } from "vue";
import axios from 'axios';
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from "@headlessui/vue";
import { PencilSquareIcon, TrashIcon } from "@heroicons/vue/24/outline";

const API_URL = import.meta.env.VITE_API_URL;
const addOrderOpen = ref(false);
const editOrderOpen = ref(false);
const deleteOrderOpen = ref(false);
const currentEditId = ref(null);
const currentDeleteId = ref(null);
const currentDeleteName = ref("");
const orders = ref([]);
const deliveryMethods = ref([]);
const paymentMethods = ref([]);
const users = ref([]);

const form = ref({
  add: {
    user_id: "",
    delivery_method_id: "",
    payment_method_id: "",
    total_amount: "",
    address: {
      address_line: "",
      postal_code: "",
      city: "",
      country: "",
    },
    errors: {},
  },
  edit: {
    id: null,
    user_id: "",
    delivery_method_id: "",
    payment_method_id: "",
    total_amount: "",
    address: {
      address_line: "",
      postal_code: "",
      city: "",
      country: "",
    },
    errors: {},
  }
});

// Validation function
const validateForm = (type) => {
  const formInstance = form.value[type];
  const errors = {};

  if (!formInstance.user_id) errors.user_id = 'User ID is required';
  if (!formInstance.delivery_method_id) errors.delivery_method_id = 'Delivery method ID is required';
  if (!formInstance.payment_method_id) errors.payment_method_id = 'Payment method ID is required';
  if (!formInstance.total_amount) errors.total_amount = 'Total amount is required';
  if (!formInstance.address.address_line) errors.address.address_line = 'Address line is required';
  if (!formInstance.address.postal_code) errors.address.postal_code = 'Postal code is required';
  if (!formInstance.address.city) errors.address.city = 'City is required';
  if (!formInstance.address.country) errors.address.country = 'Country is required';

  formInstance.errors = errors;
  return Object.keys(errors).length === 0;
}

// Fetch orders from API
const fetchOrders = async () => {
  try {
    const response = await axios.get(`${API_URL}/orders`);
    orders.value = response.data;
  } catch (error) {
    console.error('Error fetching orders:', error);
  }
}

// Fetch delivery methods
const fetchDeliveryMethods = async () => { 
  try {
    const response = await axios.get(`${API_URL}/delivery-methods/`);
    deliveryMethods.value = response.data;
  } catch (error) {
    console.error("Error fetching delivery methods:", error);
  }
};

// Fetch payment methods
const fetchPaymentMethods = async () => {
  try {
    const response = await axios.get(`${API_URL}/payment-methods/`);
    paymentMethods.value = response.data;
  } catch (error) {
    console.error("Error fetching payment methods:", error);
  }
};

// Fetch users
const fetchUsers = async () => {
  try {
    const response = await axios.get(`${API_URL}/users/`);
    users.value = response.data;
  } catch (error) {
    console.error("Error fetching users:", error);
  }
};

// Open modals
const openAddOrderModal = () => {
  addOrderOpen.value = true;
  resetAddForm();
}

const openEditOrderModal = (order) => {
  currentEditId.value = order.id;
  form.value.edit.user_id = order.user_id;
  form.value.edit.delivery_method_id = order.delivery_method_id;
  form.value.edit.payment_method_id = order.payment_method_id;
  form.value.edit.total_amount = order.total_amount;
  form.value.edit.address = { ...order.address };
  editOrderOpen.value = true;
}

const openDeleteOrderModal = (order) => {
  currentDeleteId.value = order.id;
  currentDeleteName.value = order.address.city; // or any other identifier
  deleteOrderOpen.value = true;
}

// Add Order
const submitAddOrder = async () => {
  if (validateForm('add')) {
    try {
      await axios.post(`${API_URL}/orders`, {
        user_id: form.value.add.user_id,
        delivery_method_id: form.value.add.delivery_method_id,
        payment_method_id: form.value.add.payment_method_id,
        total_amount: form.value.add.total_amount,
        address: form.value.add.address,
      });
      await fetchOrders();
      addOrderOpen.value = false;
    } catch (error) {
      console.error('Error adding order:', error);
    }
  }
}

// Edit Order
const submitEditOrder = async () => {
  if (validateForm('edit')) {
    try {
      await axios.put(`${API_URL}/orders/${currentEditId.value}`, {
        user_id: form.value.edit.user_id,
        delivery_method_id: form.value.edit.delivery_method_id,
        payment_method_id: form.value.edit.payment_method_id,
        total_amount: form.value.edit.total_amount,
        address: form.value.edit.address,
      });
      await fetchOrders();
      editOrderOpen.value = false;
    } catch (error) {
      console.error('Error editing order:', error);
    }
  }
}

// Delete Order
const submitDeleteOrder = async () => {
  try {
    await axios.delete(`${API_URL}/orders/${currentDeleteId.value}`);
    await fetchOrders();
    deleteOrderOpen.value = false;
  } catch (error) {
    console.error('Error deleting order:', error);
  }
}

// Reset form data
const resetAddForm = () => {
  form.value.add = {
    user_id: "",
    delivery_method_id: "",
    payment_method_id: "",
    total_amount: "",
    address: {
      address_line: "",
      postal_code: "",
      city: "",
      country: "",
    },
    errors: {},
  };
}

// On mounted fetch all necessary data
onMounted(() => {
  fetchOrders();
  fetchDeliveryMethods();
  fetchPaymentMethods();
  fetchUsers();
});
</script>
