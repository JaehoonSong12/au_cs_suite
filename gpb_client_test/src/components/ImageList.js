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
