import React, { useState } from 'react';
import axios from 'axios';

/**
 * Component for uploading an image to the server.
 * @param {Object} props - The component props.
 * @param {Function} props.onUploadSuccess - Callback to notify parent on successful upload.
 */
function ImageUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);

  /**
   * Handles file input change and updates the file state.
   * @param {Event} e - The change event triggered by file input.
   */
  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  /**
   * Sends the selected file to the server via POST request.
   * On success, alerts the user and triggers the `onUploadSuccess` callback.
   */
  const handleUpload = async () => {
    if (!file) {
      alert('Please select a file before uploading.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      // API POST request to upload the image
      const response = await axios.post('/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data', // Ensures file is sent properly
        },
      });
      alert(response.data.message); // Notify user of success
      if (onUploadSuccess) {
        onUploadSuccess(); // Refresh image list in parent
      }
    } catch (error) {
      console.error('Error uploading file:', error);
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
