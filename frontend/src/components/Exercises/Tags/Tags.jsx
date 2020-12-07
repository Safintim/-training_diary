import React from 'react';
import { Tag } from 'antd';
import classes from './Tags.module.css'

const { CheckableTag } = Tag;

const tagsData = ['Грудь', 'Ноги', 'Плечи', 'Икры', 'Руки', 'Пресс', 'Со своим весом'];

class Tags extends React.Component {
    state = {
        selectedTags: ['Books'],
    };

    handleChange(tag, checked) {
        const { selectedTags } = this.state;
        const nextSelectedTags = checked ? [...selectedTags, tag] : selectedTags.filter(t => t !== tag);
        console.log('You are interested in: ', nextSelectedTags);
        this.setState({ selectedTags: nextSelectedTags });
    }

    render() {
        const { selectedTags } = this.state;
        return (
            <div>
                {tagsData.map(tag => (
                    <CheckableTag
                        key={tag}
                        checked={selectedTags.indexOf(tag) > -1}
                        onChange={checked => this.handleChange(tag, checked)}
                        className={classes.tag}
                    >
                        {tag}
                    </CheckableTag>
                ))}
            </div>
        );
    }
}

const Ta

export default Tags;
