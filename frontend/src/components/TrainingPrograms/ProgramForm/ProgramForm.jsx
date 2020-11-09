import React from 'react';

import { Form, Input, Button } from 'antd';
import SelectExercise from './SelectExercise';
import classes from './ProgramForm.module.css';


const layout = {
    labelCol: {
        span: 8,
    },
    wrapperCol: {
        span: 16,
    },
};
const validateMessages = {
    required: '${label} обязательно!',
};


const Demo = () => {
    const onFinish = (values) => {
        console.log(values);
    };

    return (
        <Form {...layout} onFinish={onFinish} validateMessages={validateMessages}>
            <Form.Item
                name={['program', 'title']}
                label='Название'
                rules={[
                    {
                        required: true,
                    },
                ]}
            >
                <Input />
            </Form.Item>
            <Form.Item name={['program', 'description']} label='Описание'>
                <Input.TextArea />
            </Form.Item>
            <Form.Item wrapperCol={{ ...layout.wrapperCol, offset: 8 }}>
                <Button type="primary" htmlType="submit">
                    Submit
                </Button>
            </Form.Item>
            <Form.Item >
                <SelectExercise />
            </Form.Item>
        </Form>
    );
};



const ProgramForm = (props) => {
    return (
        <div className={classes.programForm}>
            <div className={classes.title}>
                Создание тренировки
            </div>
            <div className={classes.programForm}>
                <Demo />
            </div>
        </div>
    );
}

export default ProgramForm;
