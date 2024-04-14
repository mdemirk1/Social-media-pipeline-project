

export const getAlphaNews = async () => {
    const response = await fetch(`/api/get_alphanews_data`);
    const json = await response.json();
    
    return json.feed;
  };