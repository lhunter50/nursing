import React, { Component } from "react";
import { Button, Modal, ModalHeader, ModalBody, } from 'reactstrap'
import NewMedicationForm from "./NewMedicationForm";

class NewMedicationModal extends Component {
    state = {
        modal: false
    }

    toggle = () => {
        this.setState(previous => ({
            modal: !previous.modal
        }));
    }

    
}