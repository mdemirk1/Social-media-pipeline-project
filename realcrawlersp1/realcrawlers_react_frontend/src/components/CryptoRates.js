import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { selectCryptoRates, fetchCryptoRates } from '../backend/store/ExchangeSlice';

const CryptoRates = () => {
  const dispatch = useDispatch();
  const rates = useSelector(selectCryptoRates);

  useEffect(() => {
    dispatch(fetchCryptoRates());
  }, [dispatch]);
 
  return (
    <div>
      <h1>Cryptocurrency Rates</h1>
      <ul className='rates-list'>
        {rates?.rates.slice(0,10).map((date, i) => (
          <li key={i}
            className='rate-item'>
            {`${date.date} - high: ${date['2a. high (USD)']} - low: ${date['3a. low (USD)']}`}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CryptoRates;