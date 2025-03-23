import logo from './logo.svg';
import './App.css';

import React, { useState, useEffect } from "react";

function Card({ animal }) {
  return (
    <div className="card">
      <h2>{animal.name}</h2>
      <h3>{animal.type}</h3>
      <h3>{animal.id}</h3>
    </div>
  );
}

function App() {
  const [animals, setAnimals] = useState([]);

  useEffect(() => {
    fetch("/animals").then((res) => res.json()).then((data) => {
        setAnimals({id: data.id, name: data.name, type: data.type});
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Testing...</h1>
        <div>
          {animals.map((item, index) =>
            <Card key={index} animal={item} />
          )}
        </div>
      </header>
    </div>
  );
}

export default App;
