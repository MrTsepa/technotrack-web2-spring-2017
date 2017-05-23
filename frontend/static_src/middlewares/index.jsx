import { LOAD_POSTS_SUCCESS } from '../actions/posts.jsx';
import { LOAD_CHATS_SUCCESS } from '../actions/chats.jsx';
import { normalize, schema } from 'normalizr';

export const normalizer = store => next => action => {
    if (action.type == LOAD_POSTS_SUCCESS) {
        const user = new schema.Entity('users');
        const post = new schema.Entity('posts', {
            author: user
        });
        action.normResponce = normalize(action.responce.results, [post]);
        return next(action);
    } else if (action.type == LOAD_CHATS_SUCCESS) {
        const user = new schema.Entity('users');
        const message = new schema.Entity('messages');
        const chat = new schema.Entity('chats', {
            author: user,
            last_message: message
        });
        action.normResponce = normalize(action.responce.results, [chat]);
        console.log(action.normResponce);
        return next(action);
    } else {
        return next(action);
    }
  // console.log('dispatching', action)
  // let result = next(action)
  // console.log('next state', store.getState())
  // return result
};
