import React from 'react';
import PropTypes from 'prop-types';

import Message from './Message.jsx';

import List from 'grommet/components/List';
import ListItem from 'grommet/components/ListItem';

class ChatComponent extends React.Component {
    render() {
        const messageList = this.props.messageList.map(
            message =>
            <ListItem key={ message.id } pad="small">
                <Message {...message} />
            </ListItem>
        );
        return (
            <List>
                { messageList }
            </List>
        );
    }
}

ChatComponent.propTypes = {
    messageList: PropTypes.arrayOf(PropTypes.shape(Message.propTypes)),
};

export default ChatComponent;
