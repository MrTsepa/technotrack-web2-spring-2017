import React from 'react';
import ReactDom from 'react-dom';

import { Provider } from 'react-redux';
import initStore from './store.jsx';

import App from './components/App.jsx';

ReactDom.render(
    <Provider store={ initStore() }>
        <App />
    </Provider>,
    document.getElementById('root')
);
