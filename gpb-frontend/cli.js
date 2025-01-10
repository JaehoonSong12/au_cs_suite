/**
 * @file server.js
 * @description Express-based server for serving a React frontend, proxying API requests, 
 *              and providing console output with kleur for enhanced readability.
 */

const fs = require('fs');
const https = require('https');
const cors = require('cors');
const ip = require('ip');

const express = require('express');
const path = require('path');
const kleur = require('kleur');
const { createProxyMiddleware } = require('http-proxy-middleware');

/**
 * Utility: Draw a message in a styled box for better console readability
 * @param {string} message - The message to display
 * @returns {string} The styled box containing the message
 */
function drawBox(message) {
  const lines = message.split('\n');
  const width = Math.max(...lines.map((line) => line.length));
  const horizontalLine = '─'.repeat(width + 4);
  const top = `┌${horizontalLine}┐`;
  const bottom = `└${horizontalLine}┘`;
  const middle = lines.map((line) => `│  ${line.padEnd(width)}  │`).join('\n');
  return `${top}\n${middle}\n${bottom}`;
}

const app = express();
const PORT = process.env.PORT || 3000; // Port to run the server
// HTTPS options: Replace with your SSL certificates
const httpsOptions = {
  key: fs.readFileSync(path.join(__dirname, 'certs', 'key.pem')), // Path to SSL private key
  cert: fs.readFileSync(path.join(__dirname, 'certs', 'cert.pem')), // Path to SSL certificate
};

// Middleware: Set Content Security Policy (CSP) for secure camera access
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; media-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';"
  );
  next();
});

// Middleware: Enable CORS for cross-origin requests (adjust origin if needed)
app.use(cors({ origin: '*' }));


/**
 * Proxy setup for '/upload' endpoint.
 * Proxies requests to the backend server at 'http://127.0.0.1:8000'.
 * Logs requests, responses, and errors for debugging.
 */
app.use(
  '/upload',
  createProxyMiddleware({
    target: 'http://127.0.0.1:8000',
    changeOrigin: true,
    onProxyReq: (proxyReq, req) => {
      console.log(`[UPLOAD] Proxying request: ${req.method} ${req.url}`);
    },
    onProxyRes: (proxyRes, req) => {
      console.log(`[UPLOAD] Response received: ${proxyRes.statusCode} ${req.url}`);
    },
    onError: (err) => {
      console.error(`[UPLOAD] Proxy error: ${err.message}`);
    },
  })
);

/**
 * Proxy setup for '/images' endpoint.
 * Proxies requests to the backend server at 'http://127.0.0.1:8000'.
 * Logs requests, responses, and errors for debugging.
 */
app.use(
  '/images',
  createProxyMiddleware({
    target: 'http://127.0.0.1:8000',
    changeOrigin: true,
    onProxyReq: (proxyReq, req) => {
      console.log(`[IMAGES] Proxying request: ${req.method} ${req.url}`);
    },
    onProxyRes: (proxyRes, req) => {
      console.log(`[IMAGES] Response received: ${proxyRes.statusCode} ${req.url}`);
    },
    onError: (err) => {
      console.error(`[IMAGES] Proxy error: ${err.message}`);
    },
  })
);

/**
 * Serves static files from the React build directory.
 * @example Access the React app at 'http://localhost:PORT/'
 */
app.use(express.static(path.join(__dirname, 'build')));

/**
 * Catch-all handler for React routing.
 * Redirects all non-API requests to the React app's index.html.
 */
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(`[ERROR] ${err.message}`);
  res.status(500).send('Server Error');
});

// Create and start the HTTPS server
const server = https.createServer(httpsOptions, app);

/**
 * Starts the Express server.
 * Logs local and network URLs using kleur and for enhanced output.
 */
app.listen(PORT, () => {
  const localUrl = `https://localhost:${PORT}`;
  const networkUrl = `https://${ip.address()}:${PORT}`;

  console.log(
    'This is an obtimized production build (offical deployment)\n'
    +
    drawBox(
      `${kleur.green().bold('Serving!')}\n\n` +
        `${kleur.bold('- Local:')}    ${kleur.cyan(localUrl)}\n` +
        `${kleur.bold('- Network:')}  ${kleur.cyan(networkUrl)}\n\n` +
        `${kleur.yellow('Press Ctrl+C to stop the server.')}`,
      { padding: 1, margin: 1, borderStyle: 'double', borderColor: 'cyan' }
    )
  );
});



/**
 * Choosing the Right Method to Serve Your React Application:
 *
 * @description This section explains two ways to serve a React app in production:
 * 1. `server.js`: A custom backend solution with Express.js.
 * 2. `serve`: A simpler static file server.
 *
 * @method server.js
 * - Ideal for projects requiring backend features such as:
 *   - API proxying
 *   - Server-side rendering (SSR)
 *   - Dynamic data handling
 * - Offers flexibility for future enhancements.
 * - Requires setting up a Node.js server (e.g., using Express).
 *
 * @method serve
 * - Best for lightweight, static file serving.
 * - Serves pre-built files from the `build` folder.
 * - Easy to set up, ideal for apps with no backend logic.
 *
 * @example
 * // Use server.js for backend features:
 * node server.js
 *
 * // Use serve for static file hosting:
 * npm install -g serve
 * serve -s build
 */