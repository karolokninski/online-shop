<template>
  <div class="container mx-auto py-10">
    <div class="flex flex-col md:flex-row space-y-6 md:space-y-0 md:space-x-6">
      <div class="flex-1 bg-gray-100 p-6 rounded-md">
        <div class="text-center py-10">
          <h2 class="text-3xl font-bold text-gray-800 mb-6">Znajdź nas</h2>
          <button 
            type="button" 
            class="bg-black text-white px-8 py-3 rounded-md hover:bg-gray-800 transition-colors"
          >
            <RouterLink to="/sklepy" class="-m-1.5 p-1.5"><b>Nasze sklepy</b></RouterLink>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>