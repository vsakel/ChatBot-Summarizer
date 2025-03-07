import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import NavigationBar from './NavigationBar.jsx';  
import UploadPage from './UploadPage.jsx';
import HomePage from './HomePage.jsx';

// The core component of the application that 
// acts as a container for the two main pages, managing the routing between them
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
