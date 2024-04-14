
export const getsubRedditPosts = async (searchTerm) => {
    const response = await fetch(`/api/subreddit_posts/${searchTerm}`);
    const json = await response.json();
    //console.log(json.data.children);
    return json.data.children.map(child => child.data);
  };