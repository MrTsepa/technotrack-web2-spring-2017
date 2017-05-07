import React from 'react';
import PropTypes from 'prop-types';

// import Chat from './Chat.jsx';
import ChatBrief from './ChatBrief.jsx';

import List from 'grommet/components/List';
import ListItem from 'grommet/components/ListItem';


class ChatListComponent extends React.Component {
    render() {
        const chatList = this.props.chatList.map(
            chat =>
            <ListItem key={ chat.id } pad="small">
                <ChatBrief
                    { ...chat }
                />
            </ListItem>
        );
        return (
            <List>
                { chatList }
            </List>
        );
    }
}

ChatListComponent.propTypes = {
    chatList: PropTypes.arrayOf(PropTypes.shape(ChatBrief.propTypes)),
};

export default ChatListComponent;
