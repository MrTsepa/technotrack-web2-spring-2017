import React from 'react';
import PropTypes from 'prop-types';

import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import { Card, CardHeader, CardText, CardTitle } from 'material-ui/Card';

class PostComponent extends React.Component {
    render() {
        return (
            <Card className="post" zDepth={ 2 }>
                <CardHeader
                    title={ this.props.author.username }
                    subtitle={ this.props.updated }
                    avatar={ this.props.author.avaSrc ? this.props.author.avaSrc : '' }
                />
                {
                    this.props.title ?
                    <CardTitle
                        title={ this.props.title }
                    /> : undefined
                }
                <CardText>
                    { this.props.text }
                </CardText>
            </Card>
        );
    }
}

PostComponent.propTypes = {
    id: PropTypes.number.isRequired
};

const mapStateToProps = (state, props) => ({
    ...state.posts.posts[props.id],
    author: state.posts.users[state.posts.posts[props.id].author]
});

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({}, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(PostComponent);
