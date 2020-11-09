import { createStore } from 'redux';
import trainingProgramReducer from './training-program-reducer';


const reducers = {
    trainingProgramPage: trainingProgramReducer,
};

const store = createStore(reducers);

export default store;
