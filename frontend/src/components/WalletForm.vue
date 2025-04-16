<template>
  <form
    @submit.prevent="submitAddress"
    class="w-full max-w-xl mx-auto bg-white p-6 rounded-lg shadow-md"
  >
    <div class="mb-4">
      <label
        for="walletAddress"
        class="block text-gray-700 text-sm font-bold mb-2"
      >
        Enter Sepolia Wallet Address:
      </label>
      <input
        type="text"
        id="walletAddress"
        v-model.trim="address"
        placeholder="e.g., 0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe"
        required
        class="shadow appearance-none border rounded w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200"
        :class="{ 'border-red-500': hasError }"
      />
    </div>
    <div class="flex items-center justify-center">
      <button
        type="submit"
        :disabled="isLoading"
        class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded focus:outline-none focus:shadow-outline transition duration-200 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
      >
        <svg
          v-if="isLoading"
          class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle
            class="opacity-25"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            stroke-width="4"
          ></circle>
          <path
            class="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
          ></path>
        </svg>
        <span>{{ isLoading ? "Checking..." : "Check Balance" }}</span>
      </button>
    </div>
  </form>
</template>

<script>
import { ref } from "vue";

export default {
  name: "WalletForm",
  props: {
    isLoading: {
      // Receive loading state from parent
      type: Boolean,
      default: false,
    },
    hasError: {
      // Receive error state for styling
      type: Boolean,
      default: false,
    },
  },
  emits: ["submit-address"], // Declare the event
  setup(props, { emit }) {
    const address = ref("");

    const submitAddress = () => {
      if (address.value) {
        // Emit the address to the parent component
        emit("submit-address", address.value);
      }
    };

    return {
      address,
      submitAddress,
    };
  },
};
</script>
