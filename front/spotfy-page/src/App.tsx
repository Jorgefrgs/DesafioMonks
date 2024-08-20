import React from 'react';
import './App.css';
import { Card } from './components/Card';

function App() {
  return (
    <div className="App">
      <img
        src="https://media.licdn.com/dms/image/v2/D4D0BAQHmt5xzLo3ZBQ/company-logo_200_200/company-logo_200_200/0/1721310455635/media_monks_brasil_logo?e=2147483647&v=beta&t=i4aHdLYEyudhGersOxSWzZLorTU17kEsIAK7JHd6Tt8" 
        alt="Logo"
        className="App-logo"
      />
      <header className="App-header">
        <h1>Top Pop Artists</h1>
      </header>
      <Card />
    </div>
  );
}

export default App;
