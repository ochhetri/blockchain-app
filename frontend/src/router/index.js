// frontend/src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue"; // Rename default Home to HomeView if needed

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  // Add other routes here if needed (e.g., /about, /contract)
  // Example:
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }

  // --- Catch-all for sub-paths (handled by Netlify rewrite) ---
  // Vue Router handles specific defined paths. The Netlify _redirects
  // rule ensures that direct access to ANY path (e.g., /dashboard)
  // loads the index.html, allowing Vue Router to take over client-side.
  // You only need to define the routes you actively use in your app here.
  // If you want a specific component for /dashboard, define it:
  // { path: '/dashboard', name: 'dashboard', component: DashboardView },
  // otherwise, accessing /dashboard will likely show the HomeView or a 404
  // depending on your router setup or if you add a catch-all route:
  // { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFoundView }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL), // Use history mode
  routes,
});

export default router;
