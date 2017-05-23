import React from 'react';

import Article from 'grommet/components/Article';
import Header from 'grommet/components/Header';
import Split from 'grommet/components/Split';
import Sidebar from 'grommet/components/Sidebar';
import Menu from 'grommet/components/Menu';
import Box from 'grommet/components/Box';
import Button from 'grommet/components/Button';
import Anchor from 'grommet/components/Anchor';

import AccessibleIcon from 'grommet/components/icons/base/Accessible'

class LayoutComponent extends React.Component {
    onSelect = (name) => {
        this.props.onSelect(name);
    }

    render() {
        const anchors = this.props.menuItems.map(
            e =>
            <Anchor
                onClick={ this.onSelect.bind(this, e.name) }
                name={ e.name }
                key={ e.name }
                label={ e.text }
                path={ e.path }
            />
        )
        return (
            <div>
                <Header
                    pad="medium"
                    colorIndex='neutral-1'>
                    <AccessibleIcon size="medium" />
                </Header>
                <Split flex='right'>
                    <Sidebar
                        pad="small"
                        size="xsmall"
                        colorIndex='neutral-1-a'>
                        <Menu
                            align="center">
                            { anchors }
                        </Menu>
                    </Sidebar>
                    <Box justify='center'
                         align='center'
                         colorIndex='light-2'
                         >
                        { this.props.children }
                    </Box>
                </Split>
            </div>
        );
        // return (
        //     <div>
        //         <Header colorIndex='neutral-1'>
        //             Header
        //         </Header>
        //         <Split flex='right'>
        //             <Box justify='center'
        //                  align='center'
        //                  colorIndex='neutral-2'>
        //                 { buttons }
        //             </Box>
        //             <Box justify='center'
        //                  align='center'
        //                  colorIndex='light-2'>
        //                 { this.props.children }
        //             </Box>
        //         </Split>
        //     </div>
        // );
    }

}

LayoutComponent.propTypes = {
    menuItems: React.PropTypes.arrayOf(
        React.PropTypes.shape({
            name: React.PropTypes.string,
            text: React.PropTypes.string,
        })
    ),
    onSelect: React.PropTypes.func
};

export default LayoutComponent;
