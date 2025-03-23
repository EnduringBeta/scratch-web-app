import logo from './logo.svg';
import './App.css';

import React, { useState, useEffect } from "react";

function App() {
  const [animal, setData] = useState({id: 0, name: "Getting name...", type: "Getting animal..."});

  useEffect(() => {
    fetch("/animals/2").then((res) => res.json()).then((data) => {
        console.log(data);
        setData({id: data.id, name: data.name, type: data.type});
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Testing...</h1>
        <p>{animal.id}</p>
        <p>{animal.name}</p>
        <p>{animal.type}</p>
      </header>
    </div>
  );
}

export default App;
