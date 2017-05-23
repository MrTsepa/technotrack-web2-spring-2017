import React from 'react';
import ReactDom from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from 'react-redux';
import initStore from './store.jsx';

import App from './components/App.jsx';
// import Feed from './components/Feed.jsx';
// import MyPage from './components/MyPage.jsx';
// import ChatList from './components/ChatList.jsx';

ReactDom.render(
    <Provider store={ initStore() }>
        <BrowserRouter>
            <App />
        </BrowserRouter>
    </Provider>,
    document.getElementById('root')
);
