import React from 'react';
import classes from './Exercises.module.css';

import Tags from './Tags/Tags';
import {Col, Row} from 'antd';


const Exercises = (props) => {
    return (
        <div className={classes.exercises}>
            <Row justify='center'>
                <Col className={classes.tags}>
                    <Tags />
                </Col>
            </Row>
            <Row justify='space-between'>
                <Col>
                    <div className={classes.exercise}>
                        1. Подтягивания
                    </div>
                    <div className={classes.exercise}>
                        2. Отжимания широким хватом
                    </div>
                    <div className={classes.exercise}>
                        3. Отжимания на брусьях
                    </div>
                    <div className={classes.exercise}>
                        4. Выпады
                    </div>
                    <div className={classes.exercise}>
                        5. Присяд
                    </div>
                </Col>
                <Col>
                    <div className={classes.exercise}>
                        1. Подтягивания
                    </div>
                    <div className={classes.exercise}>
                        2. Отжимания широким хватом
                    </div>
                    <div className={classes.exercise}>
                        3. Отжимания на брусьях
                    </div>
                    <div className={classes.exercise}>
                        4. Выпады
                    </div>
                    <div className={classes.exercise}>
                        5. Присяд
                    </div>
                </Col>
                <Col>
                    <div className={classes.exercise}>
                        1. Подтягивания
                    </div>
                    <div className={classes.exercise}>
                        2. Отжимания широким хватом
                    </div>
                    <div className={classes.exercise}>
                        3. Отжимания на брусьях
                    </div>
                    <div className={classes.exercise}>
                        4. Выпады
                    </div>
                    <div className={classes.exercise}>
                        5. Присяд
                    </div>
                </Col>
            </Row>
        </div>
    );
}

export default Exercises;
