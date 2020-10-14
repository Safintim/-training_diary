<template>
  <div>
    <Navbar />
    <b-container class="page-content">
      <nuxt />
    </b-container>
    
  </div>
</template>

<script>
import Navbar from "~/components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
};
</script>

<style>
.page-content {
  margin-top: 20px;
}
</style>

