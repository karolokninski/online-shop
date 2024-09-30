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
<RouterLink to="/sklepy" class="-m-1.5 p-1.5"> <b>Nasze sklepy</b></RouterLink>
</button>
</div>
      </div>
      <div class="flex-1 bg-gray-100 p-6 rounded-md">
        <div class="bg-gray-100 py-10">
    <div class="container mx-auto max-w-md">
      <h2 class="text-3xl font-bold text-center text-gray-800 mb-6">Zapisz się do newslettera</h2>
      
      <form class="flex flex-col sm:flex-row items-center">

        <input 
          type="email" 
          placeholder="Wpisz swój email" 
          class="w-full sm:w-auto flex-1 px-4 py-2 mb-4 sm:mb-0 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" 
          required
        />


        <button 
          type="submit" 
          class="bg-black text-white px-8 py-3 rounded-md hover:bg-gray-800 transition-colors"
    >
        
         <b>Zapisz się</b> 
        </button>
      </form>
    </div>
  </div>
      </div>

    </div>
  </div>

</template>