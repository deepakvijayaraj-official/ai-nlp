### Customer Sentiment analysis of Reviews of products on a website using NLP

In this example, we'll use Python's requests and BeautifulSoup libraries to scrape customer reviews from a website and then perform sentiment analysis on those reviews using NLTK.

We define a scrape_reviews function to fetch customer reviews from the specified URL. You should modify the code within this function to match the structure of the website you want to scrape.

We call the scrape_reviews function to obtain the list of customer reviews.

We analyze the sentiment of each review using the NLTK's Sentiment Intensity Analyzer (SentimentIntensityAnalyzer) and classify them as "Positive," "Negative," or "Neutral."

Finally, we display the sentiment analysis results, including the review text and sentiment label.

Remember to replace the website_url with the actual URL of the website you want to scrape customer reviews from and adapt the code to the specific HTML structure of the target website for proper data extraction.

You need to have associated packages installed as a Pre-requisite.

```python
pip install -r requirements.txt

python3 customer_review_analysis.py
```
