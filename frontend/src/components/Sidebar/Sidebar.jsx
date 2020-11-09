import React from 'react';
import { NavLink } from 'react-router-dom';
import classes from './Sidebar.module.css';


const Sidebar = (props) => {
    return (
        <div className={classes.sidebar}>
            <div className={classes.title}>
                Дневник тренировок
            </div>
            <div className={classes.sideMenu}>
                <div className={classes.menuLink}>
                    <NavLink to='/blog'>Блог</NavLink>
                </div>
                <div className={classes.menuLink}>
                    <NavLink to='/exercises'>Упражнения</NavLink>
                </div>
                <div className={classes.menuLink}>
                    <NavLink to='/exercise'>Упражнение</NavLink>
                </div>
                <div className={classes.menuLink}>
                    <NavLink to='/exercise-form'>Создание упражнения</NavLink>
                </div>
                <div className={classes.menuLink}>
                    <NavLink to='/program-form'>Создание программы</NavLink>
                </div>
                <div className={classes.menuLink}>
                    <NavLink to='/training-programs'>Все тренировки</NavLink>
                </div>
                <div className={classes.menuLink}>
                    <NavLink to='/program'>Программа</NavLink>
                </div>
                <div className={classes.menuLink}>
                    <NavLink to='/my-training'>Мои тренировки</NavLink>
                </div>
                <div className={classes.menuLink}>
                    <NavLink to='/statistics'>Статистика</NavLink>
                </div>
                <div className={classes.menuLink}>
                    <NavLink to='/measurements'>Замеры</NavLink>
                </div>
                <div className={classes.menuLink}>
                    <NavLink to='/measurements'>Подсчет каллорий</NavLink>
                </div>

            </div>
        </div>
    );
}

export default Sidebar;
