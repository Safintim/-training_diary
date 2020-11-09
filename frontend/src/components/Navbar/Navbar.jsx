import React from 'react';
import classes from './Navbar.module.css';




const Navbar = (props) => {
    return (
        <div className={classes.navbar}>
            <div className={classes.navMenu}>
                <div className={classes.navItem}>
                    Аккаунт
                    {/* Профиль/Выйти */}
                </div>
            </div>
        </div>
    );
}

export default Navbar;
