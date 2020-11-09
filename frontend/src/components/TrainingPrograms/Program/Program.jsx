import React from 'react';
import classes from './Program.module.css';

import { Typography, Row, Col } from 'antd';

const { Text, Title } = Typography;

const Program = (props) => {
    return (
        <div>
            <Row justify='center'>
                <Col span={24} style={{ display: 'inline-flex', justifyContent: 'center'}}>
                    <Title level={2}>Ноги</Title>
                </Col>
            </Row>
            <Row justify='center'>
                <Col span={24} style={{ display: 'inline-flex', justifyContent: 'center'}}>
                    <div className={classes.img}>
                        <img src='/logo192.png' alt='Картинка' />
                    </div>
                </Col>
            </Row>
            <div className={classes.info}>
                <Row justify='center'>
                    <Col span={12}>
                        <div className={classes.description}>
                            <Text>
                                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Alias eum excepturi ipsam maiores necessitatibus optio suscipit. Cupiditate ducimus ea earum eveniet ipsum, molestiae mollitia nam nisi nobis nulla numquam obcaecati provident quaerat qui quia repellat sunt temporibus velit vitae voluptatem! Ab aliquid consectetur culpa cum deleniti dolorum eius fugiat, maiores nihil nobis odit porro possimus quae qui quisquam recusandae sed?
                            </Text>
                        </div>
                    </Col>
                </Row>
                <Row justify='center'>
                    <Col>
                            <div>1. Присяд</div>
                            <div>2. жим ногами</div>
                            <div>3. разгибание ног</div>
                            <div>4. сгибание ног</div>

                    </Col>
                </Row>
                <Row justify='center'>
                    <Col>
                        <button>Изменить</button>
                        <button>Удалить</button>
                    </Col>
                </Row>
            </div>

        </div>
    );
};


export default Program;
