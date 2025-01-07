#!/bin/bash
cat > "package.json" <<EOF
{
    "name": "fastapi-react-client",
    "version": "0.1.0",
    "private": true,
    "dependencies": {
        "axios": "^1.7.9",
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "react-scripts": "5.0.1"
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
    }
}
EOF


mkdir -p "public" && \
cat > "public\index.html" <<EOF
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>FastAPI React Client</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
EOF


mkdir -p "src" && \
cat > "src\App.js" <<EOF
import React from "react";
import FileUpload from "./components/FileUpload";
import ImageList from "./components/ImageList";

const App = () => {
  return (
    <div style={{ padding: "20px" }}>
      <h1>FastAPI React Client</h1>
      <FileUpload />
      <hr />
      <ImageList />
    </div>
  );
};

export default App;
EOF


mkdir -p "src" && \
cat > "src\index.css" <<EOF
/* src/index.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f4f4f9;
  }
  
  h1, h2 {
    color: #333;
  }
  
EOF


mkdir -p "src" && \
cat > "src\index.js" <<EOF
import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import "./index.css";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
EOF


mkdir -p "src\components" && \
cat > "src\components\FileUpload.js" <<EOF
import React, { useState } from "react";
import axios from "axios";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);  // State for loading

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage("Please select a file.");
      return;
    }

    setLoading(true);  // Start loading

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload/", 
        formData, 
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Failed to upload file.");
      console.error("Upload Error:", error);
    } finally {
      setLoading(false);  // End loading
    }
  };

  return (
    <div>
      <h2>Upload an Image</h2>
      <form onSubmit={handleUpload}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit" disabled={loading}>
          {loading ? "Uploading..." : "Upload"}
        </button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default FileUpload;
EOF


mkdir -p "src\components" && \
cat > "src\components\ImageList.js" <<EOF
import React, { useEffect, useState } from "react";
import axios from "axios";

const ImageList = () => {
  const [images, setImages] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);  // State for loading

  useEffect(() => {
    const fetchImages = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/images/");
        setImages(response.data.images);
      } catch (error) {
        setError("Failed to fetch images.");
        console.error("Fetch Error:", error);
      } finally {
        setLoading(false);  // End loading
      }
    };

    fetchImages();
  }, []);

  return (
    <div>
      <h2>Uploaded Images</h2>
      {loading && <p>Loading images...</p>}  {/* Loading message */}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {!loading && !error && images.length === 0 && (
        <p>No images uploaded yet.</p>
      )}
      <ul>
        {images.map((image) => (
          <li key={image.filename}>
            <strong>{image.filename}</strong> - {image.upload_time}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ImageList;
EOF


