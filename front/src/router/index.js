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
        name: 'user',
        component: () => import('@/views/user/List.vue'),
      },
      {
        path: '/person/list',
        name: 'person',
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
