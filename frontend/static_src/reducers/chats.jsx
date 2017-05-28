import {
    LOAD_CHATS,
    LOAD_CHATS_SUCCESS,
    LOAD_CHATS_ERROR,
    LOAD_CHAT,
    LOAD_CHAT_SUCCESS,
    OPEN_CHAT,
    CLOSE_CHAT
} from '../actions/chats.jsx';
import update from 'react-addons-update';


const initialStore = {
    chatList: [],
    chats: {},
    messages: {},
    users: {},
    chatMessageList: {},
    isLoading: false,
    isChatOpened: false,
    currentChat: undefined,
    isChatLoading: false
};

export default function chats(store = initialStore, action) {
    switch (action.type) {
        case LOAD_CHATS:
            return update(store, {
                isLoading: { $set: true }
            });
        case LOAD_CHATS_SUCCESS:
            store = update(store, {
                isLoading: {$set: false},
                chatList: {$set: action.normResponce.result},
                chats: {$merge: action.normResponce.entities.chats},
                messages: {$merge: action.normResponce.entities.messages},
                users: {$merge: action.normResponce.entities.users}
            });
            const temp = {};
            for (let key in store.chatList) {
                const id = store.chatList[key];
                temp[id] = [store.chats[id].last_message]
            }
            return update(store, {
                chatMessageList: {$set: temp}
            });
        case LOAD_CHATS_ERROR:
            return update(store, {
                isLoading: { $set: false }
            });
        case LOAD_CHAT:
            return update(store, {
                isChatLoading: { $set: true }
            });
        case LOAD_CHAT_SUCCESS: {
            store = update(store, {
                isChatLoading: { $set: false},
                messages: {$merge: action.normResponce.entities.messages},
                users: {$merge: action.normResponce.entities.users},
            });
            if (store.currentChat) {
                store = update(store, {
                    chatMessageList: {
                        $merge: {
                            [store.currentChat]: Object.keys(action.normResponce.entities.messages)
                        }
                    }
                });
            }
            return store;
        }
        case OPEN_CHAT: {
            return update(store, {
                currentChat: { $set: action.id },
                isChatOpened: { $set: true }
            });
        }
        case CLOSE_CHAT: {
            return update(store, {
                currentChat: { $set: undefined },
                isChatOpened: { $set: false }
            });
        }
        default:
            return store;
    }
}
