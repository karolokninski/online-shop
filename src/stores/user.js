import { defineStore } from 'pinia'
import axios from 'axios'
import * as jose from 'jose'

const API_URL = import.meta.env.VITE_API_URL

export const useUserStore = defineStore('user', {
  state: () => ({
    name: null,
    token: null,
    id: null,
    isAuthenticated: false,
    role: null
  }),
  actions: {
    async login(email, password, router) {
      try {
        const formData = new FormData()
        formData.append('email', email)
        formData.append('password', password)
        
        const response = await axios({
          method: 'post',
          url: API_URL + '/login',
          data: formData
        })

        this.token = response.data.access_token
        const decodedToken = jose.decodeJwt(this.token)
        this.isAuthenticated = true
        console.log(decodedToken.exp)
        this.name = decodedToken.name
        this.role = response.data.role
        this.id = response.data.id;
        router.push('/')
      } catch (error) {
        console.error('Login failed:', error.message)
        return error
      }
    },
    async register(name, email, password, router) {
      try {
        const requestData = {
          name: name,
          email: email,
          password: password
        }

        const response = await axios({
          method: 'post',
          url: API_URL + '/register',
          data: requestData
        })

        this.token = response.data.access_token
        //const decodedToken = jose.decodeJwt(this.token)
        this.isAuthenticated = true
        this.name = name
        this.id = response.data.id; 
        router.push('/')
      } catch (error) {
        console.error('Registration failed:', error.message)
        return error
      }
    },
    async passwordReset(email) {
      try {
        const requestData = {
          email: email
        }

        const response = await axios({
          method: 'post',
          url: API_URL + '/password-reset',
          data: requestData
        })

        return response
      } catch (error) {
        console.error('Password reset failed:', error.message)
        return error
      }
    },
    async verifyPasswordResetCode(code, email) {
      try {
        const requestData = {
          token: code,
          email: email
        }

        const response = await axios({
          method: 'post',
          url: API_URL + '/validate-password-reset',
          data: requestData
        })

        return response
      } catch (error) {
        console.error('Password reset code verification failed:', error.message)
        return error
      }
    },
    async changePassword(email, password) {
      try {
        const requestData = {
          email: email,
          password: password
        }

        const response = await axios({
          method: 'post',
          url: API_URL + '/change-password',
          data: requestData
        })

        return response
      } catch (error) {
        console.error('Password change failed:', error.message)
        return error
      }
    },
    logout(router) {
      try {
        this.token = null
        this.name = null
        this.isAuthenticated = false
        localStorage.removeItem('user')
        router.push('/')
      } catch (error) {
        console.error('Logout failed:', error.message)
      }
    },
    checkTokenExpiration(router) {
      if (this.token) {
        const decodedToken = jose.decodeJwt(this.token)
        if (this.isTokenExpired(decodedToken)) {
          this.logout(router)
        }
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
