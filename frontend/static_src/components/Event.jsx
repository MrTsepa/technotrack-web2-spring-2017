import React from 'react'

import PropTypes from 'prop-types';

import { Card, CardHeader, CardText, CardTitle } from 'material-ui/Card'

class EventComponent extends React.Component {
    render() {
        return (
            <Card zDepth={ 2 }>
                <CardHeader
                    title={ this.props.owner.name }
                    subtitle={ this.props.time }
                    avatar={ this.props.owner.avaSrc }
                />
                <CardTitle
                    title={ this.props.type }
                />
                <CardText>
                    { this.props.content }
                </CardText>
            </Card>
        );
    }
}

EventComponent.propTypes = {
    type: PropTypes.string.isRequired,
    content: PropTypes.string.isRequired,
    time: PropTypes.string,
    owner: PropTypes.shape({
        name:  PropTypes.string.isRequired,
        avaSrc:  PropTypes.string,
    }).isRequired,
    likescount: PropTypes.number,
};

export default EventComponent;
