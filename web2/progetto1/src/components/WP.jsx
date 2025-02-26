import React, { useEffect, useState } from 'react';
import { Container, Table } from 'react-bootstrap';

const WP = () => {
  const [WP, setWP] = useState([]);

  useEffect(() => {
    const fetchWP = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8080/WP');
        const data = await response.json();
        setWP(data);
      } catch (error) {
        console.error('Errore nel recupero dei dati:', error);
      }
    };
    fetchWP();
  }, []);

  return (
    <Container className="mt-4">
      <h1>Lista Work Packages</h1>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Progetto</th>
            <th>Nome</th>
            <th>Inizio</th>
            <th>Fine</th>
          </tr>
        </thead>
        <tbody>
          {WP.map(WP => (
            <tr key={WP.id}>
              <td>{WP.id}</td>
              <td>{WP.progetto}</td>
              <td>{WP.nome}</td>
              <td>{WP.inizio}</td>
              <td>{WP.fine}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default WP;
