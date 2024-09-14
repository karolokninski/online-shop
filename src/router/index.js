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
      }
  ]
})

export default router
