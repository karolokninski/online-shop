<template>
  <div class="text-black">
    <h1 class=" text-3xl mb-8">Produkty</h1>

    <div>
    <!-- <div class="overflow-x-auto"> -->
      <table class="w-auto table-auto bg-white rounded-md shadow-lg">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Zdjęcie
            </th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Nazwa
            </th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Cena
            </th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
              Status
            </th>
            <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
              Akcje
            </th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="product in products" :key="product.id">
            <td class="px-6 py-4">
              <img :src="product.image" alt="Product Image" class="w-12 h-12 rounded-md object-cover">
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm font-medium text-gray-900">{{ product.name }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm text-gray-900">${{ product.price }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span 
                :class="product.stock > 0 ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'"
                class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full">
                {{ product.stock > 0 ? 'In Stock' : 'Out of Stock' }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
              <button 
                @click="editProduct(product.id)" 
                class="text-indigo-600 hover:text-indigo-900 mr-3">
                Edit
              </button>
              <button 
                @click="deleteProduct(product.id)" 
                class="text-red-600 hover:text-red-900">
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      products: [
        {
          id: 1,
          name: "Product 1",
          price: 29.99,
          stock: 15,
          image: "https://via.placeholder.com/150",
        },
        {
          id: 2,
          name: "Product 2",
          price: 49.99,
          stock: 0,
          image: "https://via.placeholder.com/150",
        },
      ],
    };
  },
  methods: {
    editProduct(id) {
      console.log('Edit product', id)
    },
    deleteProduct(id) {
      console.log('Delete product', id)
    },
  },
};
</script>