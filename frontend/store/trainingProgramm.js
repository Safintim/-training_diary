export const state = () => ({
    trainingPrograms: [],
});

export const mutations = {
    setTrainingPrograms (state, programms) {
        state.trainingPrograms = programms;
    }
};

const trainingProgrammUrl = 'http://127.0.0.1:8000/api/training_programm/'

export const actions = {
    async fetch ({ commit }) {
        const programms = await this.$axios.$get(trainingProgrammUrl);
        commit('setTrainingPrograms', programms);
    },
};

export const getters = {
    trainingPrograms: state => state.trainingPrograms,
};
