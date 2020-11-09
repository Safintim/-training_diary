import React from 'react';
import classes from './ProgramCard.module.css';
import {Card} from 'antd';





const ProgramCard = (props) => {
    return (
        <div className={classes.program}>


            <div className={classes.img}>
                <img src='/logo192.png' alt='Картинка' />
            </div>
            <div className={classes.info}>
                <div className={classes.title}>
                    Ноги
                </div>
                <div className={classes.description}>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Est facilis nesciunt facere? Est nemo laborum possimus nam nihil asperiores quaerat?
                </div>
                <div className={classes.btnStart}>
                    <button>Начать</button>
                </div>
            </div>
        </div>
    );
}

export default ProgramCard;
