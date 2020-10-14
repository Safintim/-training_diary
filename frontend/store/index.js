export const actions = {
    async nuxtServerInit ({ dispatch }) {
        console.log('111');
        await dispatch('trainingProgramm/fetch')
    }
}