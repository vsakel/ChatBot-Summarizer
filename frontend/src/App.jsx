import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import NavigationBar from './NavigationBar.jsx';  
import UploadPage from './UploadPage.jsx';
import HomePage from './HomePage.jsx';

// main component of our application
function App() {
  return (
  <BrowserRouter>
    <div className="App">
      <NavigationBar/>  
      <Routes>
        <Route path="/" element={<HomePage/>}/>
        <Route path="/upload" element={<UploadPage/>}/> 
      </Routes>
    </div>
  </BrowserRouter>
  );
}

export default App;
