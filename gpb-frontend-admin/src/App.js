import React, { useState, useEffect } from 'react';
import refreshManager from './utils/RefreshManager';
import ImageUpload from './components/ImageUpload';
import ImageList from './components/ImageList';



function App() {
  const [refreshCount, setRefreshCount] = useState(0);

  useEffect(() => {
    const refreshHandler = () => {
      setRefreshCount((prev) => prev + 1);
    };

    refreshManager.register(refreshHandler);
    return () => {
      refreshManager.unregister(refreshHandler);
    };
  }, []);

  const handleManualRefresh = () => {
    refreshManager.triggerRefresh();
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
        <ImageUpload />
        <button
          onClick={handleManualRefresh}
          className="mb-4 px-4 py-2 bg-green-500 text-white font-semibold rounded-lg shadow-md hover:bg-green-600"
        >
          Refresh Images
        </button>
        <ImageList refreshCount={refreshCount} />
      </div>
    </div>
  );
}

export default App;

