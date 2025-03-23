import logo from './logo.svg';
import './App.css';

import React, { useState, useEffect } from "react";

function App() {
  const [data, setdata] = useState({
    id: 0,
    name: "",
    type: "",
  });

  useEffect(() => {
    fetch("/animals/2").then((res) =>
      res.json().then((data) => {
        setdata({
          id: data.id,
          name: data.name,
          type: data.type,
        });
      })
    );
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Testing...</h1>
        {}
        <p>{data.id}</p>
        <p>{data.name}</p>
        <p>{data.type}</p>
      </header>
    </div>
  );
}

export default App;
