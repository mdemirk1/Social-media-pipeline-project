import {createSlice} from '@reduxjs/toolkit';
import {getsubRedditPosts} from '../api/reddit';

const initialState = {
  subreddits: [],
  error: false,
  isloading: false,
};

const subRedditSlice = createSlice({
  name: 'subReddits',
  initialState,
  reducers: {
    startGetsubReddits(state) {
      state.isloading = true;
      state.error = false;
    },
    getSubredditsSuccess(state, action) {
      state.isLoading = false;
      state.subreddits= [...action.payload];
    },
    getSubredditsFailed(state) {
      state.isLoading = false;
      state.error = true;
    },
  },
});

export const {
  getSubredditsFailed,
  getSubredditsSuccess,
  startGetsubReddits,
} = subRedditSlice.actions;

export default subRedditSlice.reducer;

export const fetchsubReddits = () => async dispatch => {
  try {
    let searchTerm = "CryptoCurrency";  // default search term
    dispatch(startGetsubReddits());
    const subReddits = await getsubRedditPosts(searchTerm);
    //console.log(subReddits)
    dispatch(getSubredditsSuccess(subReddits));
  } catch (e) {
    dispatch(getSubredditsFailed());
  }
};

export const selectSubReddits = state => state.subreddits;