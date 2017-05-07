import { LOAD_POSTS_SUCCESS } from '../actions/posts.jsx';
import { normalize, schema } from 'normalizr';

export const normalizer = store => next => action => {
    if (action.type == LOAD_POSTS_SUCCESS) {
        const user = new schema.Entity('users');
        const post = new schema.Entity('posts', {
            author: user
        });
        action.normResponce = normalize(action.responce.results, [post]);
        return next(action);
    } else {
        return next(action);
    }
  // console.log('dispatching', action)
  // let result = next(action)
  // console.log('next state', store.getState())
  // return result
};
