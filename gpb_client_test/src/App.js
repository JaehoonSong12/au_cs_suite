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
