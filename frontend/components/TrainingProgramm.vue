<template>
  <b-card
    :title="training.title"
    tag="article"
    style="max-width: 20rem"
    class="training-card mb-2"
  >
    <hr />
    <b-card-text>
      {{ training.description }}
    </b-card-text>
    <b-card-text> Упражнения: </b-card-text>
    <b-card-text>
      <p v-for="exercise in training.exercises" :key="exercise.id">{{ exercise.title }}</p>
    </b-card-text>
  </b-card>
</template>

<script>
export default {
  props: {
    training: {
      type: Object,
      default() {},
    },
  },
};
</script>

<style scoped>
.training-card {
  cursor: pointer;
}
</style>