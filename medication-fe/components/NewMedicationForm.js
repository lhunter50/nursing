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

            <FormGroup>
                <Label for='classification'>Classification:</Label>
                <Input 
                    type='text'
                    name='classification'
                    onChange={this.onChange}
                    value={this.defaultIfEmpty(this.state.classification)}
                />
            </FormGroup>

            <FormGroup>
                <Label for='intention'>Intention:</Label>
                <Input 
                    type='text'
                    name='Intention'
                    onChange={this.onChange}
                    value={this.defaultIfEmpty(this.state.intention)}
                />
            </FormGroup>

            <FormGroup>
                <Label for='implications'>Implications:</Label>
                <Input 
                    type='text'
                    name='implications'
                    onChange={this.onChange}
                    value={this.defaultIfEmpty(this.state.implications)}
                />
            </FormGroup>

            <FormGroup>
                <Label for='dose'>Dose:</Label>
                <Input 
                    type='text'
                    name='dose'
                    onChange={this.onChange}
                    value={this.defaultIfEmpty(this.state.dose)}
                />
            </FormGroup>

            <FormGroup>
                <Label for='route'>Route:</Label>
                <Input 
                    type='text'
                    name='route'
                    onChange={this.onChange}
                    value={this.defaultIfEmpty(this.state.route)}
                />
            </FormGroup>

            <FormGroup>
                <Label for='frequency'>Frequency:</Label>
                <Input 
                    type='text'
                    name='frequency'
                    onChange={this.onChange}
                    value={this.defaultIfEmpty(this.state.frequency)}
                />
            </FormGroup>

            <Button>Send</Button>
        </Form>
    }
}

export default NewMedicationForm;