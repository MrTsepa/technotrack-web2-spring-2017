import { createStore, applyMiddleware, compose } from 'redux';
import reducers from './reducers/index.jsx';
import thunk from 'redux-thunk';
import { normalizer } from './middlewares/index.jsx';

function initStore() {
    return createStore(
        reducers,
        {},
        compose(
            applyMiddleware(thunk, normalizer),
            window.devToolsExtension()
        )
    );
}


export default initStore;
