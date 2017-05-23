import fetch from 'isomorphic-fetch';

export const ADD_CHAT = 'ADD_CHAT';
export const LOAD_CHATS = 'LOAD_CHATS';
export const LOAD_CHATS_SUCCESS = 'LOAD_CHATS_SUCCESS';
export const LOAD_CHATS_ERROR = 'LOAD_CHATS_ERROR';

export function addChat(chat) {
    return {
        type: ADD_CHAT,
        chat
    };
}

export function loadChats() {
    return {
        type: LOAD_CHATS,
    };
}

export function loadChatsSuccess(responce) {
    return {
        type: LOAD_CHATS_SUCCESS,
        responce
    };
}

export function loadChatsError() {
    return {
        type: LOAD_CHATS_ERROR,
    };
}

export function fetchChats() {
    return dispatch => {
        dispatch(loadChats());
        return fetch('/api/chats/', {
            headers: {
                'Authorization': 'Token fa8542303554342a41e11d64c5b94b8cbbe949c5'
            },
        })
            .then(responce => responce.json())
            .then(json => dispatch(loadChatsSuccess(json)));
    };
}
