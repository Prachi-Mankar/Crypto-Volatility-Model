import praw
import pandas as pd

# Reddit API credentials
reddit = praw.Reddit(
    client_id='As1ADaUpj-jLGGfp4LHH6g',
    client_secret='wB4rIi0jmqAT_A3iHk_cxDfbB5Xs-Q',
    user_agent='crypto-sentiment-script'
)

# Choose the subreddit and keyword
subreddit = reddit.subreddit('Bitcoin')
query = 'bitcoin'

# Fetch top 100 posts from the past month
posts = []
for post in subreddit.search(query, limit=100, sort='new'):
    posts.append({
        'title': post.title,
        'text': post.selftext,
        'score': post.score,
        'date': post.created_utc
    })

# Save to CSV
df = pd.DataFrame(posts)
df.to_csv('reddit_bitcoin_posts.csv', index=False)
print("Saved 100 posts to reddit_bitcoin_posts.csv")
