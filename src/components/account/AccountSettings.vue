<template>
  <div class="max-w-6xl mx-auto p-6 bg-gray-100 rounded-lg shadow-lg text-gray-900">
    <h2 class="text-2xl font-bold mb-6 text-center">Ustawienia konta</h2>

    <div class="flex flex-col md:flex-row gap-8">
      <div class="flex-1">
        <h3 class="text-xl font-semibold mb-4 text-center">Dane użytkownika</h3>
        <div>
          <form @submit.prevent="savePhone">
            <label class="block text-gray-700 text-sm font-bold mb-2">Imię</label>
            <input v-model="User.firstName" type="text"
              class="w-full px-4 py-2 bg-gray-200 border border-gray-300 rounded focus:outline-none" value="" readonly>

            <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Nazwisko</label>
            <input v-model="User.lastName" type="text"
              class="w-full px-4 py-2 bg-gray-200 border border-gray-300 rounded focus:outline-none" value="" readonly>

            <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Email</label>
            <input v-model="User.email" type="email"
              class="w-full px-4 py-2 bg-gray-200 border border-gray-300 rounded focus:outline-none" value="" readonly>

            <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Numer telefonu</label>
            <input v-model="User.phone" type="text"
              class="w-full px-4 py-2  border border-gray-300 rounded focus:outline-none" value="">
            <div class="mt-8 flex justify-center"></div>

            <button type="submit"
              class="px-6 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 focus:outline-none">Zmień
              numer telefonu</button>
          </form>


          <div v-if="User.errors.general" class="mt-4 text-red-500 text-center">
            {{ User.errors.general }}
          </div>
        </div>
      </div>


      <div class="flex-1">
        <h3 class="text-xl font-semibold mb-4 text-center">Zmień hasło</h3>
        <div>
          <form @submit.prevent="changePassword">
            <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Nowe hasło</label>
            <input v-model="Password.newPassword" type="password"
              class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
              placeholder="Wpisz nowe hasło">

            <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Powtórz nowe hasło</label>
            <input v-model="Password.confirmNewPassword" type="password"
              class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
              placeholder="Powtórz nowe hasło">

            <div class="mt-8 flex justify-center">
              <button type="submit"
                class="px-6 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 focus:outline-none">
                Zmień hasło
              </button>
            </div>

            <div v-if="Password.errors.general" class="mt-4 text-red-500 text-center">
              {{ Password.errors.general }}
            </div>
          </form>
        </div>
      </div>





      <div class="flex-1">
        <h3 class="text-xl font-semibold mb-4 text-center">Adres dostawy</h3>
        <form @submit.prevent="saveAddress">
          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Kraj</label>
          <input v-model="Address.country" type="text"
            class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
            placeholder="Wpisz kraj">

          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Miasto</label>
          <input v-model="Address.city" type="text"
            class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
            placeholder="Wpisz miasto">

          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Kod pocztowy</label>
          <input v-model="Address.postalCode" type="text"
            class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
            placeholder="Wpisz kod pocztowy">

          <label class="block text-gray-700 text-sm font-bold mt-4 mb-2">Ulica i nr domu</label>
          <input v-model="Address.addressLine" type="text"
            class="w-full px-4 py-2 bg-white border border-gray-300 rounded focus:outline-none"
            placeholder="Wpisz ulicę">

          <div class="mt-8 flex justify-center">
            <button type="submit"
              class="px-6 py-2 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 focus:outline-none">
              Zapisz zmiany
            </button>
          </div>

          <div v-if="Address.errors.general" class="mt-4 text-red-500 text-center">
            {{ Address.errors.general }}
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
  addressLine: "",
  country: "",
  errors: {
    general: '',
  }
});
const Password = reactive({
  newPassword: "",
  confirmNewPassword: "",
  errors: {
    general: '',
  },
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

async function saveAddress() {
  if (!Address.city || !Address.postalCode || !Address.addressLine || !Address.country) {
    Address.errors.general = "Wszystkie pola są wymagane.";
    return;
  }

  try {
    if (User.addressid == null) {

      const response = await axios.post(`${API_URL}/addresses/?user_id=${userId}`, {
        city: Address.city,
        address_line: Address.addressLine,
        postal_code: Address.postalCode,
        country: Address.country,
      });

      await fetchUserById(userId);
      if (User.addressid) {
        await fetchAddressById(User.addressid);
      }
    } else {

      const response = await axios.put(`${API_URL}/addresses/${User.addressid}`, {
        city: Address.city,
        postal_code: Address.postalCode,
        address_line: Address.addressLine,
        country: Address.country,
      });

      if (response.status === 200) {
        console.log("Adres został zaktualizowany");
        await fetchAddressById(User.addressid);
        Address.errors.general = "Adres zaktualizowany pomyślnie."
      }
    }
  } catch (error) {
    console.error("Błąd podczas zapisywania adresu:", error);
    Address.errors.general = "Nie udało się zapisać adresu.";
  }
}
async function savePhone() {
  if (!User.phone) {
    User.errors.general = "Wypełnij puste pole.";
    return;
  }
  const response = await axios.put(`${API_URL}/users/${userId}`, {
    phone: User.phone,
  });

  if (response.status === 200) {
    console.log("telefon został zaktualizowany");
    Address.errors.general = "Nr telefonu zaktualizowany pomyślnie."
    await fetchUserById(userId);
  }
}
async function changePassword() {
  if (!Password.newPassword || !Password.confirmNewPassword) {
    Password.errors.general = "Wszystkie pola są wymagane.";
    return;
  }

  if (Password.newPassword !== Password.confirmNewPassword) {
    Password.errors.general = "Hasła muszą być identyczne.";
    return;
  }

  try {
    const response = await axios.post(`${API_URL}/change-password`, {
      email: User.email,
      password: Password.newPassword,
    });

    if (response.status === 200) {
      Password.errors.general = "Hasło zostało zmienione pomyślnie.";
    }
  } catch (error) {
    console.error("Błąd podczas zmiany hasła:", error);
  }
}

onMounted(async () => {
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
});
</script>