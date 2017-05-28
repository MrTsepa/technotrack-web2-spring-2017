import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import Chat from './Chat.jsx';
import ChatBrief from './ChatBrief.jsx';

import List from 'grommet/components/List';
import ListItem from 'grommet/components/ListItem';

import Loading from 'react-loading-animation';

import { fetchChats, openChat } from '../actions/chats.jsx';

class ChatListComponent extends React.Component {
    componentDidMount() {
        this.props.fetchChats();
    }

    render() {
        if (this.props.isChatOpened) {
            return (
                <Chat id={ this.props.currentChat } />
            )
        }
        const chatList = this.props.chatList.map(
            id =>
            <ListItem key={ id } pad="small"
                onClick={this.props.openChat.bind(this, id)}>
                <ChatBrief
                    id={ id }
                />
            </ListItem>
        );
        return (
            <div>
                <Loading isLoading={ this.props.isLoading }>
                </Loading>
                <List>
                    { chatList }
                </List>
            </div>
        );
    }
}

ChatListComponent.propTypes = {
};

const mapStateToProps = state => ({
    chatList: state.chats.chatList,
    isLoading: state.chats.isLoading,
    isChatOpened: state.chats.isChatOpened,
    currentChat: state.chats.currentChat
});

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({ fetchChats, openChat }, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(ChatListComponent);
