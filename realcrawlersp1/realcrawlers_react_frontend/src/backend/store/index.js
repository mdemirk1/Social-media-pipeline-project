import {configureStore, combineReducers} from '@reduxjs/toolkit';
import subRedditSlice from './subRedditSlice';
import alphaNewsSlice from './alphaNewsSlice';
import ExchangeSlice from './ExchangeSlice';

export default configureStore({
  reducer: combineReducers({
    subreddits: subRedditSlice,
    alphaNews: alphaNewsSlice,
    rates: ExchangeSlice, 
  })
});