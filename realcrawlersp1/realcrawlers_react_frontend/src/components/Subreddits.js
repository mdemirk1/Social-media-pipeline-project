import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { selectSubReddits, fetchsubReddits } from '../backend/store/subRedditSlice';

const Subreddits = () => {
  const dispatch = useDispatch();
  const subreddits = useSelector(selectSubReddits);
  //console.log(subreddits);

  useEffect(() => {
    dispatch(fetchsubReddits());
  }, [dispatch]);

  return (
    <div>
      <h1>Subreddit Posts: Cryptocurrency</h1>
      <ul className='subreddits-list'>
        {subreddits?.subreddits.map((subreddit) => (
          <li key={subreddit.id}
            className='subreddit-item'>
            {subreddit.title}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Subreddits;