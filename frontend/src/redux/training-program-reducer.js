const SET_TRAINING_PROGRAMS = 'SET_TRAINING_PROGRAMS';

const initialState = {
    trainingPrograms: [],
};

const trainingProgramReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_TRAINING_PROGRAMS:
            return {
                ...state,
                trainingPrograms: [...state.trainingPrograms],
            }
        default:
            return state;
    }
};

const setTrainingProgramsAC = (trainingPrograms) => ({type: SET_TRAINING_PROGRAMS, trainingPrograms});

export default trainingProgramReducer;
