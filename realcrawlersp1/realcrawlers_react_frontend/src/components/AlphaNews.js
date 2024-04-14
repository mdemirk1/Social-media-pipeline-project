import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { selectAlphaNews, fetchAlphaNews } from '../backend/store/alphaNewsSlice';

const AlphaNews = () => {
  const dispatch = useDispatch();
  const alphaNews = useSelector(selectAlphaNews);
  //console.log(alphaNews);

  useEffect(() => {
    dispatch(fetchAlphaNews());
  }, [dispatch]);

  return (
    <div>
      <h1>Alpha News</h1>
      <ul className='news-feed'>
        {alphaNews?.alphaNews.map((news) => (
          <li key={news.title}
            className='news-item'>
            {news.title}- (Overall Sentiment: {news.overall_sentiment_score}, {news.overall_sentiment_label})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AlphaNews;