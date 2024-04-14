import React from 'react';
import Subreddits from './components/Subreddits';
import AlphaNews from './components/AlphaNews';
// import CryptoRates from './components/CryptoRates';

function App() {
  return (
    <div className="App">
      <Subreddits/>
      <AlphaNews /> 
      {/* <CryptoRates /> */}
    </div>
  );
}

export default App;
