import React, { Component } from 'react'
import { Col, Container, Row } from 'reactstrap'
import MedicationList from './MedicationList'
import NewMedicationModal from './NewMedicationModal'

import axios from 'axios'

import { API_URL } from '../src/constants'

class Home extends Component {
    state = {
        medications: []
    }

    componentDidMount() {
        this.resetState()
    }

    getMedications = () => {
        axios.get(API_URL).then(res => this.setState({ medications: res.data}))
    }

    resetState = () => {
        this.getMedications()
    }

    render() {
        return(
            <Container style={{ marginTop: '20px' }}>
                <Row>
                    <Col>
                        <MedicationList
                            medications={this.state.medications}
                            resetState={this.resetState}
                        />
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <NewMedicationModal create={true} resetState={this.resetState} />
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default Home