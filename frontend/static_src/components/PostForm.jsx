import React from 'react';
import PropTypes from 'prop-types';

import Paper from 'material-ui/Paper'
import { Card, CardHeader } from 'material-ui/Card'

import Box from 'grommet/components/Box';
import Form from 'grommet/components/Form';
import FormField from 'grommet/components/FormField';
import TextInput from 'grommet/components/TextInput';
import Footer from 'grommet/components/Footer';
import Button from 'grommet/components/Button';

class PostFormComponent extends React.Component {
    state = {
        title: '',
        content: '',
    };

    onCreate = (e) => {
        e.preventDefault();
        this.props.onCreate({
            owner: {
                name: 'Stas2'
            },
            ...this.state,
        });
    };

    onChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value,
        });
    };

    render() {
        return (
            <Card>
                <Box pad="small">
                    <Form>
                        <FormField label="Title">
                            <TextInput
                                name="title"
                                onDOMChange = { this.onChange }/>
                        </FormField>
                        <FormField label="Text">
                            <TextInput
                                name="content"
                                onDOMChange = { this.onChange }/>
                        </FormField>
                        <Footer pad={{"vertical": "medium"}}>
                            <Button label='Create'
                                type='submit'
                                primary={true}
                                onClick={ this.onCreate } />
                        </Footer>
                    </Form>
                </Box>
            </Card>
        );
    }
}

PostFormComponent.propTypes = {
    onCreate: PropTypes.func.isRequired,
    owner: PropTypes.shape({
        name:  PropTypes.string.isRequired,
        avaSrc:  PropTypes.string,
    }).isRequired,
};

export default PostFormComponent;
