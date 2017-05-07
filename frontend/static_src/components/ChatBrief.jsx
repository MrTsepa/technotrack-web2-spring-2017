import React from 'react';
import PropTypes from 'prop-types';

import { Card, CardHeader, CardText } from 'material-ui/Card';

class ChatBriefComponent extends React.Component {
    render() {
        const name = this.props.name ?
                        this.props.name :
                        this.props.lastMessage.owner.name;
        const avaSrc = this.props.avaSrc ?
                        this.props.avaSrc :
                        this.props.lastMessage.owner.avaSrc;
        return (
            <Card zDepth={ 2 }>
                <CardHeader
                    title={ name }
                    subtitle={ this.props.lastMessage.time }
                    avatar={ avaSrc }
                />
                <CardText>
                    { this.props.lastMessage.content }
                </CardText>
            </Card>
        );
    }
}

ChatBriefComponent.propTypes = {
    name: PropTypes.string,
    avaSrc: PropTypes.string,
    participants: PropTypes.arrayOf(
        PropTypes.shape({
            name:  PropTypes.string.isRequired,
            avaSrc:  PropTypes.string,
        })
    ).isRequired,
    lastMessage: PropTypes.shape({
        content: PropTypes.string,
        time: PropTypes.string,
        owner: PropTypes.shape({
            name:  PropTypes.string.isRequired,
            avaSrc:  PropTypes.string,
        }).isRequired,
    }).isRequired
};

export default ChatBriefComponent;
