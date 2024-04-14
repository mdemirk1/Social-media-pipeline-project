import {createSlice} from '@reduxjs/toolkit';
import {getCryptoExchange} from '../api/exchange';

const initialState = {
  rates: [],
  error: false,
  isloading: false,
};

const ExchangeSlice = createSlice({
  name: 'rates',
  initialState,
  reducers: {
    startGetCryptoRates(state) {
      state.isloading = true;
      state.error = false;
    },
    getCryptoRatesSuccess(state, action) {
      state.isLoading = false;
      state.rates= [...action.payload];
    },
    getCyrptoRatesFailed(state) {
      state.isLoading = false;
      state.error = true;
    },
  },
});

export const {
  getCryptoRatesSuccess,
  getCyrptoRatesFailed,
  startGetCryptoRates,
} = ExchangeSlice.actions;

export default ExchangeSlice.reducer;

export const fetchCryptoRates = () => async dispatch => {
  try {
    let searchTerm = "BTC";  // default search term
    dispatch(startGetCryptoRates());
    const rates = await getCryptoExchange(searchTerm);
    dispatch(getCryptoRatesSuccess(rates));
  } catch (e) {
    dispatch(getCyrptoRatesFailed());
  }
};

export const selectCryptoRates = state => state.rates;