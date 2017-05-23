import { combineReducers } from 'redux';
import router from './router.jsx';
import posts from './posts.jsx';
import chats from './chats.jsx';

export default combineReducers({
    router,
    posts,
    chats
});
