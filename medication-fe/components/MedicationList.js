import React, { Component } from 'react'
import { Table } from 'reactstrap'
import NewMedicationModal from './NewMedicationModal'

class MedicationList extends Component {
    render() {
        const medications = this.props.medications;

        return (
            <Table dark>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Classification</th>
                        <th>Intention</th>
                        <th>Implications</th>
                        <th>Dose</th>
                        <th>Route</th>
                        <th>Frequency</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {!medications || medications.length <= 0 ? (
                        <tr>
                            <td colSpan='6' align='center'>
                                <b>Oops, no medication here yet</b>
                            </td>
                        </tr>
                    ) : (
                        medications.map(medication => {
                            <tr key={medication.pk}>
                                <td>{medication.name}</td>
                                <td>{medication.classification}</td>
                                <td>{medication.intention}</td>
                                <td>{medication.implications}</td>
                                <td>{medication.dose}</td>
                                <td>{medication.route}</td>
                                <td>{medication.frequency}</td>
                                <td align='center'>
                                    <NewMedicationModal
                                        create={false}
                                        medication={medication}
                                        resetState={this.props.resetState}
                                    />
                                </td>
                            </tr>
                        })
                    )}
                </tbody>
            </Table>
        )
    }
}

export default MedicationList;