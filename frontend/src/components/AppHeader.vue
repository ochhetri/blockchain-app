<template>
  <header
    class="bg-gradient-to-r from-blue-600 to-indigo-800 text-white shadow-md"
  >
    <nav class="container mx-auto px-4 py-3 flex items-center justify-between">
      <div class="flex items-center space-x-2">
        <!-- Use the logo from the public folder -->
        <img src="/img/logo.png" alt="App Logo" class="h-8 w-auto" />
        <span class="text-xl font-semibold">ETH Balance Checker</span>
      </div>
      <!-- Add Nav links here if needed -->
      <div>
        <a
          href="https://github.com/Garbii1/blockchain-app"
          target="_blank"
          rel="noopener noreferrer"
          class="text-gray-300 hover:text-white transition duration-200"
        >
          GitHub
        </a>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: "AppHeader",
};
</script>

<style scoped>
/* Add specific styles if Tailwind isn't enough */
</style>
