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
    {name: 'myPage', text: 'My Page', path: '/my_page'},
    {name: 'chats', text: 'Chats', path: '/chats'}
];

class AppComponent extends React.Component {
    onMenuSelect = (itemName) => {
        this.props.selectPage(itemName);
    };

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
