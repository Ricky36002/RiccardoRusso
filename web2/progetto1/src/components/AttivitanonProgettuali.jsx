import React, { useEffect, useState } from 'react';
import { Container, Table } from 'react-bootstrap';

const AttivitanonProgettuali = () => {
  const [AttivitanonProgettuali, setAttivitanonProgettuali] = useState([]);

  useEffect(() => {
    const fetchAttivitanonProgettuali = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8080/AttivitanonProgettuali');
        const data = await response.json();
        setAttivitanonProgettuali(data);
      } catch (error) {
        console.error('Errore nel recupero dei dati:', error);
      }
    };
    fetchAttivitanonProgettuali();
  }, []);

  return (
    <Container className="mt-4">
      <h1>Lista Attività Non Progettuali</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Persona</th>
            <th>Tipo</th>
            <th>Giorno</th>
            <th>Ore Durata</th>
          </tr>
        </thead>
        <tbody>
          {AttivitanonProgettuali.map(item => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.persona}</td>
              <td>{item.tipo}</td>
              <td>{item.giorno}</td>
              <td>{item.oreDurata}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default AttivitanonProgettuali;
