<template>
  <div class="flex flex-row justify-around gap-16 mt-8">

    <div class="text-black">
      <h2 class="text-2xl font-bold mb-4">Dostawcy</h2>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden mb-4">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">ID Dostawcy</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">Dostawca</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">Opis</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase">Czas dostawy (dni)</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">Koszt</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase">Akcje</th>

          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="provider in providers" :key="provider.id" class="hover:bg-gray-100 transition">
            <td class="px-6 py-4">{{ provider.id }}</td>
            <td class="px-6 py-4">{{ provider.name }}</td>
            <td class="px-6 py-4">{{ provider.description }}</td>
            <td class="px-6 py-4 text-center">{{ provider.estimated_delivery_days }}</td>
            <td class="px-6 py-4 text-center">{{ provider.cost }}</td>
            <td class="px-6 py-4 text-right">
              <button @click="openEditProviderModal(provider)" class="text-indigo-600 mr-2"><PencilSquareIcon class="h-5 w-5 inline-block" aria-hidden="true" /></button>
              <button @click="openDeleteProviderModal(provider.id)" class="text-red-600"><TrashIcon class="h-5 w-5 inline-block" aria-hidden="true" /></button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="mt-4">
        <div class="flex space-x-2">
          <button class="bg-indigo-600 text-white px-4 py-2 rounded" @click="addProviderOpen = true">Dodaj
            dostawcę</button>
        </div>
      </div>
    </div>

    <div class="text-black">
      <h2 class="text-2xl font-bold mb-4">Formy Płatności</h2>
      <table class="min-w-full bg-white rounded-lg shadow-lg overflow-hidden mb-4">
        <thead class="bg-indigo-600 text-white">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">ID Formy Płatności</th>
            <th class="px-6 py-3 text-left text-xs font-medium uppercase">Nazwa Formy Płatności</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase">Opis</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase">Opłata</th>
            <th class="px-6 py-3 text-right text-xs font-medium uppercase">Akcje</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="paymentMethod in paymentMethods" :key="paymentMethod.id" class="hover:bg-gray-100 transition">
            <td class="px-6 py-4">{{ paymentMethod.id }}</td>
            <td class="px-6 py-4">{{ paymentMethod.method_name }}</td>
            <td class="px-6 py-4">{{ paymentMethod.description }}</td>
            <td class="px-6 py-4">{{ paymentMethod.fee }}</td>
            <td class="px-6 py-4 text-right">
              <button @click="openEditPaymentMethodModal(paymentMethod)" class="text-indigo-600 mr-2"><PencilSquareIcon class="h-5 w-5 inline-block" aria-hidden="true" /></button>
              <button @click="openDeletePaymentMethodModal(paymentMethod.id)" class="text-red-600"><TrashIcon class="h-5 w-5 inline-block" aria-hidden="true" /></button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="mt-4">
        <div class="flex space-x-2">
          <button class="bg-indigo-600 text-white px-4 py-2 rounded" @click="addPaymentMethodOpen = true">Dodaj formę
            płatności</button>
        </div>
      </div>
    </div>

    <TransitionRoot as="addSubpage" :show="addProviderOpen">
      <Dialog class="relative z-10" @close="addProviderOpen = false">
        <TransitionChild as="addProvider" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
          leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>

        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="addProvider" enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel
                class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                <form @submit.prevent="submitAddProviderForm">
                  <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                    <div class="sm:flex sm:items-start">
                      <div
                        class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                        <PlusCircleIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                      </div>
                      <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                        <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Dodaj dostawcę
                        </DialogTitle>
                        <div class="mt-2">
                          <p class="text-sm text-gray-500">Upewnij się, że wszystkie pola są wypełnione.</p>
                          <div class="border-b border-gray-900/10 pb-8">
                            <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                              <div class="sm:col-span-2">
                                <label for="add-name"
                                  class="block text-sm font-medium leading-6 text-gray-900">Nazwa</label>
                                <div class="mt-2">
                                  <input v-model="form.add.name" type="text" name="add-name" id="add-name"
                                    @blur="validateTitle('add')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form.add.errors.name" class="text-red-500 text-xs mt-1">{{
                                    form.add.errors.name }}</p>
                                </div>
                              </div>

                              <div class="sm:col-span-2">
                                <label for="add-cost"
                                  class="block text-sm font-medium leading-6 text-gray-900">Koszt</label>
                                <div class="mt-2">
                                  <input v-model="form.add.cost" type="number" step="0.01" name="add-cost" id="add-cost"
                                    @blur="validateCost('add')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form.add.errors.cost" class="text-red-500 text-xs mt-1">{{
                                    form.add.errors.cost }}</p>
                                </div>
                              </div>

                              <div class="sm:col-span-2">
                                <label for="add-estimated_delivery_days"
                                  class="block text-sm font-medium leading-6 text-gray-900">Czas dostawy (dni)</label>
                                <div class="mt-2">
                                  <input v-model="form.add.estimated_delivery_days" type="number" step="0.01"
                                    name="add-estimated_delivery_days" id="add-estimated_delivery_days"
                                    @blur="validateEstimatedDeliveryDays('add')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form.add.errors.estimated_delivery_days" class="text-red-500 text-xs mt-1">{{
                                    form.add.errors.estimated_delivery_days }}</p>
                                </div>
                              </div>

                              <div class="sm:col-span-6">
                                <label for="add-description"
                                  class="block text-sm font-medium leading-6 text-gray-900">Opis</label>
                                <div class="mt-2">
                                  <textarea v-model="form.add.description" name="description" id="add-description"
                                    rows="3" @blur="validateDescription('add')"
                                    class="block w-full max-h-48 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                                </textarea>
                                  <p v-if="form.add.errors.description" class="text-red-500 text-xs mt-1">{{
                                    form.add.errors.description }}</p>
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
                      Dodaj
                    </button>
                    <button type="button"
                      class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                      @click="addProviderOpen = false">
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

    <TransitionRoot as="editSubpage" :show="editProviderOpen">
      <Dialog class="relative z-10" @close="editProviderOpen = false">
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
                <form @submit.prevent="submitEditProviderForm">
                  <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                    <div class="sm:flex sm:items-start">
                      <div
                        class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                        <PencilSquareIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                      </div>
                      <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                        <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Edytuj dostawcę
                        </DialogTitle>
                        <div class="mt-2">
                          <p class="text-sm text-gray-500">Upewnij się, że wszystkie pola są wypełnione.</p>
                          <div class="border-b border-gray-900/10 pb-8">
                            <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                              <div class="sm:col-span-2">
                                <label for="edit-name"
                                  class="block text-sm font-medium leading-6 text-gray-900">Nazwa</label>
                                <div class="mt-2">
                                  <input v-model="form.edit.name" type="text" name="edit-name" id="edit-name"
                                    @blur="validateTitle('edit')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form.edit.errors.name" class="text-red-500 text-xs mt-1">{{
                                    form.edit.errors.name }}</p>
                                </div>
                              </div>

                              <div class="sm:col-span-2">
                                <label for="edit-cost"
                                  class="block text-sm font-medium leading-6 text-gray-900">Koszt</label>
                                <div class="mt-2">
                                  <input v-model="form.edit.cost" type="number" step="0.01" name="edit-cost"
                                    id="edit-cost" @blur="validateCost('edit')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form.edit.errors.cost" class="text-red-500 text-xs mt-1">{{
                                    form.edit.errors.cost }}</p>
                                </div>
                              </div>

                              <div class="sm:col-span-2">
                                <label for="edit-estimated_delivery_days"
                                  class="block text-sm font-medium leading-6 text-gray-900">Czas dostawy (dni)</label>
                                <div class="mt-2">
                                  <input v-model="form.edit.estimated_delivery_days" type="number" step="0.01"
                                    name="edit-estimated_delivery_days" id="edit-estimated_delivery_days"
                                    @blur="validateEstimatedDeliveryDays('edit')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form.edit.errors.estimated_delivery_days" class="text-red-500 text-xs mt-1">
                                    {{ form.edit.errors.estimated_delivery_days }}</p>
                                </div>
                              </div>

                              <div class="sm:col-span-6">
                                <label for="edit-description"
                                  class="block text-sm font-medium leading-6 text-gray-900">Opis</label>
                                <div class="mt-2">
                                  <textarea v-model="form.edit.description" name="edit-description"
                                    id="edit-description" rows="3" @blur="validateDescription('edit')"
                                    class="block w-full max-h-48 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                              </textarea>
                                  <p v-if="form.edit.errors.description" class="text-red-500 text-xs mt-1">{{
                                    form.edit.errors.description }}</p>
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
                      @click="editProviderOpen = false">
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


    <TransitionRoot as="div" :show="deleteConfirmationOpen" @close="deleteConfirmationOpen = false">
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
                        <p class="text-sm text-gray-500">Czy na pewno chcesz usunąć ten element? Ta czynność jest
                          nieodwracalna.</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                  <button @click="deleteProvider"
                    class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-700 sm:ml-3 sm:w-auto">Usuń</button>
                  <button type="button"
                    class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                    @click="deleteConfirmationOpen = false">Anuluj</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <TransitionRoot as="div" :show="deletePaymentMethodOpen" @close="deletePaymentMethodOpen = false">
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
                        <p class="text-sm text-gray-500">Czy na pewno chcesz usunąć ten element? Ta czynność jest
                          nieodwracalna.</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                  <button @click="confirmDeletePaymentMethod"
                    class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-700 sm:ml-3 sm:w-auto">Usuń</button>
                  <button type="button"
                    class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                    @click="deletePaymentMethodOpen = false">Anuluj</button>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <TransitionRoot as="addSubpage" :show="addPaymentMethodOpen">
      <Dialog class="relative z-10" @close="addPaymentMethodOpen = false">
        <TransitionChild as="addProvider" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100"
          leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
          <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </TransitionChild>

        <div class="fixed inset-0 z-10 w-screen overflow-y-auto">
          <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <TransitionChild as="addProvider" enter="ease-out duration-300"
              enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200"
              leave-from="opacity-100 translate-y-0 sm:scale-100"
              leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
              <DialogPanel
                class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                <form @submit.prevent="submitAddPaymentMethodForm">
                  <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                    <div class="sm:flex sm:items-start">
                      <div
                        class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                        <PlusCircleIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                      </div>
                      <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                        <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Dodaj formę
                          płatności</DialogTitle>
                        <div class="mt-2">
                          <p class="text-sm text-gray-500">Upewnij się, że wszystkie pola są wypełnione.</p>
                          <div class="border-b border-gray-900/10 pb-8">
                            <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                              <div class="sm:col-span-2">
                                <label for="add-name"
                                  class="block text-sm font-medium leading-6 text-gray-900">Nazwa</label>
                                <div class="mt-2">
                                  <input v-model="form2.add.method_name" type="text" name="add-name" id="add-name"
                                    @blur="validateTitle2('add')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form2.add.errors.name" class="text-red-500 text-xs mt-1">{{
                                    form2.add.errors.name }}</p>
                                </div>
                              </div>

                              <div class="sm:col-span-2">
                                <label for="add-cost"
                                  class="block text-sm font-medium leading-6 text-gray-900">Opłata</label>
                                <div class="mt-2">
                                  <input v-model="form2.add.fee" type="number" step="0.01" name="add-cost" id="add-cost"
                                    @blur="validateFee2('add')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form2.add.errors.fee" class="text-red-500 text-xs mt-1">{{
                                    form2.add.errors.fee }}</p>
                                </div>
                              </div>

                              <div class="sm:col-span-6">
                                <label for="add-description"
                                  class="block text-sm font-medium leading-6 text-gray-900">Opis</label>
                                <div class="mt-2">
                                  <textarea v-model="form2.add.description" name="description" id="add-description"
                                    rows="3"
                                    class="block w-full max-h-48 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"></textarea>
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
                      Dodaj
                    </button>
                    <button type="button"
                      class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                      @click="addPaymentMethodOpen = false">
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






    <TransitionRoot as="editSubpage" :show="editPaymentMethodOpen" @close="editPaymentMethodOpen = false">
      <Dialog class="relative z-10" @close="editPaymentMethodOpen = false">
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
                <form @submit.prevent="submitEditPaymentMethodForm">
                  <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                    <div class="sm:flex sm:items-start">
                      <div
                        class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                        <PencilSquareIcon class="h-6 w-6 text-blue-600" aria-hidden="true" />
                      </div>
                      <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                        <DialogTitle as="h3" class="text-base font-semibold leading-6 text-gray-900">Edytuj formę
                          płatności</DialogTitle>
                        <div class="mt-2">
                          <p class="text-sm text-gray-500">Upewnij się, że wszystkie pola są wypełnione.</p>
                          <div class="border-b border-gray-900/10 pb-8">
                            <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-6 sm:grid-cols-6">
                              <div class="sm:col-span-2">
                                <label for="edit-name"
                                  class="block text-sm font-medium leading-6 text-gray-900">Nazwa</label>
                                <div class="mt-2">
                                  <input v-model="form2.edit.name" type="text" name="edit-name" id="edit-name"
                                    @blur="validateTitle3('edit')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form2.edit.errors.name" class="text-red-500 text-xs mt-1">{{
                                    form2.edit.errors.name }}</p>
                                </div>
                              </div>

                              <div class="sm:col-span-2">
                                <label for="edit-cost"
                                  class="block text-sm font-medium leading-6 text-gray-900">Opłata</label>
                                <div class="mt-2">
                                  <input v-model="form2.edit.fee" type="number" step="0.01" name="edit-cost"
                                    id="edit-cost" @blur="validateFee2('edit')"
                                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                                  <p v-if="form2.edit.errors.fee" class="text-red-500 text-xs mt-1">{{
                                    form2.edit.errors.fee }}</p>
                                </div>
                              </div>

                              <div class="sm:col-span-6">
                                <label for="edit-description"
                                  class="block text-sm font-medium leading-6 text-gray-900">Opis</label>
                                <div class="mt-2">
                                  <textarea v-model="form2.edit.description" name="edit-description"
                                    id="edit-description" rows="3"
                                    class="block w-full max-h-48 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                              </textarea>

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
                      @click="editPaymentMethodOpen = false">
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

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import { PlusCircleIcon,  PencilSquareIcon, TrashIcon  } from '@heroicons/vue/24/outline'
import { Dialog, DialogTitle, DialogPanel, TransitionRoot, TransitionChild } from "@headlessui/vue";
const API_URL = import.meta.env.VITE_API_URL
const addProviderOpen = ref(false);
const addPaymentMethodOpen = ref(false);
const editProviderOpen = ref(false);
const editPaymentMethodOpen = ref(false);
const deleteConfirmationOpen = ref(false);
const providers = ref([]);
const paymentMethods = ref([]);
const deletePaymentMethodOpen = ref(false);
const currentDeletePaymentMethodId = ref(null);
const currentProviderId = ref(null);
const currentPaymentMethodId = ref(null);

const form = ref({
  add: {
    name: '',
    description: '',
    estimated_delivery_days: '',
    cost: 0,
    errors: {
      name: '',
      description: '',
      estimated_delivery_days: '',
      cost: 0,
    }
  },
  edit: {
    name: '',
    description: '',
    estimated_delivery_days: '',
    cost: 0,
    errors: {
      name: '',
      description: '',
      estimated_delivery_days: '',
      cost: 0,
    }
  }
})

onMounted(async () => {
  await fetchProviders();
  await fetchPaymentMethods();
});

const fetchProviders = async () => {
  try {
    console.log("Pobieram dostawców...");
    const response = await axios.get(API_URL + "/delivery-methods/");
    providers.value = response.data.map(provider => ({
      id: provider.id,
      name: provider.method_name,
      cost: provider.cost,
      estimated_delivery_days: provider.estimated_delivery_days,
      description: provider.description,
    }));
  } catch (error) {
    console.error("Błąd podczas pobierania dostawców:", error);
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


const validateTitle = (formType) => {
  const formInstance = formType === 'add' ? form.value.add : form.value.edit;

  if (!formInstance.name) {
    formInstance.errors.name = 'Nazwa dostawcy nie może być pusta';
  } else {
    formInstance.errors.name = '';
  }
};

const validateCost = (formType) => {
  const formInstance = formType === 'add' ? form.value.add : form.value.edit;

  if (formInstance.cost === null || formInstance.cost === '' || isNaN(Number(formInstance.cost))) {
    formInstance.errors.cost = 'Koszt nie może być pusty';
  } else if (Number(formInstance.cost) <= 0) {
    formInstance.errors.cost = 'Koszt musi być większy od 0';
  } else {
    formInstance.errors.cost = '';
  }
};

const validateEstimatedDeliveryDays = (formType) => {
  const formInstance = formType === 'add' ? form.value.add : form.value.edit;

  if (!formInstance.estimated_delivery_days) {
    formInstance.errors.estimated_delivery_days = 'Czas dostawy nie może być pusty';
  } else {
    formInstance.errors.estimated_delivery_days = '';
  }
};



const submitAddProviderForm = async () => {
  validateTitle('add');
  validateCost('add');
  validateEstimatedDeliveryDays('add');

  if (form.value.add.errors.name || form.value.add.errors.cost || form.value.add.errors.estimated_delivery_days) {
    return;
  }

  const newProviderData = {
    method_name: form.value.add.name.trim(),
    cost: form.value.add.cost,
    estimated_delivery_days: form.value.add.estimated_delivery_days,
    description: form.value.add.description,
  };

  console.log("Sending data:", newProviderData);

  try {

    const response = await axios.post(API_URL + "/delivery-methods/", newProviderData);
    const newProvider = {
      id: response.data.id,
      name: response.data.method_name,
      cost: response.data.cost,
      estimated_delivery_days: response.data.estimated_delivery_days,
      description: response.data.description,
    };
    providers.value.push(newProvider);
    form.value.add.name = '';
    form.value.add.cost = '';
    form.value.add.estimated_delivery_days = '';
    form.value.add.description = '';
    addProviderOpen.value = false;
  } catch (error) {
    console.error("Error adding provider:", error);
  }
};


const openDeleteProviderModal = (id) => {
  currentProviderId.value = id;
  deleteConfirmationOpen.value = true;
};
const deleteProvider = async () => {
  try {
    await axios.delete(API_URL + `/delivery-methods/${currentProviderId.value}`);
    providers.value = providers.value.filter(provider => provider.id !== currentProviderId.value);
    deleteConfirmationOpen.value = false;
  } catch (error) {
    console.error("Error deleting provider:", error);
  }
};



const openEditProviderModal = (provider) => {

  form.value.edit.name = provider.name;
  form.value.edit.cost = provider.cost;
  form.value.edit.estimated_delivery_days = provider.estimated_delivery_days;
  form.value.edit.description = provider.description;

  form.value.edit.errors = {
    name: '',
    description: '',
    estimated_delivery_days: '',
    cost: '',
  };

  currentProviderId.value = provider.id;
  editProviderOpen.value = true;
};

const submitEditProviderForm = async () => {
  validateTitle('edit');
  validateCost('edit');
  validateEstimatedDeliveryDays('edit');


  if (form.value.edit.errors.name || form.value.edit.errors.cost || form.value.edit.errors.estimated_delivery_days) {
    return;
  }

  const updatedProviderData = {
    method_name: form.value.edit.name.trim(),
    cost: form.value.edit.cost,
    estimated_delivery_days: form.value.edit.estimated_delivery_days,
    description: form.value.edit.description,
  };

  try {

    const response=await axios.put(`${API_URL}/delivery-methods/${currentProviderId.value}`, updatedProviderData);

    const index = providers.value.findIndex(provider => provider.id === currentProviderId.value);
    if (index !== -1) {
      providers.value[index] =  response.data;
    }

    editProviderOpen.value = false;
  } catch (error) {
    console.error("Error updating provider:", error);

  }
};
const openDeletePaymentMethodModal = (paymentMethodId) => {
  currentDeletePaymentMethodId.value = paymentMethodId;
  deletePaymentMethodOpen.value = true;
};

const confirmDeletePaymentMethod = async () => {
  try {
    await axios.delete(API_URL + `/payment-methods/${currentDeletePaymentMethodId.value}`);
    paymentMethods.value = paymentMethods.value.filter(method => method.id !== currentDeletePaymentMethodId.value);
    deletePaymentMethodOpen.value = false;
  } catch (error) {
    console.error("Błąd podczas usuwania metody płatności:", error);
  }
};
//zrobione

const form2 = ref({
  add: {
    method_name: '',
    description: '',
    fee: null,
    errors: {
      name: '',
      fee: '',
    }
  },
  edit: {
    method_name: '',
    description: '',
    fee: null,
    errors: {
      name: '',
      fee: '',
    }
  },
});

const validateTitle2 = (formType) => {

  const form = formType === 'add' ? form2.value.add : form2.value.edit;

  if (!form.method_name) {
    form.errors.name = 'Nazwa nie może być pusta';
  } else {
    form.errors.name = '';
  }
};
const validateTitle3 = (formType) => {

  const form = formType === 'add' ? form2.value.add : form2.value.edit;

  if (!form.name) {
    form.errors.name = 'Nazwa nie może być pusta';
  } else {
    form.errors.name = '';
  }
};

const validateFee2 = (formType) => {
  const form = formType === 'add' ? form2.value.add : form2.value.edit;


  const fee = Number(form.fee);

  if (isNaN(fee) || form.fee === '' || form.fee === null || form.fee === undefined || form.fee === '') {
    form.errors.fee = 'Opłata nie może być pusta';
  } else if (fee <= 0) {
    form.errors.fee = 'Opłata musi być większa od 0';
  } else {
    form.errors.fee = '';
  }
};



const submitAddPaymentMethodForm = async () => {
  validateTitle2('add');
  validateFee2('add');

  if (form2.value.add.errors.name || form2.value.add.errors.fee) {
    return;
  }

  const newPaymentMethodData = {
    method_name: form2.value.add.method_name.trim(),
    fee: form2.value.add.fee,
    description: form2.value.add.description,
  };

  console.log("Sending data:", newPaymentMethodData);

  try {
    const response = await axios.post(API_URL + "/payment-methods/", newPaymentMethodData);
    const newPaymentMethod = {
      id: response.data.id,
      method_name: response.data.method_name,
      fee: response.data.fee,
      description: response.data.description,
    };
    paymentMethods.value.push(newPaymentMethod);
    form2.value.add.method_name = '';
    form2.value.add.fee = '';
    form2.value.add.description = '';
    addPaymentMethodOpen.value = false;
  } catch (error) {
    console.error("Error adding payment method:", error);

  }
};




const openEditPaymentMethodModal = (paymentMethod) => {
  currentPaymentMethodId.value = paymentMethod.id;
  form2.value.edit.name = paymentMethod.method_name;
  form2.value.edit.description = paymentMethod.description;
  form2.value.edit.fee = paymentMethod.fee;
  editPaymentMethodOpen.value = true;
};


const submitEditPaymentMethodForm = async () => {
  validateTitle3('edit');
  validateFee2('edit');

  if (form2.value.edit.errors.name || form2.value.edit.errors.fee) {
    return;
  }
  const updatedPaymentMethodData = {
    method_name: form2.value.edit.name.trim(),
    description: form2.value.edit.description,
    fee: form2.value.edit.fee,
  };

  try {
    const response = await axios.put(API_URL + `/payment-methods/${currentPaymentMethodId.value}`, updatedPaymentMethodData);
    const index = paymentMethods.value.findIndex(method => method.id === currentPaymentMethodId.value);
    if (index !== -1) {
      paymentMethods.value[index] = response.data;
    }
    editPaymentMethodOpen.value = false;
  } catch (error) {
    console.error("Błąd podczas edytowania metody płatności:", error);
  }
};

</script>
