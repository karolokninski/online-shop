<template>
  <div class="text-black">
    <h1 class="text-4xl font-bold mb-8">Użytkownicy</h1>
    <div>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Imię</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Nazwisko</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Email</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider">Rola</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase tracking-wider">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="user in users" :key="user.id" class="hover:bg-gray-100 transition duration-200">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ user.firstName }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ user.lastName }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">{{ user.email }}</td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span :class="user.role === 'admin' ? 'bg-blue-100 text-blue-800' : user.role === 'pracownik' ? 'bg-yellow-100 text-yellow-800' : 'bg-green-100 text-green-800'" class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                {{ user.role.charAt(0).toUpperCase() + user.role.slice(1) }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button @click="editUser(user.id)" class="text-indigo-600 hover:text-indigo-900 mr-3">
                Edytuj
              </button>
              <button @click="deleteUser(user.id)" class="text-red-600 hover:text-red-900">
                Usuń
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <button @click="addUserOpen = true" class="mt-4 inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
        Dodaj użytkownika
      </button>
    </div>
  </div>

  <TransitionRoot as="template" :show="addUserOpen">
    <Dialog class="relative z-10" @close="addUserOpen = false">
      <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
        leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="template" enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel
              class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                <div class="sm:flex sm:items-start">
                  <div
                    class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                    <PlusCircleIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                  </div>
                  <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                    <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Dodaj użytkownika
                    </DialogTitle>
                    <div class="mt-2">
                      <p class="text-sm text-gray-500">
                        Upewnij się, że wszystkie pola są wypełnione.
                      </p>

                      <form method="POST" onsubmit="return false">
                        <div class="border-b border-gray-900/10 pb-8">
                          <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">

                            <div class="sm:col-span-3">
                              <label for="firstName"
                                class="block text-sm font-medium leading-6 text-gray-900">Imię</label>
                              <div class="mt-2">
                                <input v-model="firstName" type="text" name="firstName" id="firstName"
                                  autocomplete="given-name"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>

                            <div class="sm:col-span-3">
                              <label for="lastName"
                                class="block text-sm font-medium leading-6 text-gray-900">Nazwisko</label>
                              <div class="mt-2">
                                <input v-model="lastName" type="text" name="lastName" id="lastName"
                                  autocomplete="family-name"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>

                            <div class="sm:col-span-3">
                              <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
                              <div class="mt-2">
                                <input v-model="email" type="email" name="email" id="email" autocomplete="email"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>

                            <div class="sm:col-span-3">
                              <label for="password"
                                class="block text-sm font-medium leading-6 text-gray-900">Hasło</label>
                              <div class="mt-2">
                                <input v-model="password" type="password" name="password" id="password"
                                  autocomplete="new-password"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                              </div>
                            </div>

                            <div class="sm:col-span-3">
                              <label for="role" class="block text-sm font-medium leading-6 text-gray-900">Rola</label>
                              <div class="mt-2">
                                <select v-model="role" name="role" id="role"
                                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                  <option value="admin">Admin</option>
                                  <option value="pracownik">Pracownik</option>
                                  <option value="zwykly">Zwykły</option>
                                </select>
                              </div>
                            </div>

                          </div>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
              <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                <button type="button"
                  class="inline-flex w-full justify-center rounded-md bg-primary-500 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-primary-600 sm:ml-3 sm:w-auto"
                  @click="handleAddButton">
                  Dodaj
                </button>
                <button type="button"
                  class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                  @click="addUserOpen = false" ref="cancelButtonRef">
                  Anuluj
                </button>
              </div>
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
import { PlusCircleIcon } from "@heroicons/vue/24/outline";

const API_URL = import.meta.env.VITE_API_URL;
const addUserOpen = ref(false);
const firstName = ref("");
const lastName = ref("");
const email = ref("");
const password = ref("");
const role = ref("zwykly");
const users = ref([]);

const handleAddButton = () => {
  const newUser = {
    id: users.value.length + 1,
    firstName: firstName.value,
    lastName: lastName.value,
    email: email.value,
    role: role.value,
  };
  users.value.push(newUser);
  addUserOpen.value = false;
  console.log("Dodano użytkownika:", newUser);
};

const editUser = (id) => {
  console.log("Edytuj użytkownika o id:", id);
};

const deleteUser = (id) => {
  users.value = users.value.filter(user => user.id !== id);
  console.log("Usunięto użytkownika o id:", id);
};

const fetchUsers = async () => {
  try {
    const response = await axios.get(API_URL + '/users')
    users.value = response.data.map((user) => ({
      ...user,
      firstName: user.first_name,
      lastName: user.last_name,
    }))
    console.log(users.value)
  } catch (error) {
    console.error('Błąd podczas pobierania użytkowników:', error)
  }
}

onMounted(fetchUsers);
</script>
