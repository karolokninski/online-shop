
<template>
  <div class="bg-white flex min-h-full flex-1 flex-col">
    <header class="absolute bg-white inset-x-0 top-0 z-50" style="margin-bottom: 1rem;">
      <nav class="flex flex-col" aria-label="Global">
        <div class="flex flex-row items-center justify-between py-2 px-6 lg:px-8">
          <div class="flex lg:flex-1">
            <RouterLink to="/" class="-m-1.5 p-1.5">
              <span class="sr-only">Tech-Bay</span>
              <img class="h-12 w-auto" src="@/assets/logo.png" alt="" />
            </RouterLink>
          </div>
        </div>
      </nav>
    </header>
    <div class="flex flex-1 flex-col justify-center px-6 py-12 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Zaloguj się</h2>
      </div>
      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" method="POST" onsubmit="return false">
          <div class="h-1">
            <div v-if="errorMessage" class="flex flex-row gap-1">
              <ExclamationCircleIcon class="h-5 w-5 text-red-500" aria-hidden="true" />
              <p class="text-red-500 text-xs italic my-auto">{{ errorMessage }}</p>
            </div>
          </div>
          <div>
            <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Adres e-mail</label>
            <div class="mt-1">
              <input v-model="email" id="email" name="email" type="email" @input="validateEmail" :class="emailClass" autocomplete="email" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-inset sm:text-sm sm:leading-6" />
              <div v-if="!isValidEmail" class="flex flex-row mt-1 gap-1">
                <ExclamationCircleIcon class="h-5 w-6 text-red-500" aria-hidden="true" />
                <p class="text-red-500 text-xs my-auto">Nieprawidłowy adres email</p>
              </div>
            </div>
          </div>
          <div>
            <div class="flex items-center justify-between">
              <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Hasło</label>
              <div class="text-sm">
                <RouterLink to="/przypomnienie-hasla" class="font-semibold text-indigo-600 hover:text-indigo-500">Nie pamiętasz hasła?</RouterLink>
              </div>
            </div>
            <div class="mt-1">
              <input v-model="password" id="password" name="password" type="password" @input="validatePassword" :class="passwordClass" autocomplete="current-password" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-inset sm:text-sm sm:leading-6" />
              <div v-if="!isValidPassword" class="flex flex-row mt-1 gap-1">
                <ExclamationCircleIcon class="h-5 w-6 text-red-500" aria-hidden="true" />
                <p class="text-red-500 text-xs my-auto">Hasło musi mieć minimum 8 znaków</p>
              </div>
            </div>
          </div>
          <div>
            <button type="submit" @click="handleLogin" class="flex w-full h-9 justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
              <svg v-if="isLoading" class="animate-spin my-auto h-5 w-5 text-sm leading-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span v-else class="text-sm font-semibold leading-6 text-white">Zaloguj się</span>
            </button>
          </div>
        </form>
        <p class="mt-10 text-center text-sm text-gray-500">
          Nie masz konta?
          {{ ' ' }}
          <RouterLink to="/rejestracja" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Zarejestruj się</RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue'
  import { useUserStore } from '@/stores/user'
  import { useRouter } from 'vue-router'
  import { ExclamationCircleIcon } from '@heroicons/vue/24/outline'

  const router = useRouter()
  const isLoading = ref(false)
  const userStore = useUserStore()
  const email = ref('')
  const password = ref('')
  const errorMessage = ref('')
  const isValidEmail = ref(true)
  const isValidPassword = ref(true)

  const emailClass = computed(() => {
    return {
      'ring-red-500 focus:ring-red-600': !isValidEmail.value,
      'ring-gray-300 focus:ring-indigo-600': isValidEmail.value
    }
  })
  const passwordClass = computed(() => {
    return {
      'ring-red-500 focus:ring-red-600': !isValidPassword.value,
      'ring-gray-300 focus:ring-indigo-600': isValidPassword.value
    }
  })

  function validateEmail() {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    isValidEmail.value = emailRegex.test(email.value)
  }

  function validatePassword() {
    const passwordRegex = /^[A-Za-z\d@$!%*?&]{8,}$/
    isValidPassword.value = passwordRegex.test(password.value)
  }

  const handleLogin = async () => {
    if (isValidEmail.value && isValidPassword.value) {
      isLoading.value = true

      try {
        var result = await userStore.login(email.value, password.value, router)
      
        if (result.status != 200) {
          errorMessage.value = result.response.data.detail
        }

      } finally {
        isLoading.value = false
      }
    }
  }
</script>
  