import React, { useEffect, useState } from 'react';
import axios from 'axios';
import refreshManager from '../utils/RefreshManager';

function ImageList() {
  const [images, setImages] = useState([]);

  useEffect(() => {
    const fetchImages = async () => {
      try {
        const response = await axios.get('/images/');
        setImages(response.data.images);
      } catch (error) {
        alert('Error fetching images');
      }
    };

    const refreshHandler = () => {
      fetchImages();
    };

    refreshManager.register(refreshHandler);
    fetchImages(); // Initial fetch

    return () => {
      refreshManager.unregister(refreshHandler);
    };
  }, []);

  const handleDelete = async (filename) => {
    try {
      await axios.delete(`/images/${filename}`);
      refreshManager.triggerRefresh(); // Trigger refresh via singleton
      alert('File deleted successfully');
    } catch (error) {
      alert('Error deleting file');
    }
  };

  return (
    <div>
      <h2 className="text-xl font-semibold text-gray-700 mb-4">Image List</h2>
      <ul className="divide-y divide-gray-200">
        {images.map((image) => (
          <li
            key={image.filename}
            className="flex items-center justify-between py-3"
          >
            <div>
              <p className="text-gray-800 font-medium">{image.filename}</p>
              <p className="text-gray-500 text-sm">
                {new Date(image.upload_time).toLocaleString()}
              </p>
            </div>
            <div className="flex items-center gap-4">
              <a
                href={`/images/${image.filename}`}
                target="_blank"
                rel="noopener noreferrer"
                className="px-3 py-1 bg-green-500 text-white text-sm font-semibold rounded-lg hover:bg-green-600"
              >
                Download
              </a>
              <button
                onClick={() => handleDelete(image.filename)}
                className="px-3 py-1 bg-red-500 text-white text-sm font-semibold rounded-lg hover:bg-red-600"
              >
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ImageList;
