<template>
  <div class="d-flex" id="wrapper">
    <Sidebar />
    <div class="container-fluid">
      <Navbar />
      <nuxt />
    </div>
  </div>
</template>

<script>
import Sidebar from '~/components/Sidebar.vue';
import Navbar from '~/components/Navbar.vue';

export default {
  components: {
    Sidebar,
    Navbar,
  },
};
</script>

<style scoped>
</style>

