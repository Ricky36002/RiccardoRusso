import React, { useEffect, useState } from 'react';
import { Container, Table } from 'react-bootstrap';

const AttivitaProgettuali = () => {
  const [AttivitaProgettuali, setAttivitaProgettuali] = useState([]);

  useEffect(() => {
    const fetchAttivitaProgettuali = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8080/AttivitaProgettuali');
        const data = await response.json();
        setAttivitaProgettuali(data);
      } catch (error) {
        console.error('Errore nel recupero dei dati:', error);
      }
    };
    fetchAttivitaProgettuali();
  }, []);

  return (
    <Container className="mt-4">
      <h1>Lista Attività Progettuali</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Persona</th>
            <th>Progetto</th>
            <th>WP</th>
            <th>Giorno</th>
            <th>Tipo</th>
            <th>Ore Durata</th>
          </tr>
        </thead>
        <tbody>
          {AttivitaProgettuali.map(item => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.persona}</td>
              <td>{item.progetto}</td>
              <td>{item.wp}</td>
              <td>{item.giorno}</td>
              <td>{item.tipo}</td>
              <td>{item.oreDurata}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default AttivitaProgettuali;
