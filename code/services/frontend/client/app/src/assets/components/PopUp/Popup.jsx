import React, { useState } from 'react';
import Modal from 'react-modal';

Modal.setAppElement('#root'); // Wymagane, aby określić element źródłowy dla dostępności

const InfoModal = ({ isOpen, closeModal, message }) => {
    return (
        <Modal 
            isOpen={isOpen}
            onRequestClose={closeModal}
            contentLabel="Informacja"
        >
            <h2>Informacja</h2>
            <p>{message}</p>
            <button onClick={closeModal}>Zamknij</button>
        </Modal>
    );
};

export default InfoModal;
