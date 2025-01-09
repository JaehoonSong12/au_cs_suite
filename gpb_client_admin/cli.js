/**
 * @file server.js
 * @description Express-based server for serving a React frontend, proxying API requests, 
 *              and providing console output with kleur for enhanced readability.
 */
const express = require('express');
const path = require('path');
const kleur = require('kleur');
const { createProxyMiddleware } = require('http-proxy-middleware');

function drawBox(message) {
  const lines = message.split('\n');
  const width = Math.max(...lines.map(line => line.length));
  const horizontalLine = '─'.repeat(width + 4);
  const top = `┌${horizontalLine}┐`;
  const bottom = `└${horizontalLine}┘`;
  const middle = lines.map(line => `│  ${line.padEnd(width)}  │`).join('\n');
  return `${top}\n${middle}\n${bottom}`;
}

const app = express();
const PORT = process.env.PORT || 3000; // Port to run the server

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

/**
 * Starts the Express server.
 * Logs local and network URLs using kleur and for enhanced output.
 */
app.listen(PORT, () => {
  const localUrl = `http://localhost:${PORT}`;
  const networkUrl = `http://${require('ip').address()}:${PORT}`;

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