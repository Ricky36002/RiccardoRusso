import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CustomNavbar from './components/Navbar';
import Home from './components/Home';
import Persona from './components/Persona';
import Progetto from './components/Progetto';
import WP from './components/WP';
import Assenze from './components/Assenze';
import AttivitaProgetto from './components/AttivitaProgettuali';
import AttivitanonProgettuali from './components/AttivitanonProgettuali';

const App = () => {
  return (
    <Router>
      <CustomNavbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Persona" element={<Persona />} />
        <Route path="/Progetto" element={<Progetto />} />
        <Route path="/WP" element={<WP />} />
        <Route path="/Assenze" element={<Assenze />} />
        <Route path="/AttivitaProgettuali" element={<AttivitaProgetto />} />
        <Route path="/AttivitanonProgettuali" element={<AttivitanonProgettuali />} />
        
      </Routes>
    </Router>
  );
};

export default App;