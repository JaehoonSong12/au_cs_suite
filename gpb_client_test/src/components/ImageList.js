import React, { useEffect, useState } from 'react';
import axios from 'axios';

/**
 * Component for displaying a list of uploaded images.
 * @param {Object} props - The component props.
 * @param {boolean} props.refresh - A flag to trigger re-fetching of the image list.
 */
function ImageList({ refresh }) {
  const [images, setImages] = useState([]);

  /**
   * Fetches the list of images from the server.
   * Executes whenever the `refresh` flag changes.
   */
  useEffect(() => {
    const fetchImages = async () => {
      try {
        // API GET request to retrieve image list
        const response = await axios.get('/images/');
        setImages(response.data.images); // Update state with fetched images
      } catch (error) {
        console.error('Error fetching images:', error);
        alert('Error fetching images');
      }
    };

    fetchImages();
  }, [refresh]); // Dependency array ensures fetchImages runs on refresh

  /**
   * Deletes an image from the server by filename.
   * @param {string} filename - The name of the file to delete.
   */
  const handleDelete = async (filename) => {
    try {
      // API DELETE request to remove the image
      await axios.delete(`/images/${filename}`);
      // Remove deleted image from local state
      setImages(images.filter((image) => image.filename !== filename));
      alert('File deleted successfully');
    } catch (error) {
      console.error('Error deleting file:', error);
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
              {/* Button to download the image */}
              <a
                href={`/images/${image.filename}`}
                target="_blank"
                rel="noopener noreferrer"
                className="px-3 py-1 bg-green-500 text-white text-sm font-semibold rounded-lg hover:bg-green-600"
              >
                Download
              </a>
              {/* Button to delete the image */}
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
