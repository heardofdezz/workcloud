import Vue from 'vue'
import VueRouter from 'vue-router'

import AccountsRoutes from '@/router/accounts'
import CommunitiesRoutes from '@/router/communities'

import { store } from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'landing',
    component: () => import('@/views/Landing.vue')
  },
  {
    path: '/home',
    name: 'home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/search',
    name: 'search',
    component: () => import('@/views/Search.vue')
  },
  ...AccountsRoutes,
  ...CommunitiesRoutes,
]

const router = new VueRouter({
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isApproved) {
      next({
        name: 'accounts.login',
        query: {
          nextURL: to.path
        }
      })
    }
    else if (
      to.matched.some(record => record.meta.StaffOnly) &&
      !store.getters.isStaff
    ) {
      next(false)
    }
    else {
      next()
    }
  }
  else {
    next()
  }
})

export default router
