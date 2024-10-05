import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior() {
    document.getElementById('app').scrollIntoView({ behavior: 'smooth' });
  },
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: () => import('../views/HomepageView.vue')
    },
    {
     path: '/sklepy',
     name: 'ourShops',
     component: () => import('../views/OurShopsView.vue')
    },
    {
      path: '/produkty',
      name: 'products',
      component: () => import('../views/ProductsView.vue')
    },
    {
      path: '/produkt/:id',
      name: 'product',
      component: () => import('../views/ProductView.vue')
    },
    {
      path: '/logowanie',
      name: 'signIn',
      component: () => import('../views/signIn/SignInView.vue')
    },
    {
      path: '/rejestracja',
      name: 'registraion',
      component: () => import('../views/signIn/RegistrationView.vue')
    },
    {
      path: '/przypomnienie-hasla',
      name: 'passwordReset',
      component: () => import('../views/signIn/PasswordResetView.vue')
    },
    {
      path: '/konto',
      name: 'account',
      component: () => import('../views/AccountView.vue'),
      children: [
        {
          path: 'ustawienia',
          name: 'accountSettings',
          component: () => import('../components/account/AccountSettings.vue'),
        },
        {
          path: 'zamowienia',
          name: 'orderHistory',
          component: () => import('../components/account/OrderHistory.vue'),
        },
        {
          path: 'ulubione',
          name: 'favouriteProducts',
          component: () => import('../components/account/FavouriteProducts.vue'),
        }
      ]
    },
    { 
      path: '/:pathMatch(.*)*',
      name: 'pageNotFound',
      component: () => import('../views/PageNotFoundView.vue'),
      beforeEnter: (to, from, next) => { // redirect /api to API server
        if (to.path.startsWith('/api')) {
          window.location.href = to.fullPath
        } else {
          next()
        }
      }
    }
  ]
})

export default router
