<template>
  <footer class="bg-gray-200 text-gray-600 text-center p-4 mt-12">
    <div class="container mx-auto">
      © {{ new Date().getFullYear() }} ETH Balance Checker. Built with Flask &
      Vue.
    </div>
  </footer>
</template>

<script>
export default {
  name: "AppFooter",
};
</script>
