import csv
import re
import requests
from bs4 import BeautifulSoup

# Function to check if a text contains Arabic characters
def is_arabic(text):
    arabic_pattern = re.compile('[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
    return bool(arabic_pattern.search(text))

url = 'https://www.amazon.eg/-/en/NOKIA-105-Dual-SIM-Black/dp/B07WXW8V4X/ref=sr_1_10?crid=3M72SHMQQVEDX&keywords=mobile&qid=1702480243&sprefix=%2Caps%2C131&sr=8-10&th=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    review_divs = soup.find_all('div', {'data-hook': 'review'})
    Arabic_data_scrapped = {}

    for review_div in review_divs:
        # Catch Arabic Comments
        span_texts = [span.text.strip() for span in review_div.find_all('span', {'data-hook': 'review-body'})]
        arabic_reviews = [text for text in span_texts if is_arabic(text)]

        # Catch The Rating
        if bool(arabic_reviews):
            rating_span = review_div.find('span', {'class': 'a-icon-alt'})
            if rating_span:
                rating_text = rating_span.text.strip()
                # Catch only the number from rating
                rating = re.search(r'\d+\.\d+', rating_text)
                if rating:
                    rating_value = float(rating.group())
                    content_value = arabic_reviews[0]
                    # check threshold
                    label_value = 1 if rating_value > 3 else 0
                    # Add in Dictionary
                    Arabic_data_scrapped[label_value] = content_value
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Write to CSV file
with open('arabic_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['label', 'content']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Iterate over the dictionary and write each row
    for label, content in Arabic_data_scrapped.items():
        writer.writerow({'label': label, 'content': content})