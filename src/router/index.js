import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
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
      path: '/produkty',
      name: 'products',
      component: () => import('../views/ProductsView.vue')
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
      path: '/:pathMatch(.*)*',
      name: 'pageNotFound',
      component: () => import('../views/PageNotFoundView.vue')
    }
  ]
})

export default router
