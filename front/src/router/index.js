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
        path: '/user',
        name: 'user_list',
        component: () => import('@/views/user/List.vue'),
      },
      {
        path: '/user/new',
        name: 'user_new',
        component: () => import('@/views/user/NewEdit.vue'),
      },
      {
        path: '/user/:id',
        name: 'user_edit',
        component: () => import('@/views/user/NewEdit.vue'),
      },
      {
        path: '/person',
        name: 'person_list',
        component: () => import('@/views/person/List.vue'),
      },
      {
        path: '/person/new',
        name: 'person_new',
        component: () => import('@/views/person/NewEdit.vue'),
      },
      {
        path: '/person/:id',
        name: 'person_edit',
        component: () => import('@/views/person/NewEdit.vue'),
      }, 
      {
        path: '/col_meta',
        name: 'col_meta_list',
        component: () => import('@/views/col_meta/List.vue'),
      },
      {
        path: '/col_meta/new',
        name: 'col_meta_new',
        component: () => import('@/views/col_meta/NewEdit.vue'),
      },
      {
        path: '/col_meta/:id',
        name: 'col_meta_edit',
        component: () => import('@/views/col_meta/NewEdit.vue'),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router
