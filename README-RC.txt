To run the program and get Reddit titles from cryptocurrency subreddit,
start faktory by typing faktory to the terminal.
you first need to run simple_faktory.py to start the faktory workers.
Then, you need to run reddit_crawler.py from another terminal to give jobs to this worker in every 3 minutes.

This is an example for name of reddit post -> t3_175jl1l
This is what we called id in our code.
However, reddit calls this name. And call 175jl1l id.
In get_comments function, API needs id, 
so we put the end part of name which is 175jl1l in this example.