import React from 'react';
import PropTypes from 'prop-types';

import PostForm from './PostForm.jsx';
import PostList from './PostList.jsx';

import Box from 'grommet/components/Box';
import Columns from 'grommet/components/Columns';
import Image from 'grommet/components/Image';

import { OWNER } from '../mock_data.jsx';

class MyPageComponent extends React.Component {
    render () {
        return (
                <Columns
                    maxCount={ 2 }
                    masonry={ true }
                    justify="start"
                >
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
                </Columns>
        );
    }
}

MyPageComponent.propTypes = {
    postList: PropTypes.arrayOf(
        PropTypes.object
    )
};

export default MyPageComponent;
