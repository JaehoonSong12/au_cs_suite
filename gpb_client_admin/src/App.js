import React, { useState } from 'react';
import ImageUpload from './components/ImageUpload';
import ImageList from './components/ImageList';

function App() {
  const [refresh, setRefresh] = useState(false);

  const refreshImageList = () => {
    setRefresh(!refresh);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="max-w-4xl mx-auto bg-white rounded-lg shadow-md p-6">
        <h1 className="text-2xl font-bold text-center text-blue-600 mb-6">
          4 You (Admin)
        </h1>
        <p>
          This is an admin instance to test "Image File IO Management", "Networking", and "Security" modules!
        </p>
        <ImageUpload onUploadSuccess={refreshImageList} />
        <ImageList refresh={refresh} />
      </div>
    </div>
  );
}

export default App;
