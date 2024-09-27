import { defineStore } from 'pinia'
import axios from 'axios'
import * as jose from 'jose'

const API_URL = import.meta.env.VITE_API_URL

export const useUserStore = defineStore('user', {
  state: () => ({
    username: null,
    token: null,
    isAuthenticated: false
  }),
  actions: {
    async login(email, password, router) {
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
        const decodedToken = jose.decodeJwt(this.token)
        this.isAuthenticated = true
        this.username = decodedToken.username
        router.push('/')
      } catch (error) {
        console.error('Login failed:', error)
      }
    },
    async register(username, email, password, router) {
      try {
        const requestData = {
          username: username,
          email: email,
          password: password
        }

        const response = await axios({
          method: 'post',
          url: API_URL + '/register',
          data: requestData
        })

        this.token = response.data.access_token
        // const decodedToken = jose.decodeJwt(this.token)
        this.isAuthenticated = true
        this.username = username
        router.push('/')
      } catch (error) {
        console.error('Registration failed:', error)
      }
    },
    async passwordReset(email, router) {
      try {
        const requestData = {
          email: email
        }

        const response = await axios({
          method: 'post',
          url: API_URL + '/passwordReset',
          data: requestData
        })

        // this.token = response.data.access_token
        // const decodedToken = jose.decodeJwt(this.token)
        // this.isAuthenticated = true
        // this.username = username
        // router.push('/')
      } catch (error) {
        console.error('Password reset failed:', error)
      }
    },
    logout() {
      try {
        this.token = null;
        this.username = null;
        this.isAuthenticated = false;
        localStorage.removeItem('user');
      } catch (error) {
        console.error('Logout failed:', error);
      }
    }
  },
  persist: {
    enabled: true,
    strategies: [
      {
        key: 'user',
        storage: localStorage
      },
    ],
  }
});
