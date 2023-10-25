import requests
from bs4 import BeautifulSoup
import json


def scrape_comments(url, num_pages=1):
    comments_by_category = {}

    for page in range(1, num_pages + 1):
        page_url = f'{url}page/{page}' if page > 1 else url  # Handle pagination

        response = requests.get(page_url)


        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            comments = soup.find_all('div', class_='quote')

            for comment in comments:
                author = comment.find('small', class_ ='author').text.strip()
                text = comment.find('span', class_ ='text').text.strip()

                # Extract categories (tags)
                tags =[tag.text for tag in comment.find_all('a', class_ ='tag')]

                # Add comments to the respective category
                for category in tags:
                    if category in comments_by_category:
                        comments_by_category[category].append({'author': author, 'text': text})
                else:
                    comments_by_category[category] = [{'author': author, 'text': text}]

    else:
       print(f'Failed to retrieve the web page (Page {page}). Status code:', response.status_code)

        # Count the number of comments per category
        category_counts = {category: len(comments) for category, comments in comments_by_category.items()}

        # Output the results
        print("Comments by Category:")
        print(json.dumps(comments_by_category, indent=2))

        print("\nNumber of Comments per Category:")
        print(json.dumps(category_counts, indent=2))

# Example usage
url = 'https://quotes.toscrape.com/page/'
num_pages = 3  # Change this value to the number of pages you want to scrape
scrape_comments(url, num_pages)


