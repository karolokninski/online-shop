import { createRouter, createWebHistory } from 'vue-router'
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL

const routes = [
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
    path: '/admin',
    name: 'adminPanel',
    component: () => import('../views/AdminPanelView.vue'),
    children: [
      {
        path: 'produkty',
        name: 'productManagement',
        component: () => import('../components/adminPanel/ProductManagement.vue'),
      },
      {
        path: 'kategorie',
        name: 'productCategories',
        component: () => import('../components/adminPanel/ProductCategories.vue'),
      },
      {
        path: 'parametry',
        name: 'productParameters',
        component: () => import('../components/adminPanel/ProductParameters.vue'),
      },
      {
        path: 'uzytkownicy',
        name: 'userManagement',
        component: () => import('../components/adminPanel/UserManagement.vue'),
      },
      {
        path: 'zamowienia',
        name: 'orderManagement',
        component: () => import('../components/adminPanel/OrderManagement.vue'),
      },
      {
        path: 'dostawa-i-platnosc',
        name: 'deliveryAndPayment',
        component: () => import('../components/adminPanel/DeliveryAndPayment.vue'),
      },
      {
        path: 'podstrony',
        name: 'subpageManagement',
        component: () => import('../components/adminPanel/SubpageManagement.vue'),
      },
    ]
  },
  { 
    path: '/:pathMatch(.*)*',
    name: 'pageNotFound',
    component: () => import('../views/PageNotFoundView.vue')
  }
]

const fetchSubpagesRoutes = async () => {
  try {
    const response = await axios.get(API_URL + '/subpages')
    const subpages = response.data

    subpages.forEach(subpage => {
      routes.push({
        path: subpage.path,
        name: subpage.path,
        component: () => import('../views/SubpageView.vue'),
        meta: {
          id: subpage.id,
          title: subpage.title
        }
      })
    })
  } catch (error) {
    console.error('Error fetching subpages:', error)
  }
}

// Call the function to fetch subpage routes
await fetchSubpagesRoutes()

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior() {
    document.getElementById('app').scrollIntoView({ behavior: 'smooth' });
  },
  routes
})

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Geeked.tech'
  next()
})

export default router
