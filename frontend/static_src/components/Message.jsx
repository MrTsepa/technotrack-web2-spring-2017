import React from 'react';
import PropTypes from 'prop-types';

import { Card, CardHeader, CardText } from 'material-ui/Card';

class MessageComponent extends React.Component {
    render() {
        return (
            <Card className="post" zDepth={ 2 }>
                <CardHeader
                    title={ this.props.owner.name }
                    subtitle={ this.props.time }
                    avatar={ this.props.owner.avaSrc }
                />
                <CardText>
                    { this.props.content }
                </CardText>
            </Card>
        );
    }
}

MessageComponent.propTypes = {
    content: PropTypes.string.isRequired,
    time: PropTypes.string,
    owner: PropTypes.shape({
        name:  PropTypes.string.isRequired,
        avaSrc:  PropTypes.string,
    }).isRequired,
};

export default MessageComponent;
