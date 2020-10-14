<template>
    <b-container >
        <b-row class="justify-content-center">
            <b-col v-for="training in trainings" :key="training.id" sm="6" md="6" lg="3">
                <TrainingProgramm :training="training" />
            </b-col>
            <NewTraining />
        </b-row>
    </b-container>
</template>

<script>
import TrainingProgramm from '~/components/TrainingProgramm.vue'
import NewTraining from '~/components/NewTraining.vue'

export default {
  computed: {
    trainings () {
      console.log(this.$store.getters['trainingProgramm/trainingPrograms'])
      return this.$store.getters['trainingProgramm/trainingPrograms']
    }
  },
  components: {
    TrainingProgramm,
    NewTraining,
  }
}
</script>

<style>

</style>

