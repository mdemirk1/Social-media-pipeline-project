import {createSlice} from '@reduxjs/toolkit';
import {getAlphaNews} from '../api/alphanews';

const initialState = {
  alphaNews: [],
  error: false,
  isloading: false,
};

const alphaNewsSlice = createSlice({
  name: 'alphaNews',
  initialState,
  reducers: {
    startGetNews(state) {
      state.isloading = true;
      state.error = false;
    },
    getNewsSuccess(state, action) {
      state.isLoading = false;
      state.alphaNews = [...action.payload];
    },
    getNewsFailed(state) {
      state.isLoading = false;
      state.error = true;
    },
  },
});

export const {
  getNewsFailed,
  getNewsSuccess,
  startGetNews,
} = alphaNewsSlice.actions;

export default alphaNewsSlice.reducer;

export const fetchAlphaNews = () => async dispatch => {
  try {
    dispatch(startGetNews());
    const news_feed = await getAlphaNews();
    dispatch(getNewsSuccess(news_feed));
  } catch (e) {
    dispatch(getNewsFailed());
  }
};

export const selectAlphaNews = state => state.alphaNews;