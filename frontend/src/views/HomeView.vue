<template>
  <div>
    <!-- Hero Section -->
    <section
      class="bg-hero-pattern bg-cover bg-center text-white py-20 md:py-32 relative"
    >
      <!-- Overlay for better text visibility -->
      <div class="absolute inset-0 bg-black opacity-50"></div>
      <div class="container mx-auto px-4 text-center relative z-10">
        <h1 class="text-4xl md:text-5xl font-bold mb-4">
          Sepolia ETH Balance Checker
        </h1>
        <p class="text-lg md:text-xl mb-8">
          Instantly check the Ether balance of any address on the Sepolia test
          network.
        </p>
        <!-- Wallet Form is placed below the hero text -->
        <WalletForm
          @submit-address="fetchBalance"
          :is-loading="isLoading"
          :has-error="!!error"
          class="relative z-20"
        />
      </div>
    </section>

    <!-- Main Content Area -->
    <main class="container mx-auto px-4 py-8">
      <!-- Balance Display Area -->
      <BalanceDisplay
        :address-data="balanceData"
        :error="error"
        :initial-load="initialLoad"
      />

      <!-- Optional: Add other sections like transaction history, etc. -->
    </main>
  </div>
</template>

<script>
import { ref } from "vue";
import axios from "axios";
import WalletForm from "@/components/WalletForm.vue";
import BalanceDisplay from "@/components/BalanceDisplay.vue";

export default {
  name: "HomeView",
  components: {
    WalletForm,
    BalanceDisplay,
  },
  setup() {
    const balanceData = ref(null);
    const isLoading = ref(false);
    const error = ref(null);
    const initialLoad = ref(true); // Track if it's the initial state

    // Define API Base URL - Use environment variables for flexibility
    // In development, this points to your local Flask server.
    // In production, this will point to your Render deployment URL.
    const API_BASE_URL =
      process.env.VUE_APP_API_BASE_URL || "http://127.0.0.1:5001/api";
    console.log("API Base URL:", API_BASE_URL); // For debugging

    const fetchBalance = async (address) => {
      isLoading.value = true;
      error.value = null; // Clear previous errors
      balanceData.value = null; // Clear previous data
      initialLoad.value = false; // No longer initial state

      try {
        const response = await axios.get(`${API_BASE_URL}/balance/${address}`);
        if (response.data && !response.data.error) {
          balanceData.value = response.data;
        } else {
          // Handle errors returned in the response data
          error.value = response.data.error || "An unknown error occurred.";
        }
      } catch (err) {
        console.error("API Request Error:", err);
        if (err.response) {
          // The request was made and the server responded with a status code
          // that falls out of the range of 2xx
          error.value =
            err.response.data.error ||
            `Error ${err.response.status}: ${err.response.statusText}`;
        } else if (err.request) {
          // The request was made but no response was received
          error.value = "Could not connect to the API server. Is it running?";
        } else {
          // Something happened in setting up the request that triggered an Error
          error.value = err.message || "An unexpected error occurred.";
        }
        balanceData.value = null; // Clear data on error
      } finally {
        isLoading.value = false;
      }
    };

    return {
      balanceData,
      isLoading,
      error,
      initialLoad,
      fetchBalance,
    };
  },
};
</script>

<style scoped>
/* Add specific styles for HomeView if needed */
</style>
