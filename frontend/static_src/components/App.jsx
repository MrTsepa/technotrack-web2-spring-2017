import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { BrowserRouter, Route, IndexRoute } from 'react-router-dom';
import { selectPage } from '../actions/router.jsx';

import 'grommet/scss/vanilla/index.scss';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import App from 'grommet/components/App';

import Layout from './Layout.jsx'
import Feed from './Feed.jsx'
import MyPage from './MyPage.jsx'
import Chat from './Chat.jsx'
import ChatList from './ChatList.jsx'

const MENU_ITEMS = [
    {name: 'feed', text: 'Feed', path: '/'},
    {name: 'myPage', text: 'MyPage', path: '/my_page'},
    {name: 'chats', text: 'Chats', path: '/chats'}
]

const OWNER = {
    name: 'Stas',
    avaSrc: '',
};

const MESSAGE = {
    owner: OWNER,
    time: "19 Feb at 12:01 pm",
    content: "Lorem ipsum dolor sit amet, nibh volutpat tincidunt, risus nec laborum maecenas a lectus, ullamcorper nunc congue ligula neque",
    likescount: 200,
}

const MESSAGE_LIST = [
    {...MESSAGE, id: 0},
    {...MESSAGE, id: 1},
    {...MESSAGE, id: 2},
    {...MESSAGE, id: 3, content: 'Short Message'},
    {...MESSAGE, id: 4},
    {...MESSAGE, id: 5},
    {...MESSAGE, id: 6},
    {...MESSAGE, id: 7},
    {...MESSAGE, id: 8},
    {...MESSAGE, id: 9},
    {...MESSAGE, id: 10},
    {...MESSAGE, id: 11},
    {...MESSAGE, id: 12},
    {...MESSAGE, id: 13},
]

const CHAT = {
    name: 'Chat',
    avaSrc: '',
    messages: MESSAGE_LIST,
    lastMessage: MESSAGE,
    participants: [OWNER, OWNER, OWNER]
}

const CHAT_LIST = [
    {...CHAT, id: 0},
    {...CHAT, id: 1},
    {...CHAT, id: 2},
    {...CHAT, id: 3},
    {...CHAT, id: 4},
    {...CHAT, id: 5},
    {...CHAT, id: 6},
]



class AppComponent extends React.Component {
    onMenuSelect = (itemName) => {
        this.props.selectPage(itemName);
    }

    render() {
        let page;
        switch (this.props.currentPage) {
            case 'feed':
                page = <Feed />;
                break;
            case 'myPage':
                page =  <MyPage />;
                break;
            case 'chats':
                page = <ChatList />;
                break;
        }
        return (
        <MuiThemeProvider>
            <App>
                <Layout onSelect={ this.onMenuSelect } menuItems={ MENU_ITEMS }>
                {/*
                    <Route exact={true} path='/' component={Feed} />
                    <Route path='/my_page' component={MyPage} />
                    <Route path='/chats/' component={ChatList} />
                */}
                    {/* this.props.children */}
                    { page }
                </Layout>
            </App>
        </MuiThemeProvider>
        );
    }
}

const mapStateToProps = state => ({
    currentPage: state.router.currentPage,
});

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({ selectPage }, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(AppComponent);
