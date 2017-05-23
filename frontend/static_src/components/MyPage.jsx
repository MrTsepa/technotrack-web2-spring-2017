import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

import {
    closePostModal
} from '../actions/posts.jsx';

import PostForm from './PostForm.jsx';
import PostList from './PostList.jsx';
import Post from './Post.jsx';

import ReactModal from 'react-modal';

import Box from 'grommet/components/Box';
import Columns from 'grommet/components/Columns';
import Image from 'grommet/components/Image';
import Button from 'grommet/components/Button';

import { OWNER } from '../mock_data.jsx';

class MyPageComponent extends React.Component {
    render () {
        return (
            <div>
                <Columns
                    maxCount={ 2 }
                    masonry={ true }
                    justify="start"
                >

                    <Box align="center">
                        <Box
                            pad="small"
                            size="large"
                            alignSelf="center"
                        >
                            <PostForm onCreate={ this.onCreate } owner={ OWNER } />
                        </Box>
                        <Box
                            size="large"
                            alignSelf="center">
                            <PostList />
                        </Box>
                    </Box>
                    <Box size="small"
                        align="start">
                        <Box align='center'
                            pad='medium'
                            margin='small'
                            colorIndex='light-3'>
                            <Image />
                        </Box>
                        <Box align='center'
                            pad='medium'
                            margin='small'
                            colorIndex='light-3'>
                            INFO ABOUT USER
                        </Box>
                    </Box>
                </Columns>
                <ReactModal
                        isOpen={ this.props.isPostModalOpened }
                    >
                    <Post id={ this.props.postModalId } />
                    <Button
                        margin='medium'
                        label="Close"
                        primary={ true }
                        onClick={this.props.closePostModal}
                        />
                </ReactModal>
            </div>
        );
    }
}

MyPageComponent.propTypes = {
};

const mapStateToProps = state => ({
    isPostModalOpened: state.posts.isModalOpened,
    postModalId: state.posts.modalId
});

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({
        closePostModal
    }, dispatch)
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(MyPageComponent);
