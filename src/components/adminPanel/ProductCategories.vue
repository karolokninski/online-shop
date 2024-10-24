<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Kategorie</h1>
    <div>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Nazwa Kategorii</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="category in categories" :key="category" class="hover:bg-gray-100 transition duration-200">
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm font-medium text-gray-900">{{ category }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="deleteCategory(category)" class="text-red-600 hover:text-red-900">Usuń</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="mt-4">
        <div class="flex space-x-2">
          <input v-model="categoryName" type="text" placeholder="Wpisz nazwę kategorii"
            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
          <button 
            @click="addCategory" 
            class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Dodaj Kategorię
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const categoryName = ref("");
const categories = ref([]);

// Funkcja do dodawania przykładowych kategorii
const addSampleCategories = () => {
  categories.value = ["Procesory", "Karty graficzne", "Obudowy"];
};

// Funkcja do dodawania kategorii
const addCategory = () => {
  if (categoryName.value.trim() !== "") {
    categories.value.push(categoryName.value.trim());
    categoryName.value = ""; // Resetowanie pola
  }
};

// Funkcja do usuwania kategorii
const deleteCategory = (category) => {
  categories.value = categories.value.filter((c) => c !== category);
};

// Dodaj przykładowe kategorie przy załadowaniu komponentu
onMounted(() => {
  addSampleCategories();
});
</script>

<style scoped>
/* Możesz dodać dodatkowe style tutaj, jeśli potrzebujesz */
</style>
