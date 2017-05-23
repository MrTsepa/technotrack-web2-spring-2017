import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

// import Chat from './Chat.jsx';
import ChatBrief from './ChatBrief.jsx';

import List from 'grommet/components/List';
import ListItem from 'grommet/components/ListItem';

import Loading from 'react-loading-animation';

import { fetchChats } from '../actions/chats.jsx';

class ChatListComponent extends React.Component {
    componentDidMount() {
        this.props.fetchChats();
    }

    render() {
        const chatList = this.props.chatList.map(
            id =>
            <ListItem key={ id } pad="small">
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
    isLoading: state.chats.isLoading
});

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({ fetchChats }, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(ChatListComponent);
