// frontend/src/main.js
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/css/tailwind.css"; // Import Tailwind CSS

createApp(App).use(router).mount("#app");
