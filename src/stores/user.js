import { defineStore } from 'pinia'
import axios from 'axios'
// import jwtDecode from 'jwt-decode'
import router from '@/router'

export const useSearchStore = defineStore('search', {
  state: () => ({
    user: null,
    token: null,
    isAuthenticated: false
  }),
  actions: {
    async login(username, password) {

      try {
        const response = await axios.post('/token', {
          username: username,
          password: password,
        })

        this.token = response.data.access_token
        this.isAuthenticated = true
        // const decodedToken = jwtDecode(this.token)
        this.user = username
        router.push({ name: 'dashboard' })

      } catch (error) {
        console.error('Login failed:', error)
      }
    }
  }
});
