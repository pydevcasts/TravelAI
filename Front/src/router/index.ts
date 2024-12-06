import { createRouter, createWebHistory } from 'vue-router'

import SigninView from '@/views/Authentication/SigninView.vue'
import SignupView from '@/views/Authentication/SignupView.vue'
import NewPasswordView from "@/views/Authentication/NewPasswordView.vue";
import BasicChartView from '@/views/Charts/BasicChartView.vue'
import ECommerceView from '@/views/Dashboard/ECommerceView.vue'
// import FormElementsView from '@/views/Forms/FormElementsView.vue'
import PredictView from '@/views/Predict/PredictView.vue'
import SettingsView from '@/views/Pages/SettingsView.vue'
import ProfileView from '@/views/users/ProfileView.vue'
import TagView from '@/views/Tag/TagView.vue'
import UsersView from '@/views/users/UsersView.vue'
import AlertsView from '@/views/UiElements/AlertsView.vue'
import ButtonsView from '@/views/UiElements/ButtonsView.vue'
import { useUserStore } from '@/stores/userStore';

const routes = [
  {
    path: '/',
    name: 'eCommerce',
    component: ECommerceView,
    meta: {
      title: 'eCommerce Dashboard',
      requiresAuth: true 
    }
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
    meta: {
      title: 'Profile',
      requiresAuth: true 
    }
  },
  {
    path: '/tag',
    name: 'tag',
    component: TagView,
    meta: {
      title: 'tag',
      requiresAuth: true 
    }
  },

  // {
  //   path: '/forms/form-elements',
  //   name: 'formElements',
  //   component: FormElementsView,
  //   meta: {
  //     title: 'Form Elements'
  //   }
  // },
  {
    path: '/predict',
    name: 'predict',
    component: PredictView,
    meta: {
      title: 'Predict House'
    }
  },
  {
    path: '/users',
    name: 'users',
    component: UsersView,
    meta: {
      title: 'Users',
      requiresAuth: true 
    }
  },
  {
    path: '/pages/settings',
    name: 'settings',
    component: SettingsView,
    meta: {
      title: 'Settings'
    }
  },
  {
    path: '/charts/basic-chart',
    name: 'basicChart',
    component: BasicChartView,
    meta: {
      title: 'Basic Chart'
    }
  },
  {
    path: '/ui-elements/alerts',
    name: 'alerts',
    component: AlertsView,
    meta: {
      title: 'Alerts'
    }
  },
  {
    path: '/ui-elements/buttons',
    name: 'buttons',
    component: ButtonsView,
    meta: {
      title: 'Buttons'
    }
  },
  {
    path: '/signin',
    name: 'signin',
    component: SigninView,
    meta: {
      title: 'Signin'
    }
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
    meta: {
      title: 'Signup'
    }},
  {
    path: '/new-password',
    name: 'new-password',
    component: NewPasswordView,
    meta: {
      title: 'New Password'
    }
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { left: 0, top: 0 }
  }
})


router.beforeEach((to, from, next) => {
  const userStore = useUserStore();
  const isAuthenticated = userStore.isAuthenticated;

  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/signin');
  } else {
    next();
  }
});

export default router
