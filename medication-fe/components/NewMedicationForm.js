import React from 'react';
import {Button, Form, FormGroup, Input, Label} from 'reactstrap';

import axios from 'axios'

import { API_URL } from '../src/constants'

class NewMedicationForm extends React.Component {
    //set initial state
    state={
        pk:0,
        name:'',
        classification:'',
        implications:'',
        dose:'',
        route:'',
        frequency:'',
    }

    componentDidMount() {
        if (this.props.medication) {
            const { pk, name, classification, implications, dose, route, frequency } = this.props.medication;
            this.setState({ pk, name, classification, implications, dose, route, frequency });
        }
    }

    onChange = e => {
        this.setState({ [e.target.name] : e.target.value }) 
    };

    createMedication = e => {
        e.preventDefault();
        axios.put(API_URL + this.state.pk, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        })
    }

    editMedication = e => {
        e.preventDefault();
        axios.put(API_URL + this.state.pk, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        })
    }

    defaultIfEmpty = value => {
        return value == "" ? "" : value;
    }

    render() {
        <Form onSubmit={this.props.medication ? this.editMedication : this.createMedication}>
            <FormGroup>
                <Label for='name'>Name:</Label>
                <Input 
                    type='text'
                    name='name'
                    onChange={this.onChange}
                    value={this.defaultIfEmpty(this.state.name)}
                />
            </FormGroup>
            
        </Form>
    }
}