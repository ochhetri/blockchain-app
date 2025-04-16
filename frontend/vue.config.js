// frontend/vue.config.js
const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.NODE_ENV === 'production' ? '/' : '/',

  // Add chainWebpack to modify the underlying Webpack config
  chainWebpack: config => {
    // Target all CSS rule types (CSS, PostCSS, Sass, etc.)
    const cssRule = config.module.rule('css'); // Basic CSS rule
    const postcssRule = config.module.rule('postcss'); // PostCSS rule

    // Function to modify the css-loader options
    const setUrlOption = (use) => {
      if (use.loader === 'css-loader') {
        use.options = use.options || {};
        // --- THIS IS THE KEY ---
        // Disable URL handling by css-loader
        use.options.url = false;
        console.log('!!! Disabled css-loader url handling for:', use.loader); // For verification
      }
    };

    // Apply the modification to the loaders within the rules
    // Need to target the specific 'use' entries for css-loader
    // This structure might vary slightly based on exact Vue CLI version, but aims to find css-loader
    cssRule.oneOfs.store.forEach(oneOf => {
       oneOf.use('css-loader').tap(options => {
          options.url = false;
          console.log(`!!! Disabled url handling in css-loader for css rule oneOf`);
          return options;
       });
    });
     postcssRule.oneOfs.store.forEach(oneOf => {
       oneOf.use('css-loader').tap(options => { // Assumes css-loader runs before postcss-loader in this chain
          options.url = false;
          console.log(`!!! Disabled url handling in css-loader for postcss rule oneOf`);
          return options;
       });
    });

     // --- Fallback/Alternative approach if the above doesn't target correctly ---
     // Iterate through rules and uses more generally (less precise)
     /*
     config.module.rules.store.forEach(rule => {
       rule.uses.store.forEach(useEntry => {
         if (useEntry.store.get('loader') === 'css-loader') {
           useEntry.store.set('options', {
             ...(useEntry.store.get('options') || {}),
             url: false
           });
           console.log('!!! Disabled css-loader url handling (General)');
         }
       });
     });
     */
  }
})