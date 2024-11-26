<template>
  <div class="flex flex-col gap-8 w-full max-w-7xl mx-auto mb-2 px-4 py-6 sm:px-6 lg:px-8">
    <LogoButton></LogoButton>
    <h1 class="text-4xl font-bold text-gray-900 text-center">Zamówienie</h1>
    <div class="w-full flex flex-col">
      <div class="mt-6 overflow-hidden border border-gray-200 rounded-lg bg-white shadow-md">
        <ul role="list" class="divide-y divide-gray-200">
          <li v-for="product in shoppingCartStore.products" :key="product.id" class="flex py-6 px-4">
            <div class="h-24 w-24 flex-shrink-0 overflow-hidden rounded-md border border-gray-200">
              <img v-if="product.imageSrc" :src="product.imageSrc" :alt="product.imageAlt"
                class="h-full w-full object-cover object-center" />
              <PhotoIcon v-else class="p-6 rounded-md object-cover text-gray-300" aria-hidden="true" />
            </div>
            <div class="ml-4 flex flex-1 flex-col">
              <div>
                <div class="flex justify-between text-base font-medium text-gray-900">
                  <h3>
                    <RouterLink :to="`/produkt/${product.id}`">{{ product.name }}</RouterLink>
                  </h3>
                  <p class="ml-4">{{ product.totalPrice }} PLN</p>
                </div>
                <p class="mt-1 text-sm text-gray-500">{{ product.color }}</p>
                <p v-if="product.quantity > 1" class="text-xs text-gray-500">
                  za szt. {{ product.price }} PLN
                </p>
              </div>
              <div class="flex flex-1 items-end justify-between text-sm">
                <div class="flex">
                  <select v-if="product.quantity < 5 && product.quantity >= 1" v-model="product.quantity"
                    @change="handleQuantityChange(product.id)"
                    class="rounded-md border-gray-300 bg-transparent py-1 pr-7 text-gray-500 focus:ring-2 focus:ring-indigo-600 sm:text-sm">
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                    <option value="5">5+</option>
                  </select>
                  <input v-else type="number" v-model.lazy="product.quantity"
                    @change="handleQuantityChange(product.id)"
                    class="ml-2 rounded-md border-gray-300 bg-transparent py-1 w-16 text-gray-500 focus:ring-2 focus:ring-indigo-600 sm:text-sm" />
                </div>
                <button type="button" @click="shoppingCartStore.removeProduct(product.id)"
                  class="font-medium text-indigo-600 hover:text-indigo-500">
                  Usuń
                </button>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>

    <div class="flex flex-col md:flex-row gap-4">
      <div class="flex flex-col w-full">
        <div class="bg-white shadow-md rounded-md p-6">
          <h2 class="text-xl font-semibold text-gray-900">Dane do wysyłki</h2>
          <form @submit.prevent class="mt-4 space-y-4">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700">Imię i nazwisko</label>
              <input type="text" id="name" name="name" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
            </div>
            <div>
              <label for="phone" class="block text-sm font-medium text-gray-700">Numer telefonu</label>
              <input type="tel" id="phone" name="phone" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
            </div>
            <div>
              <label for="city" class="block text-sm font-medium text-gray-700">Kraj</label>
              <input type="text" id="country" name="city" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
            </div>
            <div>
              <label for="city" class="block text-sm font-medium text-gray-700">Kod pocztowy</label>
              <input type="text" id="postalCode" name="city" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
            </div>
            <div>
              <label for="city" class="block text-sm font-medium text-gray-700">Miasto</label>
              <input type="text" id="city" name="city" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
            </div>
            <div>
              <label for="address" class="block text-sm font-medium text-gray-700">Adres</label>
              <input type="text" id="addressLine" name="address" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
            </div>
          </form>
          <div v-if="errors.address" class="text-red-500 text-sm mt-2">
          {{ errors.address }}
        </div>
          <div v-if="Address.city && Address.postalCode && Address.addressLine && Address.country">
      <div class="bg-white shadow-lg rounded-md p-6">
        <div class="flex items-center space-x-3">
          <input
            type="checkbox"
            id="use-address"
            class="h-5 w-5 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
          />
          <label for="use-address" class="text-sm font-medium text-gray-700">
            <span>Użyj twojego adresu:</span>
            <span class="font-semibold">
              <br />{{ Address.addressLine }}
              <br />{{ Address.city }}
              <br />{{ Address.country }}
            </span>
          </label>
        </div>
      </div>
    </div>
        </div>
      </div>

      <div class="flex flex-col w-full ">
        <div class="bg-white shadow-md rounded-md p-6">
          <h2 class="text-xl font-semibold text-gray-900 mb-4">Opcje dostawy</h2>
          <div class="space-y-4">
            <div v-for="provider in providers" :key="provider.id" class="flex items-center">
              <input type="radio" :id="'provider-' + provider.id" name="delivery-provider" :value="provider"
                v-model="selectedProvider" class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300" />
              <label :for="'provider-' + provider.id" class="ml-3 text-sm text-gray-700">
                {{ provider.name }} ({{ provider.cost }} PLN, {{ provider.estimated_delivery_days }} dni)
              </label>
            </div>
          </div>
        </div>

        <div class="mt-6 bg-white shadow-md rounded-md p-6">
          <h2 class="text-xl font-semibold text-gray-900 mb-4">Sposób płatności</h2>
          <div class="space-y-4">
            <div v-for="method in paymentMethods" :key="method.method_name" class="flex items-center">
              <input type="radio" :id="'method-' + method.method_name" name="payment-method" :value="method"
                v-model="selectedMethod" class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300" />
              <label :for="'provider-' + method.id" class="ml-3 text-sm text-gray-700">
                {{ method.method_name }} ({{ method.fee }} PLN)
              </label>
            </div>
          </div>
        </div>

        <div v-if="errors.methods" class="text-red-500 text-sm mt-2">
          {{ errors.methods }}
        </div>

        <div class="mt-6 bg-white shadow-md rounded-md p-6">
          <div class="flex justify-between text-base font-medium text-gray-900">
            <p>Do zapłaty</p>
            <p>{{ total }} PLN</p>
          </div>
          <div class="mt-6">
            <button
              class="flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-base font-medium text-white shadow-sm hover:bg-indigo-700"
              @click="handlePayment">
              <b>Płatność</b>
            </button>
          </div>
          <div class="mt-6 flex justify-center text-center text-sm text-gray-500">
            <button type="button" class="font-medium text-indigo-600 hover:text-indigo-500"
              @click="shoppingCartStore.open = false">Kontynuuj zakupy</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script setup>
import LogoButton from '@/components/LogoButton.vue';
import { onMounted, watch, ref, reactive, computed} from 'vue'
import { useRouter } from 'vue-router'
import { useShoppingCartStore } from '@/stores/shoppingCart'
import { useUserStore } from '@/stores/user';
import axios from 'axios';
const API_URL = import.meta.env.VITE_API_URL;
const showModal = ref(false);
const userStore = useUserStore();
const userId = userStore.id;
const shoppingCartStore = useShoppingCartStore();
const paymentMethods = ref([]);
const selectedProvider = ref(null);
const selectedMethod = ref(null);
console.log('User ID:', userId);
console.log(paymentMethods);

const total = computed(() => {
  const productsCost = shoppingCartStore.products.reduce((total, product) => {
    return total + product.quantity * product.price;
  }, 0);

  const deliveryCost = selectedProvider.value?.cost || 0;
  const paymentFee = selectedMethod.value?.fee || 0;

  return (productsCost + deliveryCost + paymentFee).toFixed(2);
});

const User = reactive({
  firstName: "",
  lastName: "",
  email: "",
  phone: "",
  addressid: "",
  errors: {
    general: '',
  }
});
const Address = reactive({
  city: "",
  postalCode: "",
  addressLine: "",
  country: "",
  errors: {
    general: '',
  }
});
const newAddress = reactive({
  city: "",
  postalCode: "",
  addressLine: "",
  country: "",
  phone: "",
  errors: {
    general: '',
  }
});
const providers = ref([]);
const errors = reactive({
  address: '',
  methods: '',
});
const router = useRouter()

const handlePayment = async () => {
  if (validateForm) {
    const response = await axios.post(`${API_URL}/transactions`, {
      amount: total.value,
      description: "zamówienie w sklepie Geeked.tech",
      payer_email: "Tutaj_dane_z@formularza.pl",
      payer_name: "Tutaj dane z formularza"
    });
    console.log(response.data)
    if (response.data.transaction_url) {
      window.location.href = response.data.transaction_url;
    } else {
      console.error("Błąd podczas tworzenia płatności tpay.");
    }
  }
};
const validateForm = () => {
  newAddress.phone=document.getElementById('phone').value
  newAddress.city=document.getElementById('city').value
  newAddress.postalCode=document.getElementById('postalCode').value
  newAddress.addressLine=document.getElementById('addressLine').value
  newAddress.country=document.getElementById('country').value
  newAddress.name=document.getElementById('name').value
  if (!document.querySelector("#use-address").checked&&(newAddress.phone==""||newAddress.city==""|| newAddress.addressLine==""|| newAddress.postalCode==""||newAddress.country==""||newAddress.name=="")) {
    errors.address = "Upewnij się, że wypełniłeś formularz adresu";
    return false;
  }
  if (!selectedProvider.value || !selectedMethod.value) {
    errors.methods = "Wybierz dostawę i sposób płatności";
    return false;
  }
  else {
    errors.address = '';
    return true;
  }

};
const fetchPaymentMethods = async () => {
  try {
    const response = await axios.get(API_URL + "/payment-methods/");
    paymentMethods.value = response.data;
  } catch (error) {
    console.error("Error fetching payment methods:", error);
  }
};

const saveAddress = async () => {
  try {
   await axios.put(`${API_URL}/users/${userId}`, {
    phone: newAddress.phone,
  });
  if (User.addressid == null) {

 await axios.post(`${API_URL}/addresses/?user_id=${userId}`, {
  city: newAddress.city,
  address_line: newAddress.addressLine,
  postal_code: newAddress.postalCode,
  country: newAddress.country,
});

await fetchUserById(userId);
if (User.addressid) {
  await fetchAddressById(User.addressid);
}
} else {

await axios.put(`${API_URL}/addresses/${User.addressid}`, {
  city: newAddress.city,
  address_line: newAddress.addressLine,
  postal_code: newAddress.postalCode,
  country: newAddress.country,
});
}

    alert('Adres został zapisany!');
  } catch (error) {
    console.error('Błąd podczas zapisywania adresu:', error);
    alert('Nie udało się zapisać adresu.');
  } finally {
    closeModal();
  }
  //instrukcje
};
const fetchProviders = async () => {
  try {
    const response = await axios.get(API_URL + "/delivery-methods/");
    providers.value = response.data.map(provider => ({
      id: provider.id,
      name: provider.method_name,
      cost: provider.cost,
      estimated_delivery_days: provider.estimated_delivery_days,
    }));
  } catch (error) {
    console.error("Błąd podczas pobierania dostawców:", error);
  }
};
const handleQuantityChange = (id) => {
  const product = shoppingCartStore.products.find(product => product.id == id)

  if (product.quantity < 1) {
    product.quantity = 1
  } else if (product.quantity > 99) {
    console.log("Brak w magazynie.")

  }

  shoppingCartStore.updateQuantity()
  total = shoppingCartStore.productsSum();

}
const checkCartAndRedirect = () => {
  if (shoppingCartStore.products.length === 0) {
    router.back()
  }
}
async function fetchUserById(id) {
  try {
    const response = await axios.get(`${API_URL}/users/${id}`);
    const userData = response.data;


    User.firstName = userData.first_name;
    User.lastName = userData.last_name;
    User.email = userData.email;
    User.phone = userData.phone;
    User.addressid = userData.address_id;


  } catch (error) {
    console.error("Błąd podczas pobierania danych użytkownika:", error);
    User.errors.general = "Nie udało się pobrać danych użytkownika.";
  }
}
async function fetchAddressById(id) {
  try {
    const response = await axios.get(`${API_URL}/addresses/${id}`);
    const addressData = response.data;

    Address.city = addressData.city;
    Address.postalCode = addressData.postal_code;
    Address.addressLine = addressData.address_line;
    Address.country = addressData.country;

  } catch (error) {
    console.error("Błąd podczas pobierania adresu:", error);
  }
}

onMounted(async () => {
  checkCartAndRedirect();
  fetchProviders();
  fetchPaymentMethods();
  if (userId) {
    await fetchUserById(userId);

    if (User.addressid) {
      fetchAddressById(User.addressid);
    } else {
      console.error("Brak adresu dla użytkownika.");
    }
  } else {
    console.error("Brak ID użytkownika.");
    User.errors.general = "ID użytkownika jest wymagane do pobrania danych.";
  }
})

watch(() => shoppingCartStore.products, () => {
  checkCartAndRedirect();
})
</script>