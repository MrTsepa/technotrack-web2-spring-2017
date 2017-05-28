import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import { Card, CardHeader, CardText } from 'material-ui/Card';

class MessageComponent extends React.Component {
    render() {
        return (
            <Card className="post" zDepth={ 2 }>
                <CardHeader
                    title={ this.props.author.username }
                    subtitle={ this.props.updated }
                    avatar={ this.props.author.avaSrc ? this.props.author.avaSrc : '' }
                />
                <CardText>
                    { this.props.text }
                </CardText>
            </Card>
        );
    }
}

MessageComponent.propTypes = {
    id: PropTypes.number.isRequired
};

const mapStateToProps = (state, props) => {
    // console.log(props.id);
    // console.log(state.chats.messages);
    return {
        ...state.chats.messages[props.id],
        author: state.chats.users[state.chats.messages[props.id].author]
    };
};

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({}, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(MessageComponent);
