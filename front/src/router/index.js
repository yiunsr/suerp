// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "home" */ '@/components/First.vue'),
      },
      {
        path: '/user/list',
        name: 'user_list',
        component: () => import('@/views/user/List.vue'),
      },
      {
        path: '/user/new',
        name: 'user_new',
        component: () => import('@/views/user/NewEdit.vue'),
      },
      {
        path: '/user/:userId',
        name: 'user_edit',
        component: () => import('@/views/user/NewEdit.vue'),
      },
      {
        path: '/person/list',
        name: 'person_list',
        component: () => import('@/views/person/List.vue'),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router
