import { defineStore } from 'pinia'
import axios from 'axios'
import * as jose from 'jose'

const API_URL = import.meta.env.VITE_API_URL

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    token: null,
    isAuthenticated: false
  }),
  actions: {
    async login(email, password) {
      try {
        const formData = new FormData()
        formData.append('email', email)
        formData.append('password', password)
        
        const response = await axios({
          method: 'post',
          url: API_URL + '/token',
          data: formData,
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })

        this.token = response.data.access_token
        this.isAuthenticated = true
        const decodedToken = jose.decodeJwt(this.token)
        this.user = decodedToken.username
      } catch (error) {
        console.error('Login failed:', error)
      }
    }
  }
});
