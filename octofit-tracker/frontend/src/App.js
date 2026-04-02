import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import Leaderboard from './components/Leaderboard';

function App() {
  const codespaceNameEnv = process.env.REACT_APP_CODESPACE_NAME;
  const apiBaseUrl = codespaceNameEnv 
    ? `https://${codespaceNameEnv}-8000.app.github.dev/api`
    : 'http://localhost:8000/api';
  
  console.log(`API Base URL: ${apiBaseUrl}`);

  return (
    <Router>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <img src="/logo.png" alt="OctoFit" className="d-inline-block align-text-top me-2" height="40" />
            OctoFit Tracker
          </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <Link className="nav-link" to="/">Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container-fluid mt-4">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/activities" element={<Activities apiBaseUrl={apiBaseUrl} />} />
          <Route path="/teams" element={<Teams apiBaseUrl={apiBaseUrl} />} />
          <Route path="/users" element={<Users apiBaseUrl={apiBaseUrl} />} />
          <Route path="/workouts" element={<Workouts apiBaseUrl={apiBaseUrl} />} />
          <Route path="/leaderboard" element={<Leaderboard apiBaseUrl={apiBaseUrl} />} />
        </Routes>
      </div>
    </Router>
  );
}

function Home() {
  return (
    <div className="text-center mt-5">
      <h1 className="display-4">Welcome to OctoFit Tracker</h1>
      <p className="lead">Track your fitness goals and compete with friends!</p>
      <div className="mt-4">
        <p className="text-muted">Select a section from the navigation menu above to get started.</p>
      </div>
    </div>
  );
}

export default App;
