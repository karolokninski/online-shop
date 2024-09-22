import { defineStore } from 'pinia'
import axios from 'axios'
// import jwtDecode from 'jwt-decode'
import router from '@/router'

const API_URL = import.meta.env.VITE_API_URL

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    token: null,
    isAuthenticated: false
  }),
  actions: {
    async login(username, password) {
      try {
        console.log(API_URL + '/token', username, password)
        const response = await axios.post(API_URL + '/token', {
          username: username,
          password: password
        })

        this.token = response.data.access_token
        this.isAuthenticated = true
        // const decodedToken = jwtDecode(this.token)
        this.user = username
        // router.push({ name: 'homepage' })

        console.log('Login successful') 
        console.log(response.data) 

      } catch (error) {
        console.error('Login failed:', error)
      }
    }
  }
});
