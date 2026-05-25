import pandas as pd

# 1. Social Media Comments Data Simulation
data = {
    'username': ['user1', 'user2', 'user3', 'user4', 'user5'],
    'comment': [
        'This game is great!', 
        'I hate the latest update, bugs everywhere.', 
        'is there any tips to get to level 5?', 
        'boring gameplay and environment.',
        'this is the best game i ever played!'
    ]
}

df = pd.DataFrame(data)

# 2. Simple Function to Classified the Sentiments
def sentiment_classification(text):
    text = text.lower()
    if 'great' in text or 'good' in text or 'best' in text:
        return 'Positive'
    elif 'hate' in text or 'bug' in text or 'boring' in text:
        return 'Negative'
    else:
        return 'Neutral'

# 3. Applying the Classification
df['sentiment'] = df['comment'].apply(sentiment_classification)

# 4. Showing Result
print("Comment Analysis Data Result :")
print(df)
