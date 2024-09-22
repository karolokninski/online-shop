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
     path: '/nasze-sklep',
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
      component: () => import('../views/SignInView.vue')
    },
    {
      path: '/rejestracja',
      name: 'registraion',
      component: () => import('../views/RegistrationView.vue')
    },
    {
      path: '/przypomnienie-hasla',
      name: 'passwordReset',
      component: () => import('../views/PasswordResetView.vue')
    },
    { 
      path: '/:pathMatch(.*)*',
      name: 'pageNotFound',
      component: () => import('../views/PageNotFoundView.vue')
    }
  ]
})

export default router
