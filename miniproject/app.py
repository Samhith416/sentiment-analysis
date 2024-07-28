from flask import Flask, render_template, request
from collections import defaultdict

app = Flask(__name__)

# Sample data
articles = [
    {"category": "Sports", "sentiment": "positive"},
    {"category": "Politics", "sentiment": "negative"},
    # Add more articles here
]

categories = ["Sports", "Politics", "Technology", "Health",
              "Entertainment", "Business", "Science", "World", "Lifestyle", "Travel"]

# Calculate sentiment difference
sentiment_counts = defaultdict(lambda: {"positive": 0, "negative": 0})

for article in articles:
    category = article["category"]
    sentiment = article["sentiment"]
    sentiment_counts[category][sentiment] += 1

sentiment_diff = {}
for category in categories:
    positive_count = sentiment_counts[category]["positive"]
    negative_count = sentiment_counts[category]["negative"]
    sentiment_diff[category] = positive_count - negative_count


def recommend_articles(mood):
    recommended_categories = []
    if mood == "happy":
        recommended_categories = ['business','entertainment', 'tech', 'arts', 'science']
                                  
    elif mood == "sad":
        recommended_categories = ['crime & security', 'politics', 'weird-news', 'health & education', 'sports']
                                  
    return recommended_categories


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form['mood']
    recommendations = recommend_articles(mood)
    return render_template('index.html', recommendations=recommendations, mood=mood)


if __name__ == '__main__':
    app.run(debug=True)
