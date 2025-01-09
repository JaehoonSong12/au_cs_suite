// src/net/proxy.js

const { createProxyMiddleware } = require('http-proxy-middleware');

class ProxyManager {
  constructor() {
    if (!ProxyManager.instance) {
      ProxyManager.instance = this;
    }
    return ProxyManager.instance;
  }

  setupProxy(app) {
    app.use(
      '/upload',
      createProxyMiddleware({
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        onProxyReq: (proxyReq, req, res) => {
          console.log(`[UPLOAD] Proxying request: ${req.method} ${req.url}`);
        },
        onProxyRes: (proxyRes, req, res) => {
          console.log(`[UPLOAD] Response received: ${proxyRes.statusCode} ${req.url}`);
        },
        onError: (err, req, res) => {
          console.error(`[UPLOAD] Proxy error: ${err.message}`);
        },
      })
    );

    app.use(
      '/images',
      createProxyMiddleware({
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        onProxyReq: (proxyReq, req, res) => {
          console.log(`[IMAGES] Proxying request: ${req.method} ${req.url}`);
        },
        onProxyRes: (proxyRes, req, res) => {
          console.log(`[IMAGES] Response received: ${proxyRes.statusCode} ${req.url}`);
        },
        onError: (err, req, res) => {
          console.error(`[IMAGES] Proxy error: ${err.message}`);
        },
      })
    );
  }
}

// Ensure only one instance of ProxyManager
const proxyManager = new ProxyManager();
Object.freeze(proxyManager);

module.exports = proxyManager;
