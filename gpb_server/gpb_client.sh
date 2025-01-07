#!/bin/bash
cat > "package.json" <<EOF
{
  "name": "app",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@coreui/react": "^5.4.1",
    "axios": "^1.7.9",
    "cra-template": "1.2.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^4.2.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "tailwindcss": "^3.4.17"
  }
}
EOF


cat > "tailwind.config.js" <<EOF
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
EOF


mkdir -p "public" && \
cat > "public\index.html" <<EOF
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  </body>
</html>
EOF


mkdir -p "public" && \
cat > "public\manifest.json" <<EOF
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
EOF


mkdir -p "public" && \
cat > "public\robots.txt" <<EOF
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:
EOF


mkdir -p "src" && \
cat > "src\App.js" <<EOF

import React, { useState, useRef } from "react";

import axios from "axios";

const App = () =>{
  const [images, setImages] = useState([null, null, null, null]);
  const [selectedFrame, setSelectedFrame] = useState(null);
  const [isCameraActive, setIsCameraActive] = useState(false);
  const [filteredImages, setFilteredImages] = useState([null, null, null, null]);

  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  const handleFrameClick = (frame) => {
    setSelectedFrame(frame);
  };

  const handleImageUpload = (event, frame) => {
    const file = event.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        const updatedImages = [...images];
        updatedImages[frame - 1] = reader.result;
        setImages(updatedImages);
        const updatedFilteredImages = [...filteredImages];
        updatedFilteredImages[frame - 1] = null; // Reset any existing filter
        setFilteredImages(updatedFilteredImages);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleCapturePhoto = () => {
    if (canvasRef.current && videoRef.current) {
      const context = canvasRef.current.getContext("2d");
      if (context) {
        context.drawImage(videoRef.current, 0, 0, canvasRef.current.width, canvasRef.current.height);
        const imageData = canvasRef.current.toDataURL("image/png");

        const updatedImages = [...images];
        updatedImages[selectedFrame - 1] = imageData;
        setImages(updatedImages);

        const updatedFilteredImages = [...filteredImages];
        updatedFilteredImages[selectedFrame - 1] = null; // Reset any existing filter
        setFilteredImages(updatedFilteredImages);

        stopCamera();
      }
    }
  };

  const applyFilter = () => {
    if (selectedFrame === null || !images[selectedFrame - 1]) return;
    const updatedFilteredImages = [...filteredImages];
    updatedFilteredImages[selectedFrame - 1] = images[selectedFrame - 1]; // Apply filter (grayscale)
    setFilteredImages(updatedFilteredImages);
  };

  const startCamera = () => {
    setIsCameraActive(true);
    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
          videoRef.current.play();
        }
      })
      .catch((err) => {
        console.error("Error accessing camera:", err);
        setIsCameraActive(false);
      });
  };

  const stopCamera = () => {
    if (videoRef.current && videoRef.current.srcObject) {
      const stream = videoRef.current.srcObject;
      stream.getTracks().forEach((track) => track.stop());
      videoRef.current.srcObject = null;
    }
    setIsCameraActive(false);
  };

  const handleBackToFrames = () => {
    setSelectedFrame(null);
    stopCamera();
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-blue-900 to-pink-200 font-poppins">
      <header className="text-center mb-8">
        <h1 className="text-4xl font-bold text-white">4 You</h1>

        <p className="text-lg text-white opacity-80">Your memories, captured in four frames.</p>
      </header>
   
      {selectedFrame === null ? (
        <div className="grid grid-cols-2 gap-4 w-4/5 max-w-md mb-8">
          {[1, 2, 3, 4].map((frame) => (
            <div
              key={frame}
              className="relative aspect-square rounded-lg border-2 border-dashed border-white bg-white/30 flex items-center justify-center cursor-pointer overflow-hidden"
              onClick={() => handleFrameClick(frame)}
            >
              {filteredImages[frame - 1] ? (
                <img
                  src={filteredImages[frame - 1]}
                  alt={`Filtered Frame ${frame}`}
                  className="w-full h-full object-cover grayscale"
                />
              ) : images[frame - 1] ? (
                <img
                  src={images[frame - 1]}
                  alt={`Frame ${frame}`}
                  className="w-full h-full object-cover"
                />
              ) : (
                <p className="text-white text-sm opacity-80">Frame {frame}</p>
              )}
            </div>
          ))}
        </div>
      ) : (
        <div className="flex flex-col items-center gap-5">
          {isCameraActive ? (
            <div>
              <video ref={videoRef} className="w-72 h-72 rounded-lg object-cover" />
              <canvas ref={canvasRef} className="hidden" />
              <button
                className="px-5 py-2 mt-3 text-white bg-purple-500 rounded-full hover:bg-purple-600"
                onClick={handleCapturePhoto}
              >
                Capture Photo
              </button>
            </div>
          ) : (
            <>
              <div className="w-72 h-72 rounded-lg border-2 border-dashed border-white bg-white/30 flex items-center justify-center overflow-hidden">
                {filteredImages[selectedFrame - 1] ? (
                  <img
                    src={filteredImages[selectedFrame - 1]}
                    alt={`Filtered Frame ${selectedFrame}`}
                    className="w-full h-full object-contain grayscale"
                  />
                ) : images[selectedFrame - 1] ? (
                  <img
                    src={images[selectedFrame - 1]}
                    alt={`Frame ${selectedFrame}`}
                    className="w-full h-full object-contain"
                  />
                ) : (
                  <p className="text-white text-sm opacity-80">Frame {selectedFrame}</p>
                )}
              </div>
              <input
                type="file"
                accept="image/*"
                className="mt-2"
                onChange={(event) => handleImageUpload(event, selectedFrame)}
              />
              <button
                className="px-5 py-2 mt-3 text-white bg-purple-500 rounded-full hover:bg-purple-600"
                onClick={startCamera}
              >
                Open Camera
              </button>
              {images[selectedFrame - 1] && (
                <button
                  className="px-5 py-2 mt-3 text-white bg-green-500 rounded-full hover:bg-green-600"
                  onClick={applyFilter}
                >
                  Apply Filter
                </button>
              )}
            </>
          )}
          <button
            className="px-5 py-2 mt-3 text-white bg-red-500 rounded-full hover:bg-red-600"
            onClick={handleBackToFrames}
          >
            Back to Frames
          </button>
        </div>
      )}
    </div>
  );
};

export default App;
EOF


mkdir -p "src" && \
cat > "src\index.css" <<EOF
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
EOF


mkdir -p "src" && \
cat > "src\index.js" <<EOF
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
EOF


mkdir -p "src" && \
cat > "src\reportWebVitals.js" <<EOF
const reportWebVitals = onPerfEntry => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;
EOF


