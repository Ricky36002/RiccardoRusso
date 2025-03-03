import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const CustomNavbar = () => {
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand as={Link} to="/">My App</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/">Home</Nav.Link>
            <Nav.Link as={Link} to="/Assenze">Assenze</Nav.Link>
            <Nav.Link as={Link} to="/Persona">Persona</Nav.Link>
            <Nav.Link as={Link} to="/Progetto">Progetto</Nav.Link>
            <Nav.Link as={Link} to="/WP">WP</Nav.Link>
            {/* <Nav.Link as={Link} to="/AttivitaProgettuali">AttivitaProgetto</Nav.Link> */}
            <Nav.Link as={Link} to="/AttivitanonProgettuali">AttivitanonProgettuali</Nav.Link>
            
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default CustomNavbar;