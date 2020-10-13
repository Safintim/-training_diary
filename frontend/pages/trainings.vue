<template>
    <b-container >
        <b-row class="justify-content-center">
            <b-col v-for="index in 11" :key="index" sm="6" md="6" lg="3">
                <TrainingProgramm />
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
import TrainingProgramm from '~/components/TrainingProgramm.vue'

export default {
  
  components: {
    TrainingProgramm
  }
}
</script>

<style>

</style>

