import fetch from 'isomorphic-fetch';

export const ADD_POST = 'ADD_POST';
export const LOAD_POSTS = 'LOAD_POSTS';
export const LOAD_POSTS_SUCCESS = 'LOAD_POSTS_SUCCESS';
export const LOAD_POSTS_ERROR = 'LOAD_POSTS_ERROR';

export function addPost(post) {
    return {
        type: ADD_POST,
        post
    };
}

export function loadPosts() {
    return {
        type: LOAD_POSTS,
    };
}

export function loadPostsSuccess(responce) {
    return {
        type: LOAD_POSTS_SUCCESS,
        responce
    };
}

export function loadPostsError() {
    return {
        type: LOAD_POSTS_ERROR,
    };
}

export function fetchPosts() {
    return dispatch => {
        dispatch(loadPosts());
        return fetch('/api/posts/', {
            headers: {
                'Authorization': 'Token fa8542303554342a41e11d64c5b94b8cbbe949c5'
            },
        })
            .then(responce => responce.json())
            .then(json => dispatch(loadPostsSuccess(json)));
    };
}
