<template>
  <div class="flex flex-row justify-around gap-16 mt-8">
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
              <button @click="openEditProviderModal(provider)" class="text-indigo-600 mr-2">Edytuj</button>
              <button @click="openDeleteProviderModal(provider.id)" class="text-red-600">Usuń</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="mt-4">
        <div class="flex space-x-2">
          <input v-model="newProviderName" type="text" placeholder="Nazwa dostawcy"
            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          <button class="bg-indigo-600 text-white px-4 py-2 rounded" @click="addProvider">Dodaj dostawcę</button>
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
              <button @click="openEditPaymentMethodModal(paymentMethod)" class="text-indigo-600 mr-2">Edytuj</button>
              <button @click="openDeletePaymentMethodModal(paymentMethod.id)" class="text-red-600">Usuń</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="mt-4">
        <div class="flex space-x-2">
          <input v-model="newPaymentMethodName" type="text" placeholder="Nazwa formy płatności"
            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          <button class="bg-indigo-600 text-white px-4 py-2 rounded" @click="addPaymentMethod">Dodaj formę płatności</button>
        </div>
      </div>
    </div>

    <!-- Modal Edytuj Dostawcę -->
    <TransitionRoot as="div" :show="editProviderOpen" @close="editProviderOpen = false">
      <Dialog as="div" class="relative z-10">
        <TransitionChild
          as="div"
          enter="ease-out duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in duration-200"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-center justify-center p-4 text-center">
            <TransitionChild
              as="div"
              enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100"
              leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            >
              <DialogPanel class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:max-w-lg">
                <form @submit.prevent="submitEditProvider">
                  <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                    <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Edytuj Dostawcę</DialogTitle>
                    <div class="mt-2">
                      <input v-model="editProviderName" type="text" placeholder="Nazwa dostawcy"
                        class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                      <p v-if="providerError" class="text-red-500 text-xs mt-1">{{ providerError }}</p>
                    </div>
                  </div>
                  <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                    <button type="submit" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-700 sm:ml-3 sm:w-auto">Zapisz</button>
                    <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="editProviderOpen = false">Anuluj</button>
                  </div>
                </form>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <!-- Modal Edytuj Formę Płatności -->
    <TransitionRoot as="div" :show="editPaymentMethodOpen" @close="editPaymentMethodOpen = false">
      <Dialog as="div" class="relative z-10">
        <TransitionChild
          as="div"
          enter="ease-out duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in duration-200"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-center justify-center p-4 text-center">
            <TransitionChild
              as="div"
              enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100"
              leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            >
              <DialogPanel class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:max-w-lg">
                <form @submit.prevent="submitEditPaymentMethod">
                  <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                    <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Edytuj Formę Płatności</DialogTitle>
                    <div class="mt-2">
                      <input v-model="editPaymentMethodName" type="text" placeholder="Nazwa formy płatności"
                        class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                      <p v-if="paymentMethodError" class="text-red-500 text-xs mt-1">{{ paymentMethodError }}</p>
                    </div>
                  </div>
                  <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                    <button type="submit" class="inline-flex w-full justify-center rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-700 sm:ml-3 sm:w-auto">Zapisz</button>
                    <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="editPaymentMethodOpen = false">Anuluj</button>
                  </div>
                </form>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <!-- Modal Potwierdzenia Usunięcia -->
    <TransitionRoot as="div" :show="deleteConfirmationOpen" @close="deleteConfirmationOpen = false">
      <Dialog as="div" class="relative z-10">
        <TransitionChild
          as="div"
          enter="ease-out duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="ease-in duration-200"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>
        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-center justify-center p-4 text-center">
            <TransitionChild
              as="div"
              enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100"
              leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            >
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
                    <h3 class="text-base font-semibold leading-6 text-gray-900" id="modal-title">Usuń Element</h3>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">Czy na pewno chcesz usunąć ten element? Ta czynność jest nieodwracalna.</p>
                    </div>
                  </div>
                </div>
              </div>
                <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                  <button @click="deleteProvider" class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-700 sm:ml-3 sm:w-auto">Usuń</button>
                  <button type="button" class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto" @click="deleteConfirmationOpen = false">Anuluj</button>
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
import { ref } from "vue";
import { Dialog, TransitionRoot, TransitionChild } from '@headlessui/vue';

const addProviderOpen = ref(false);
const addPaymentMethodOpen = ref(false);
const editProviderOpen = ref(false);
const editPaymentMethodOpen = ref(false);
const deleteConfirmationOpen = ref(false);
const providers = ref([{ id: 1, name: "InPost" }, { id: 2, name: "DHL" }]);
const paymentMethods = ref([{ id: 1, name: "Przelewy24" }, { id: 2, name: "PayU" }]);
const newProviderName = ref('');
const newPaymentMethodName = ref('');
const editProviderName = ref('');
const editPaymentMethodName = ref('');
const providerError = ref('');
const paymentMethodError = ref('');
const currentProviderId = ref(null);
const currentPaymentMethodId = ref(null);

const addProvider = () => {
  if (newProviderName.value.trim() === '') {
    providerError.value = 'Nazwa dostawcy nie może być pusta';
    return;
  }
  providers.value.push({ id: providers.value.length + 1, name: newProviderName.value });
  newProviderName.value = '';
  providerError.value = '';
};

const addPaymentMethod = () => {
  if (newPaymentMethodName.value.trim() === '') {
    paymentMethodError.value = 'Nazwa formy płatności nie może być pusta';
    return;
  }
  paymentMethods.value.push({ id: paymentMethods.value.length + 1, name: newPaymentMethodName.value });
  newPaymentMethodName.value = '';
  paymentMethodError.value = '';
};

const openEditProviderModal = (provider) => {
  editProviderName.value = provider.name;
  currentProviderId.value = provider.id;
  editProviderOpen.value = true;
};

const submitEditProvider = () => {
  if (editProviderName.value.trim() === '') {
    providerError.value = 'Nazwa dostawcy nie może być pusta';
    return;
  }
  const providerIndex = providers.value.findIndex(p => p.id === currentProviderId.value);
  if (providerIndex !== -1) {
    providers.value[providerIndex].name = editProviderName.value;
  }
  editProviderOpen.value = false;
  editProviderName.value = '';
  providerError.value = '';
};

const openEditPaymentMethodModal = (paymentMethod) => {
  editPaymentMethodName.value = paymentMethod.name;
  currentPaymentMethodId.value = paymentMethod.id;
  editPaymentMethodOpen.value = true;
};

const submitEditPaymentMethod = () => {
  if (editPaymentMethodName.value.trim() === '') {
    paymentMethodError.value = 'Nazwa formy płatności nie może być pusta';
    return;
  }
  const paymentMethodIndex = paymentMethods.value.findIndex(pm => pm.id === currentPaymentMethodId.value);
  if (paymentMethodIndex !== -1) {
    paymentMethods.value[paymentMethodIndex].name = editPaymentMethodName.value;
  }
  editPaymentMethodOpen.value = false;
  editPaymentMethodName.value = '';
  paymentMethodError.value = '';
};

const openDeleteProviderModal = (id) => {
  currentProviderId.value = id;
  deleteConfirmationOpen.value = true;
};

const deleteProvider = () => {
  providers.value = providers.value.filter(provider => provider.id !== currentProviderId.value);
  deleteConfirmationOpen.value = false;
};

const openDeletePaymentMethodModal = (id) => {
  currentPaymentMethodId.value = id;
  deleteConfirmationOpen.value = true;
};

const deletePaymentMethod = () => {
  paymentMethods.value = paymentMethods.value.filter(pm => pm.id !== currentPaymentMethodId.value);
  deleteConfirmationOpen.value = false;
};

</script>
