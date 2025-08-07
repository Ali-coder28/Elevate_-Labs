import requests
from bs4 import BeautifulSoup

# URL of the news website
url = 'https://www.bbc.com/news'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all headlines (this may vary based on the website's structure)
    headlines = soup.find_all('h3')  # Example: BBC uses <h3> for headlines

    # Print the headlines
    for headline in headlines:
        print(headline.get_text())
else:
    print(f"Failed to retrieve news. Status code: {response.status_code}")
