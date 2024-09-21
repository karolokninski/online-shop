<template>
  <TransitionRoot as="template" :show="shoppingCartStore.open">
    <Dialog class="relative z-10" @close="shoppingCartStore.open = false">
      <TransitionChild as="template" enter="ease-in-out duration-500" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in-out duration-500" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-hidden">
        <div class="absolute inset-0 overflow-hidden">
          <div class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10">
            <TransitionChild as="template" enter="transform transition ease-in-out duration-500 sm:duration-700" enter-from="translate-x-full" enter-to="translate-x-0" leave="transform transition ease-in-out duration-500 sm:duration-700" leave-from="translate-x-0" leave-to="translate-x-full">
              <DialogPanel class="pointer-events-auto w-screen max-w-md">
                <div class="flex h-full flex-col overflow-y-scroll bg-white shadow-xl">
                  <div class="flex-1 overflow-y-auto px-4 py-6 sm:px-6">
                    <div class="flex items-start justify-between">
                      <DialogTitle class="text-lg font-medium text-gray-900">Koszyk</DialogTitle>
                      <div class="ml-3 flex h-7 items-center">
                        <button type="button" class="relative -m-2 p-2 text-gray-400 hover:text-gray-500" @click="shoppingCartStore.open = false">
                          <span class="absolute -inset-0.5" />
                          <span class="sr-only">Zamknij koszyk</span>
                          <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                        </button>
                      </div>
                    </div>

                    <div class="mt-8">
                      <div class="flow-root">
                        <ul role="list" class="-my-6 divide-y divide-gray-200">
                          <li v-for="product in shoppingCartStore.products" :key="product.id" class="flex py-6">
                            <div class="h-24 w-24 flex-shrink-0 overflow-hidden rounded-md border border-gray-200">
                              <img :src="product.imageSrc" :alt="product.imageAlt" class="h-full w-full object-cover object-center" />
                            </div>

                            <div class="ml-4 flex flex-1 flex-col">
                              <div>
                                <div class="flex justify-between text-base font-medium text-gray-900">
                                  <h3>
                                    <RouterLink :to="`/produkt/${product.id}`">{{ product.name }}</RouterLink>
                                  </h3>
                                  <p class="ml-4">{{ product.totalPrice}} PLN</p>
                                </div>
                                <div class="flex justify-between text-base font-medium text-gray-900">
                                  <p class="mt-1 text-sm text-gray-500">{{ product.color }}</p>
                                  <p v-if="product.quantity > 1" class="ml-4 text-xs text-gray-500">za szt. {{ product.price }} PLN</p>
                                </div>
                              </div>
                              <div class="flex flex-1 items-end justify-between text-sm">
                                <div class="flex flex-row">
                                  <select v-if="product.quantity < 5 && product.quantity >= 1" v-model="product.quantity" @change="handleQuantityChange(product.id)" class="rounded-md border-0 bg-transparent py-1 pr-7 text-gray-500 focus:ring-2 focus:ring-indigo-600 sm:text-sm">
                                    <option>1</option>
                                    <option>2</option>
                                    <option>3</option>
                                    <option>4</option>
                                    <option value="5">5+</option>
                                  </select>
                                  <input v-else type="number" v-model.lazy="product.quantity" @change="handleQuantityChange(product.id)" class="rounded-md border-0 bg-transparent py-1 w-16 text-gray-500 focus:ring-2 focus:ring-indigo-600 sm:text-sm">
                                </div>
                              </div>
                            </div>
                          </li>
                        </ul>
                      </div>
                    </div>

                  <div class="border-t border-gray-200 px-4 py-6 sm:px-6">
                    <div class="flex justify-between text-base font-medium text-gray-900">

                    </div>
                    <p class="mt-0.5 text-sm text-gray-500">Wysyłka i podatki obliczane przy kasie.</p>
                    <div class="mt-6">
                      <a href="#" class="flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-base font-medium text-white shadow-sm hover:bg-indigo-700">Wybierz dostawę</a>
                    </div>
                    <div class="mt-6 flex justify-center text-center text-sm text-gray-500">
                      <p>
                        lub{{ ' ' }}
                        <button type="button" class="font-medium text-indigo-600 hover:text-indigo-500" @click="shoppingCartStore.open = false">
                          Kontynuuj zakupy
                          <span aria-hidden="true"> &rarr;</span>
                        </button>
                      </p>
                    </div>
                  </div>
                </div>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>
  
<script setup>
  import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
  import { XMarkIcon } from '@heroicons/vue/24/outline'
  import { useShoppingCartStore } from '@/stores/shoppingCart'
  
  const shoppingCartStore = useShoppingCartStore()

  const handleQuantityChange = (id) => {
    const product = shoppingCartStore.products.find(product => product.id == id)
    
    if (product.quantity < 1) {
      product.quantity = 1
    } else if (product.quantity > 99) {
      console.log("Brak w magazynie.")
      // dodac pop-out
    }

    shoppingCartStore.updateQuantity()
  }
</script>