import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://insights.blackcoffer.com/rising-it-cities-and-its-impact-on-the-economy-environment-infrastructure-and-city-life-by-the-year-2040-2/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article titles
titles = soup.find_all('h1', class_='entry-title')

# Find all the article content
contents = soup.find_all('div', class_='entry-content')

# Extract and print the title and content of each article
for title, content in zip(titles, contents):
    article_title = title.text.strip()  # Extract the text and remove leading/trailing whitespace
    article_content = content.text.strip()  # Extract the text and remove leading/trailing whitespace
    print("Title:", article_title)
    print("Content:", article_content)
    print()
