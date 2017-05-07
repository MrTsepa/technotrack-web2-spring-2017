import { SELECT_PAGE } from '../actions/router.jsx';

export default function router(store = { currentPage: 'feed' }, action) {
    switch (action.type) {
    case SELECT_PAGE:
        return { currentPage: action.page };
    default:
        return store;
    }
}
