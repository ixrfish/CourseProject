import React from 'react';
import ReactDOM from 'react-dom/client';
import './frontend/index.css';
import EaterPageWithNavigate from './frontend/EaterPage';
import EaterResult from './frontend/EaterResult';
import reportWebVitals from './frontend/reportWebVitals';
import {BrowserRouter as Router} from 'react-router-dom';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
        <EaterPageWithNavigate />
    </Router>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
