import React from 'react';
import {Button, Form, FormGroup, Input, Label} from 'reactstrap';

import axios from 'axios'

class NewMedicationForm extends React.Component {
    state={
        pk:0,
        name:'',
        classification:'',
        implications:'',
        dose:'',
        route:'',
        frequency:'',
    }
}