import {
    LOAD_CHATS,
    LOAD_CHATS_SUCCESS,
    LOAD_CHATS_ERROR
} from '../actions/chats.jsx';
import update from 'react-addons-update';


const initialStore = {
    chatList: [],
    chats: {},
    messages: {},
    users: {},
    isLoading: false
};

export default function chats(store = initialStore, action) {
    switch (action.type) {
    case LOAD_CHATS:
        return update(store, {
            isLoading: { $set: true }
        });
    case LOAD_CHATS_SUCCESS:
        return update(store, {
            isLoading: { $set: false },
            chatList: { $set: action.normResponce.result },
            chats: { $merge: action.normResponce.entities.chats },
            messages: { $merge: action.normResponce.entities.messages },
            users: { $merge: action.normResponce.entities.users }
        });
    case LOAD_CHATS_ERROR:
        return update(store, {
            isLoading: { $set: false }
        });
    default:
        return store;
    }
}
