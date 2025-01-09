import React, { useState } from 'react';
import axios from 'axios';
import refreshManager from '../utils/RefreshManager';

function ImageUpload() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      alert(response.data.message);
      refreshManager.triggerRefresh(); // Trigger refresh via singleton
    } catch (error) {
      alert('Error uploading file');
    }
  };

  return (
    <div className="mb-6">
      <h2 className="text-xl font-semibold text-gray-700 mb-4">
        Upload Image
      </h2>
      <div className="flex items-center gap-4">
        <input
          type="file"
          onChange={handleFileChange}
          className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none focus:ring focus:ring-blue-300"
        />
        <button
          onClick={handleUpload}
          className="px-4 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300"
        >
          Upload
        </button>
      </div>
    </div>
  );
}

export default ImageUpload;
