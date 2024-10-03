import { defineStore } from 'pinia'
import axios from 'axios'
import * as jose from 'jose'

const API_URL = import.meta.env.VITE_API_URL

export const useUserStore = defineStore('user', {
  state: () => ({
    name: null,
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
        this.name = decodedToken.name
        router.push('/')
      } catch (error) {
        console.error('Login failed:', error)
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
        // const decodedToken = jose.decodeJwt(this.token)
        this.isAuthenticated = true
        this.name = name
        router.push('/')
      } catch (error) {
        console.error('Registration failed:', error)
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
        console.error('Password reset failed:', error)
        return error
      }
    },
    async verifyPasswordResetCode(code, router) {
      try {
        const requestData = {
          code: code
        }

        // const response = await axios({
        //   method: 'post',
        //   url: API_URL + '/password-reset',
        //   data: requestData
        // })

        // return response
      } catch (error) {
        console.error('Password reset code verification failed:', error)
        return error
      }
    },
    logout() {
      try {
        this.token = null;
        this.name = null;
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
