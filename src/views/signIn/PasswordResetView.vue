<template>
  <div class="bg-white flex min-h-full flex-1 flex-col">
    <header class="absolute bg-white inset-x-0 top-0 z-50 mt-2">
      <nav class="flex flex-col" aria-label="Global">
        <div class="flex flex-row items-center justify-between py-2 px-6 lg:px-8">
          <div class="flex lg:flex-1 h-12">
            <RouterLink to="/" class="ml-1 pt-0 pb-0 px-1 flex flex-row border-b-2 border-black">
              <img class="h-12 w-auto" src="@/assets/logo.svg" alt="logo Geeked.tech" />
              <span class="text-black text-lg font-semibold mb-1 mt-auto">Geeked</span>
            </RouterLink>
          </div>
        </div>
      </nav>
    </header>
    <div v-if="!submitCodeView && !changePasswordView" class="flex flex-1 flex-col justify-center px-6 py-12 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Przypomnienie hasła</h2>
      </div>
      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" method="POST" onsubmit="return false">
          <div v-if="emailErrorMessage" class="h-1">
            <div class="flex flex-row gap-1">
              <ExclamationCircleIcon class="h-5 w-5 text-red-500" aria-hidden="true" />
              <p class="text-red-500 text-xs my-auto font-semibold">{{ emailErrorMessage }}</p>
            </div>
          </div>
          <div>
            <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Adres e-mail</label>
            <div class="mt-1">
              <input v-model="email" id="email" name="email" type="email" @input="validateEmail" :disabled="isLoading" :class="emailClass" autocomplete="email" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-inset sm:text-sm sm:leading-6" />
              <div v-if="!isValidEmail" class="flex flex-row mt-1 gap-1">
                <ExclamationCircleIcon class="h-5 w-6 text-red-500" aria-hidden="true" />
                <p class="text-red-500 text-xs my-auto">Nieprawidłowy adres e-mail</p>
              </div>
            </div>
          </div>
          <div>
            <button type="submit" @click="handlePasswordReset" class="flex w-full h-9 justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
              <svg v-if="isLoading" class="animate-spin my-auto h-5 w-5 text-sm leading-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span v-else class="text-sm font-semibold leading-6 text-white">Odzyskaj hasło</span>
            </button>
          </div>
        </form>
        <p class="mt-10 text-center text-sm text-gray-500">
          Pamiętasz hasło?
          {{ ' ' }}
          <RouterLink to="/logowanie" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Zaloguj się</RouterLink>
        </p>
      </div>
    </div>
    <div v-if="submitCodeView && !changePasswordView" class="flex flex-1 flex-col justify-center px-6 py-12 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Wprowadź kod weryfikacyjny</h2>
      </div>
      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" method="POST" onsubmit="return false">
          <div v-if="validationErrorMessage" class="h-1">
            <div class="flex flex-row gap-1">
              <ExclamationCircleIcon class="h-5 w-5 text-red-500" aria-hidden="true" />
              <p class="text-red-500 text-xs my-auto font-semibold">{{ validationErrorMessage }}</p>
            </div>
          </div>
          <div>
            <label for="code" class="block text-sm font-medium leading-6 text-gray-900">Kod weryfikacyjny</label>
            <div class="mt-1">
              <input v-model="code" id="code" name="code" type="text" @input="validateCode" :disabled="isLoading" :class="codeClass" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-inset sm:text-sm sm:leading-6" />
              <div v-if="!isValidCode" class="flex flex-row mt-1 gap-1">
                <ExclamationCircleIcon class="h-5 w-6 text-red-500" aria-hidden="true" />
                <p class="text-red-500 text-xs my-auto">Kod weryfikacyjny musi się składać z 6 znaków</p>
              </div>
            </div>
          </div>
          <div>
            <button type="submit" @click="handleSubmitCode" class="flex w-full h-9 justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
              <svg v-if="isLoading" class="animate-spin my-auto h-5 w-5 text-sm leading-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span v-else class="text-sm font-semibold leading-6 text-white">Weryfikuj</span>
            </button>
          </div>
        </form>
        <p class="mt-10 text-center text-sm text-gray-500">
          Pamiętasz hasło?
          {{ ' ' }}
          <RouterLink to="/logowanie" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Zaloguj się</RouterLink>
        </p>
      </div>
    </div>
    <div v-if="!submitCodeView && changePasswordView" class="flex flex-1 flex-col justify-center px-6 py-12 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Zmień hasło</h2>
      </div>
      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" method="POST" onsubmit="return false">
          <div v-if="changePasswordErrorMessage" class="h-1">
            <div class="flex flex-row gap-1">
              <ExclamationCircleIcon class="h-5 w-5 text-red-500" aria-hidden="true" />
              <p class="text-red-500 text-xs my-auto font-semibold">{{ changePasswordErrorMessage }}</p>
            </div>
          </div>
          <div>
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Nowe hasło</label>
            <div class="mt-1">
              <input v-model="password" id="password" name="password" type="password" @input="validatePassword" :disabled="isLoading" :class="passwordClass" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-inset sm:text-sm sm:leading-6" />
              <div v-if="!isValidPassword" class="flex flex-row mt-1 gap-1">
                <ExclamationCircleIcon class="h-5 w-6 text-red-500" aria-hidden="true" />
                <p class="text-red-500 text-xs my-auto">Hasło musi mieć minimum 8 znaków</p>
              </div>
            </div>
          </div>
          <div>
            <label for="repeatedPassword" class="block text-sm font-medium leading-6 text-gray-900">Powtórz nowe hasło</label>
            <div class="mt-1">
              <input v-model="repeatedPassword" id="repeatedPassword" name="repeatedPassword" type="password" @input="validateRepeatedPassword" :disabled="isLoading" :class="repeatedPasswordClass" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset placeholder:text-gray-400 focus:ring-2 focus:ring-inset sm:text-sm sm:leading-6" />
              <div v-if="!isValidRepeatedPassword" class="flex flex-row mt-1 gap-1">
                <ExclamationCircleIcon class="h-5 w-6 text-red-500" aria-hidden="true" />
                <p class="text-red-500 text-xs my-auto">Hasła muszą być takie same</p>
              </div>
            </div>
          </div>
          <div>
            <button type="submit" @click="handleChangePassword" class="flex w-full h-9 justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
              <svg v-if="isLoading" class="animate-spin my-auto h-5 w-5 text-sm leading-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span v-else class="text-sm font-semibold leading-6 text-white">Zmień hasło</span>
            </button>
          </div>
        </form>
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
  const submitCodeView = ref(false)
  const changePasswordView = ref(false)
  const userStore = useUserStore()
  const email = ref('')
  const code = ref('')
  const password = ref('')
  const repeatedPassword = ref('')
  const emailErrorMessage = ref('')
  const validationErrorMessage = ref('')
  const changePasswordErrorMessage = ref('')
  const isValidEmail = ref(true)
  const isValidCode = ref(true)
  const isValidPassword = ref(true)
  const isValidRepeatedPassword = ref(true)

  const emailClass = computed(() => {
    return {
      'ring-red-500 focus:ring-red-600': !isValidEmail.value,
      'ring-gray-300 focus:ring-indigo-600': isValidEmail.value
    }
  })

  const codeClass = computed(() => {
    return {
      'ring-red-500 focus:ring-red-600': !isValidEmail.value,
      'ring-gray-300 focus:ring-indigo-600': isValidEmail.value
    }
  })

  const passwordClass = computed(() => {
    return {
      'ring-red-500 focus:ring-red-600': !isValidEmail.value,
      'ring-gray-300 focus:ring-indigo-600': isValidEmail.value
    }
  })

  const repeatedPasswordClass = computed(() => {
    return {
      'ring-red-500 focus:ring-red-600': !isValidEmail.value,
      'ring-gray-300 focus:ring-indigo-600': isValidEmail.value
    }
  })

  function validateEmail() {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/
    isValidEmail.value = emailRegex.test(email.value)
  }

  function validateCode() {
    const codeRegex = /^[A-Za-z\d@$!%*?.&]{6}$/
    isValidCode.value = codeRegex.test(code.value)
  }

  function validatePassword() {
    const passwordRegex = /^[A-Za-z\d@$!%*?.&]{8,}$/
    isValidPassword.value = passwordRegex.test(password.value)
    validateRepeatedPassword()
  }
  
  function validateRepeatedPassword() {
    isValidRepeatedPassword.value = (password.value == repeatedPassword.value)
  }

  const handlePasswordReset = async () => {
    if (isValidEmail.value) {
      isLoading.value = true

      try {
        var result = await userStore.passwordReset(email.value)
        if (result.status != 200 && result.response.data.detail) {
          emailErrorMessage.value = result.response.data.detail
        } else if (result.status == 200) {
          submitCodeView.value = true
        }
      } finally {
        isLoading.value = false
      }
    }
  }
  const handleSubmitCode = async () => {
    if (isValidCode.value) {
      isLoading.value = true

      try {
        var result = await userStore.verifyPasswordResetCode(code.value, email.value)
        console.log(result)
        if (result.status != 200 && result.response.data.detail) {
          validationErrorMessage.value = result.response.data.detail
        } else if (result.status == 200) {
          submitCodeView.value = false
          changePasswordView.value = true
        }
      } finally {
        isLoading.value = false
      }
    }
  }

  const handleChangePassword = async () => {
    if (isValidPassword.value && isValidRepeatedPassword.value) {
      isLoading.value = true

      try {
        var result = await userStore.changePassword(email.value, password.value)
        if (result.status != 200 && result.response.data.detail) {
          changePasswordErrorMessage.value = result.response.data.detail
        } else if (result.status == 200) {
          changePasswordView.value = false
        }
      } finally {
        isLoading.value = false
      }
    }
  }
</script>
  