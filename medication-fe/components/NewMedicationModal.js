import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody, } from 'reactstrap'
import NewMedicationForm from "./NewMedicationForm";

class NewMedicationModal extends Component {
    
    // set initial state of modal to false (we dont want it open on load)
    state = {
        modal: false
    }

    // toggle state so we can open and close the modal
    toggle = () => {
        this.setState(previous => ({
            modal: !previous.modal
        }));
    }

    render() {
        const create = this.props.create;

        var title = 'Editing Medication';
        var button = <Button onClick={this.toggle}>Edit</Button>;
        if(create){
            title = "Creating New Medication";

            button= (
                <Button
                    color="primary"
                    className="float-right"
                    onClick={this.toggle}
                    style={{ minWidth: '200px'}}
                    >
                        Create New
                    </Button>
            )
        }

        return (
            <Fragment>
                {button}
                <Modal isOpen={this.state.modal} toggle={this.toggle}>
                    <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

                    <ModalBody>
                        <NewMedicationForm
                            resetState={this.props.resetState}
                            toggle={this.toggle}
                            medication={this.props.medication}
                        />
                    </ModalBody>
                </Modal>
            </Fragment>
        )
    }
}

export default NewMedicationModal;