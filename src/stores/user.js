import { defineStore } from 'pinia'
import axios from 'axios'
// import jwtDecode from 'jwt-decode'
import router from '@/router'

const API_URL = import.meta.env.API_URL

export const useSearchStore = defineStore('search', {
  state: () => ({
    user: null,
    token: null,
    isAuthenticated: false
  }),
  actions: {
    async login(username, password) {

      try {
        const response = await axios.post(API_URL + '/token', {
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
