import { combineReducers } from 'redux';
import router from './router.jsx';
import posts from './posts.jsx';

export default combineReducers({
    router,
    posts
});
