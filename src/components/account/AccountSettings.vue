<template>
  <div class="max-w-6xl mx-auto p-6 bg-gray-100 rounded-lg shadow-lg">
    <h2 class="text-2xl font-bold mb-6 text-center">Ustawienia konta</h2>


    <div class="flex flex-col md:flex-row gap-8">


      <div class="flex-1">
        <h3 class="text-xl font-semibold mb-4 text-center">Dane użytkownika</h3>
        <div>

          <label class="block text-gray-700 text-sm font-bold mb-2">Imię</label>
          <input v-model="User.firstName" type="text" class="w-full px-4 py-2 bg-gray-200 border border-gray-300 rounded focus:outline-none"
            value="" readonly>

          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Nazwisko</label>
          <input v-model="User.lastName" type="text" class="w-full px-4 py-2 bg-gray-200 border border-gray-300 rounded focus:outline-none"
            value="" readonly>

          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Email</label>
          <input v-model="User.email "type="email" class="w-full px-4 py-2 bg-gray-200 border border-gray-300 rounded focus:outline-none"
            value="" readonly>

            <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Numer telefonu</label>
          <input v-model="User.phone "type="number" class="w-full px-4 py-2  border border-gray-300 rounded focus:outline-none"
            value="">
            <div class="mt-8 flex justify-center"></div>
            <button
                class="px-6 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 focus:outline-none">Zmień
                numer telefonu</button>
        </div>
        
      </div>


      <div class="flex-1">
        <h3 class="text-xl font-semibold mb-4 text-center">Zmień hasło</h3>
        <div>
          <form action="">
            <label class="block text-gray-700 text-sm font-bold mb-2">Stare hasło</label>
            <input type="password" class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
              placeholder="Wpisz stare hasło">

            <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Nowe hasło</label>
            <input type="password" class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
              placeholder="Wpisz nowe hasło">

            <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Powtórz nowe hasło</label>
            <input type="password" class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
              placeholder="Powtórz nowe hasło">
            <div class="mt-8 flex justify-center">
              <button
                class="px-6 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 focus:outline-none">Zmień
                hasło</button>
            </div>
          </form>
        </div>
      </div>





      <div class="flex-1">
        <h3 class="text-xl font-semibold mb-4 text-center">Adres dostawy</h3>
        <form>
          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Kraj</label>
          <input type="text" class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
            placeholder="Wpisz kraj">

          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Miasto</label>
          <input type="text" class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
            placeholder="Wpisz kod pocztowy">


          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Kod pocztowy</label>
          <input type="text" class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
            placeholder="Wpisz ulicę">

          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Ulica</label>
          <input type="text" class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
            placeholder="Wpisz numer domu">

          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Numer domu</label>
          <input type="text" class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
            placeholder="Wpisz numer telefonu">
          <div class="mt-8 flex justify-center">
            <button
              class="px-6 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 focus:outline-none">Zapisz
              zmiany</button>
          </div>
        </form>
      </div>
    </div>


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
  street: "",
  houseNumber: "",
  country: "",
  errors: {
    general: '',
  }
});

async function fetchUserById(id) {
  try {
    const response = await axios.get(`${API_URL}/users/${id}`);
    const userData = response.data;


    User.firstName = userData.first_name;
    User.lastName = userData.last_name;
    User.email = userData.email;
    User.phone = userData.phone;
    User.addressid = userData.address_id;
    
    console.log("Dane użytkownika:", userData);
  } catch (error) {
    console.error("Błąd podczas pobierania danych użytkownika:", error);
    User.errors.general = "Nie udało się pobrać danych użytkownika.";
  }
}
async function fetchAddressById(id) {
  try {
    const response = await axios.get(`${API_URL}/address/${id}`);
    const addressData = response.data;


    Address.city = addressData.city;
   
    
    console.log("adres:", addressData);
  } catch (error) {
  }
}

onMounted(() => {
  if (userId) {
    fetchUserById(userId);
  } else {
    console.error("Brak ID użytkownika.");
    User.errors.general = "ID użytkownika jest wymagane do pobrania danych.";
  }
});
</script>