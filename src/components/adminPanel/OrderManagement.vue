<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Zamówienia</h1>
    <div>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">ID</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Klient</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Data</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Dostawa</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Płatność</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Wartość</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Status</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Produkty</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Akcje</th>
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
            <td v-if="order.order_items.length" class="px-6 py-4 whitespace-nowrap">
              <table class="min-w-full bg-gray-100 mt-4 rounded-lg shadow-lg overflow-hidden">
                <thead class="bg-indigo-200 text-gray-900">
                  <tr>
                    <th class="px-4 py-2 text-left text-xs font-medium uppercase tracking-wider">ID</th>
                    <th class="px-4 py-2 text-left text-xs font-medium uppercase tracking-wider">Ilość</th>
                    <th class="px-4 py-2 text-left text-xs font-medium uppercase tracking-wider">Cena</th>
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
            <td v-else></td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <!--<button @click="openEditOrderModal(order)" class="text-indigo-600 hover:text-indigo-900">
                <PencilSquareIcon class="h-5 w-5 inline-block" aria-hidden="true" />
              </button>-->
              <button @click="openDeleteOrderModal(order)" class="text-red-600 hover:text-red-900 ml-2">
                <TrashIcon class="h-5 w-5 inline-block" aria-hidden="true" />
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>






  <TransitionRoot as="div" :show="deleteOrderOpen" @close="deleteOrderOpen = false">
      <Dialog as="div" class="relative z-10">
        <TransitionChild as="div" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
          leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-center justify-center p-4 text-center">
            <TransitionChild as="div" enter="ease-out duration-300"
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
                      <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Usuń Element</h3>
                      <div class="mt-2">
                        <p class="text-sm text-gray-500">Czy na pewno chcesz usunąć to zamówienie? Ta czynność jest
                          nieodwracalna.</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                  <button @click="submitDeleteOrder"
                    class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-700 sm:ml-3 sm:w-auto">Usuń</button>
                  <button type="button"
                    class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                    @click="deleteOrderOpen = false">Anuluj</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>




    <TransitionRoot as="editSubpage" :show="editOrderOpen">
      <Dialog class="relative z-10" @close="editOrderOpen = false">
        <TransitionChild as="editProvider" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
          leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>

        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="editProvider" enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel
                class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                <form @submit.prevent="submitEditOrder">
                  <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                    <div class="sm:flex sm:items-start">
                      <div
                        class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                        <PencilSquareIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                      </div>
                      <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                        <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Edytuj Zamówienie
                        </DialogTitle>
                        <div class="mt-2">
                          <p class="text-sm text-gray-500">Upewnij się, że wszystkie pola są wypełnione.</p>
                          <div class="border-b border-gray-900/10 pb-8">
                            <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">





                              <div class="sm:col-span-2">
                              <label for="edit-user_id" class="block text-sm font-medium leading-6 text-gray-900">Klient</label>
                              <div class="mt-2">
                                <select v-model="form.edit.user_id" name="edit-user_id" id="edit-user_id"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                  
                                  <option v-for="user in users" :key="user.id" :value="user.id">{{ user.first_name +" "+ user.last_name }}</option>
                                </select>
                                <p v-if="form.edit.errors.user_id" class="text-red-500 text-xs mt-1">{{ form.edit.errors.user_id }}</p>
                              </div>
                            </div>

                      
                            <div class="sm:col-span-2">
                              <label for="edit-delivery_method_id" class="block text-sm font-medium leading-6 text-gray-900">Dostawa</label>
                              <div class="mt-2">
                                <select v-model="form.edit.delivery_method_id" name="edit-delivery_method_id" id="edit-delivery_method_id"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                  
                                  <option v-for="method in deliveryMethods" :key="method.id" :value="method.id">{{ method.method_name }}</option>
                                </select>
                                <p v-if="form.edit.errors.delivery_method_id" class="text-red-500 text-xs mt-1">{{ form.edit.errors.delivery_method_id }}</p>
                              </div>
                            </div>

                          
                            <div class="sm:col-span-2">
                              <label for="edit-payment_method_id" class="block text-sm font-medium leading-6 text-gray-900">Płatność</label>
                              <div class="mt-2">
                                <select v-model="form.edit.payment_method_id" name="edit-payment_method_id" id="edit-payment_method_id"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                  
                                  <option v-for="method in paymentMethods" :key="method.id" :value="method.id">{{ method.method_name }}</option>
                                </select>
                                <p v-if="form.edit.errors.payment_method_id" class="text-red-500 text-xs mt-1">{{ form.edit.errors.payment_method_id }}</p>
                              </div>
                            </div>

                        


                            <div class="sm:col-span-2">
                              <label for="edit-payment_method_id" class="block text-sm font-medium leading-6 text-gray-900">Status</label>
                              <div class="mt-2">
                                <select  name="edit-payment_method_id" id="edit-payment_method_id"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                  
                                  <option value="" disabled selected hidden>Pending</option>
                                  <option>Oczekujące</option>
                                  <option>Wysłane</option>
                                  <option>Dostarczone</option>
                                </select>
                                <p v-if="form.edit.errors.payment_method_id" class="text-red-500 text-xs mt-1">{{ form.edit.errors.order_status }}</p>
                              </div>
                            </div>




                                        <div class="sm:col-span-2">
                                          <label for="edit-total_amount" class="block text-sm font-medium leading-6 text-gray-900">Wartość</label>
                                          <div class="mt-2">
                                            <input v-model="form.edit.total_amount" type="number" step="0.01" name="edit-total_amount" id="edit-total_amount"
                                              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                            <p v-if="form.edit.errors.total_amount" class="text-red-500 text-xs mt-1">{{ form.edit.errors.total_amount }}</p>
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
                      class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-700 sm:ml-3 sm:w-auto">
                      Zapisz
                    </button>
                    <button type="button"
                      class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                      @click="editOrderOpen = false">
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
import { PencilSquareIcon, TrashIcon } from "@heroicons/vue/24/outline";

const API_URL = import.meta.env.VITE_API_URL;
const editOrderOpen = ref(false);
const deleteOrderOpen = ref(false);
const currentEditId = ref(null);
const currentDeleteId = ref(null);
const currentDeleteName = ref("");
const orders = ref([]);
const users = ref([]);
const deliveryMethods = ref([]);
const paymentMethods = ref([]);

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

const fetchOrders = async () => {
  try {
    const response = await axios.get(`${API_URL}/orders`);
    orders.value = response.data;
    console.log(orders.value)
  } catch (error) {
    console.error('Error fetching orders:', error);
  }
}

const fetchDeliveryMethods = async () => { 
  try {
    const response = await axios.get(`${API_URL}/delivery-methods/`);
    deliveryMethods.value = response.data;
    console.log("Fetched users:", deliveryMethods.value); 
  } catch (error) {
    console.error("Error fetching delivery methods:", error);
  }
};

const fetchPaymentMethods = async () => {
  try {
    const response = await axios.get(`${API_URL}/payment-methods/`);
    paymentMethods.value = response.data;
    console.log("Fetched users:", paymentMethods.value); 
  } catch (error) {
    console.error("Error fetching payment methods:", error);
  }
};

const fetchUsers = async () => {
  try {
    const response = await axios.get(`${API_URL}/users/`);
    users.value = response.data;
    console.log("Fetched users:", users.value);
  } catch (error) {
    console.error("Error fetching users:", error);
  }
};


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
  currentDeleteName.value = order.address.city;
  deleteOrderOpen.value = true;
}



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

const submitDeleteOrder = async () => {
  try {
    await axios.delete(`${API_URL}/orders/${currentDeleteId.value}`);
    await fetchOrders();
    deleteOrderOpen.value = false;
  } catch (error) {
    console.error('Error deleting order:', error);
  }
}


onMounted(() => {
  fetchOrders();
  fetchDeliveryMethods();
  fetchPaymentMethods();
  fetchUsers();
});
</script>
