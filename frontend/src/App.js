import React from 'react';
import './App.css';

import { BrowserRouter, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar/Sidebar';
import Navbar from './components/Navbar/Navbar';
import Blog from './components/Blog/Blog';
import Exercises from './components/Exercises/Exercises';
import Measurements from './components/Measurements/Measurements';
import MyTrainingPrograms from './components/MyTrainingPrograms/MyTrainingPrograms';
import Statistics from './components/Statistics/Statistics';
import TrainingProgram from './components/TrainingPrograms/TrainingPrograms';
import ProgramForm from './components/TrainingPrograms/ProgramForm/ProgramForm';
import Program from './components/TrainingPrograms/Program/Program';
import ExerciseItem from './components/Exercises/ExerciseItem/ExerciseItem';
import ExerciseForm from './components/Exercises/ExerciseForm/ExerciseForm';
import 'bootstrap/dist/css/bootstrap.min.css';

const App = (props) => {
    return (
        <BrowserRouter>
            <div className='appWrapper'>
                <Sidebar />
                <Navbar />
                <div className='appContent'>
                    <Route 
                        path='/blog'
                        render={() => <Blog />}
                    />
                    <Route 
                        path='/exercises'
                        render={() => <Exercises />}
                    />
                    <Route
                        path='/exercise'
                        render={() => <ExerciseItem />}
                    />
                    <Route
                        path='/exercise-form'
                        render={() => <ExerciseForm />}
                    />
                    <Route
                        path='/program'
                        render={() => <Program />}
                    />
                    <Route 
                        path='/training-programs'
                        render={() => <TrainingProgram />}
                    />
                    <Route 
                        path='/training-programs'
                        render={() => <TrainingProgram />}
                    />
                    <Route 
                        path='/my-training'
                        render={() => <MyTrainingPrograms />}
                    />
                    <Route 
                        path='/statistics'
                        render={() => <Statistics />}
                    />
                    <Route 
                        path='/measurements'
                        render={() => <Measurements />}
                    />
                    <Route 
                        path='/program-form'
                        render={() => <ProgramForm />}
                    />
                </div>
            </div>
        </BrowserRouter>
    );
};

export default App;
