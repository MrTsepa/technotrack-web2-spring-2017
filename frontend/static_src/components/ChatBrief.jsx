import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import { Card, CardHeader, CardText } from 'material-ui/Card';

class ChatBriefComponent extends React.Component {
    render() {
        const name = this.props.author.username;
        const avaSrc = this.props.avaSrc;
        return (
            <Card zDepth={ 2 }>
                <CardHeader
                    title={ name }
                    subtitle={ this.props.lastMessage.created }
                    avatar={ avaSrc }
                />
                <CardText>
                    { this.props.lastMessage.text }
                </CardText>
            </Card>
        );
    }
}

// ChatBriefComponent.propTypes = {
//     name: PropTypes.string,
//     avaSrc: PropTypes.string,
//     participants: PropTypes.arrayOf(
//         PropTypes.shape({
//             name:  PropTypes.string.isRequired,
//             avaSrc:  PropTypes.string,
//         })
//     ).isRequired,
//     lastMessage: PropTypes.shape({
//         content: PropTypes.string,
//         time: PropTypes.string,
//         owner: PropTypes.shape({
//             name:  PropTypes.string.isRequired,
//             avaSrc:  PropTypes.string,
//         }).isRequired,
//     }).isRequired
// };
ChatBriefComponent.propTypes = {
    id: PropTypes.number.isRequired
};

const mapStateToProps = (state, props) => {
    const lastMessageId = state.chats.chats[props.id].last_message;
    if (lastMessageId == null) {
        return {
            lastMessage: {text: '', created: ''},
            author: {username: ''}
        };
    }
    const lastMessage = state.chats.messages[lastMessageId];
    const author = state.chats.users[lastMessage.author];
    return {
        lastMessage,
        author
    };
};

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({}, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(ChatBriefComponent);
