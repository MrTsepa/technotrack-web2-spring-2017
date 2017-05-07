import React, { PropTypes } from 'react';

import Event from './Event.jsx'

import List from 'grommet/components/List';
import ListItem from 'grommet/components/ListItem';

const OWNER = {
    name: 'Stas',
    avaSrc: '',
};

const EVENT_LIST = [
    {id: 1, type: 'post', content: 'new post', owner: OWNER},
    {id: 2, type: 'friendship', content: 'user1 to user2', owner: OWNER},
    {id: 3, type: 'post', content: 'new post', owner: OWNER},
    {id: 4, type: 'achievement', content: 'AAAAAAAAAa', owner: OWNER},
    {id: 5, type: 'post', content: 'new post', owner: OWNER},
]

class FeedComponent extends React.Component {
    render () {
        const eventList = EVENT_LIST.map(
            event =>
            <ListItem key={ event.id }>
                <Event
                    { ...event }
                />
            </ListItem>
        );
        return (
            <List className="feed">
                { eventList }
            </List>
        );
    }
}



export default FeedComponent;
