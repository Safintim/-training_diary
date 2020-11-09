import React from 'react';
import { NavLink } from 'react-router-dom';


import classes from './NewProgram.module.css';


const NewProgram = (props) => {
    return (
        <div className={classes.program}>
            <NavLink to='/program-form'>
                <div className={classes.img}>
                    Добавить тренировку
                    <img src='/plus.png' alt='Добавить тренировку' />
                </div>
            </NavLink>
        </div>
    );
}

export default NewProgram;
