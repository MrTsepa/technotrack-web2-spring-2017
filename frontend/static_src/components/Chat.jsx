import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import Message from './Message.jsx';

import List from 'grommet/components/List';
import ListItem from 'grommet/components/ListItem';
import Loading from 'react-loading-animation';


import { fetchChat, closeChat } from '../actions/chats.jsx';

class ChatComponent extends React.Component {
    componentDidMount() {
        this.props.fetchChat(this.props.id);
    }

    componentWillUnmount() {
        this.props.closeChat();
    }

    render() {
        const messageList = this.props.messageList.map(
            id =>
            <ListItem key={ id } pad="small">
                <Message id={ id } />
            </ListItem>
        );
        console.log(messageList);
        return (
            <div>
                <Loading isLoading={ this.props.isLoading }>
                </Loading>
                <List className="post-list">
                    { messageList }
                </List>
            </div>
        );
    }
}

ChatComponent.propTypes = {
    id: PropTypes.number.isRequired
};

const mapStateToProps = (state, props) => {
    // console.log(state.chats.chatMessageList);
    // console.log(props.id);
    return {
        messageList: state.chats.chatMessageList[props.id],
        isLoading: state.chats.isChatLoading
    };
};

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({ fetchChat, closeChat }, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(ChatComponent);
