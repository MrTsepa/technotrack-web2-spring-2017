import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import Post from './Post.jsx';

import List from 'grommet/components/List';
import ListItem from 'grommet/components/ListItem';

import Loading from 'react-loading-animation';

import { loadPosts, loadPostsSuccess, loadPostsError, fetchPosts } from '../actions/posts.jsx';

class PostListComponent extends React.Component {
    componentDidMount() {
        this.props.fetchPosts();
    }

    render() {
        const postList = this.props.postList.map(
            id =>
            <ListItem key={ id } pad="small">
                <Post id={ id } />
            </ListItem>
        );
        return (
            <div>
                <Loading isLoading={ this.props.isLoading}>
                </Loading>
                <List className="post-list">
                    { postList }
                </List>
            </div>
        );
    }
}

PostListComponent.propTypes = {
};

const mapStateToProps = state => ({
    postList: state.posts.postList,
    isLoading: state.posts.isLoading
});

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({ loadPosts, loadPostsSuccess, loadPostsError, fetchPosts }, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(PostListComponent);
