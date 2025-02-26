import React, { useEffect, useState } from 'react';
import { Container, Table } from 'react-bootstrap';

const Progetto = () => {
  const [Progetto, setProgetto] = useState([]);

  useEffect(() => {
    const fetchProgetto = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8080/Progetto');
        const data = await response.json();
        setProgetto(data);
      } catch (error) {
        console.error('Errore nel recupero dei dati:', error);
      }
    };
    fetchProgetto();
  }, []);

  return (
    <Container className="mt-4">
      <h1>Lista Progetto</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Inizio</th>
            <th>Fine</th>
            <th>Budget</th>
          </tr>
        </thead>
        <tbody>
          {Progetto.map(progetto => (
            <tr key={progetto.id}>
              <td>{progetto.id}</td>
              <td>{progetto.nome}</td>
              <td>{progetto.inizio}</td>
              <td>{progetto.fine}</td>
              <td>{progetto.budget} €</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default Progetto;
