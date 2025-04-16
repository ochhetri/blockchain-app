<template>
  <div class="flex flex-col min-h-screen">
    <AppHeader />
    <div class="flex-grow">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </div>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";

export default {
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>

<style>
/* Global transition styles */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Ensure html, body, #app take full height for footer positioning */
html,
body,
#app {
  height: 100%;
  margin: 0;
}
#app {
  display: flex;
  flex-direction: column;
}
</style>
