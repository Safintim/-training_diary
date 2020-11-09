import React from 'react';
import NewProgram from './NewProgram/NewProgram';
import ProgramCard from './ProgramCard/ProgramCard';
import classes from './TrainingPrograms.module.css';
import {NavLink} from 'react-router-dom';




const TrainingPrograms = (props) => {
    return (
        <div className={classes.trainingPrograms}>
            <div className={classes.title}>
                Программы тренировок
            </div>
            <div className={classes.programs}>
                <ProgramCard />
                <ProgramCard />
               
                <NewProgram />
            </div>
        </div>
    );
}

export default TrainingPrograms;
