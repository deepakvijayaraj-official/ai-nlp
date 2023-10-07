import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Function to scrape customer reviews from a website
def scrape_reviews(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            reviews = []
            
            # Modify the following code to extract reviews from the specific website
            # Example: Extracting reviews from <div class="review"> elements
            #review_elements = soup.find_all('div', class_='review')
           
            #print(f"reviews: {review_elements}")
            for review_element in review_elements:
                review_text = review_element.text.strip()
                reviews.append(review_text)
            
            return reviews
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred while scraping reviews: {str(e)}")
        return []

# Analyze sentiment of a list of reviews
def analyze_reviews_sentiment(reviews):
    sentiments = []
    for review in reviews:
        sentiment_scores = sia.polarity_scores(review)
        sentiment = "Positive" if sentiment_scores['compound'] >= 0.05 else "Negative" if sentiment_scores['compound'] <= -0.05 else "Neutral"
        sentiments.append(sentiment)
    return sentiments

# URL of the website to scrape customer reviews from
website_url = "https://example.com/reviews"  # Replace with the actual URL

# Scrape reviews from the website
customer_reviews = scrape_reviews(website_url)

if customer_reviews:
    # Perform sentiment analysis on the scraped reviews
    sentiments = analyze_reviews_sentiment(customer_reviews)

    # Display sentiment analysis results
    for i, review in enumerate(customer_reviews):
        print(f"Review {i + 1}:")
        print(f"Text: {review}")
        print(f"Sentiment: {sentiments[i]}")
        print("\n")
else:
    print("No customer reviews found on the website.")

