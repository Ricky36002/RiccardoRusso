import React, { useEffect, useState } from 'react';
import { Container, Table } from 'react-bootstrap';

const Assenze = () => {
  const [Assenze, setAssenze] = useState([]);

  useEffect(() => {
    const fetchAssenze = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8080/Assenze');
        const data = await response.json();
        setAssenze(data);
      } catch (error) {
        console.error('Errore nel recupero dei dati:', error);
      }
    };
    fetchAssenze();
  }, []);

  return (
    <Container className="mt-4">
      <h1>Lista Assenze</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Persona</th>
            <th>Tipo</th>
            <th>Giorno</th>
          </tr>
        </thead>
        <tbody>
          {Assenze.map(assenza => (
            <tr key={assenza.id}>
              <td>{assenza.id}</td>
              <td>{assenza.persona}</td>
              <td>{assenza.tipo}</td>
              <td>{assenza.giorno}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default Assenze;
