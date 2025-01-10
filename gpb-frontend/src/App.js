
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
