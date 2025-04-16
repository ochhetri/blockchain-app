<template>
  <div
    v-if="addressData"
    class="mt-8 w-full max-w-xl mx-auto bg-white p-6 rounded-lg shadow-md text-center"
  >
    <h3 class="text-lg font-semibold mb-3 text-gray-800">
      Balance Information
    </h3>
    <p class="text-gray-600 break-words mb-2">
      <strong class="font-medium text-gray-700">Address:</strong>
      {{ addressData.address }}
    </p>
    <p class="text-2xl font-bold text-blue-700">
      {{ addressData.balance_ether }} ETH
    </p>
    <p class="text-sm text-gray-500 mt-1">
      ({{ addressData.balance_wei }} Wei)
    </p>
  </div>
  <div
    v-else-if="error"
    class="mt-8 w-full max-w-xl mx-auto bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative shadow-md"
    role="alert"
  >
    <strong class="font-bold">Error:</strong>
    <span class="block sm:inline"> {{ error }}</span>
  </div>
  <div v-else-if="initialLoad" class="mt-8 text-center text-gray-500">
    Enter a wallet address above to check its balance.
  </div>
</template>

<script>
export default {
  name: "BalanceDisplay",
  props: {
    addressData: {
      // Object containing address, balance_ether, balance_wei
      type: Object,
      default: null,
    },
    error: {
      // Error message string
      type: String,
      default: null,
    },
    initialLoad: {
      // Flag to show initial message
      type: Boolean,
      default: true,
    },
  },
};
</script>
