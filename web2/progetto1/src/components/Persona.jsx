import React, { useEffect, useState } from 'react';
import { Container, Table } from 'react-bootstrap';

const Persona = () => {
  const [Persona, setPersona] = useState([]);

  useEffect(() => {
    const fetchPersona = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8080/Persona');
        const data = await response.json();
        setPersona(data);
      } catch (error) {
        console.error('Errore nel recupero dei dati:', error);
      }
    };
    fetchPersona();
  }, []);

  return (
    <Container className="mt-4">
      <h1>Lista Persona</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Cognome</th>
            <th>Posizione</th>
            <th>Stipendio</th>
          </tr>
        </thead>
        <tbody>
          {Persona.map(persona => (
            <tr key={persona.id}>
              <td>{persona.id}</td>
              <td>{persona.nome}</td>
              <td>{persona.cognome}</td>
              <td>{persona.posizione}</td>
              <td>{persona.stipendio} €</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default Persona;
