import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// // Set up the proxy in your development environment
// import proxyManager from './net/proxy'; // Import the ProxyManager
// if (process.env.NODE_ENV === 'development') {
//   proxyManager.setupProxy(require('express')()); // Express server or your setup
// }

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <App />
  // <React.StrictMode>
  //   <App />
  // </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
