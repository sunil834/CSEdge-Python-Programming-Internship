# Web Scraping Tool with BeautifulSoup
'''Develop a web scraping application using Python's BeautifulSoup library. 
Extract data from a website and present it in a structured format (e.g., CSV, JSON). 
'''

# Required Modules
import requests
from bs4 import BeautifulSoup
import csv
import json

# Fetching URL
url = 'https://www.imdb.com/chart/top/'

# Using headers to prevent boting
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Converting Json to HTML
def js_to_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    scripts = soup.find_all('script')

    for script in scripts:
        if script.get('type') == 'application/ld+json':
            return script.string
    return None

# Extracting the top 250 iMDB movie details from the url
def extract_movie_data(json_data):
    movies = []

    for item in json_data.get('itemListElement', []):
        movie = item.get('item', {})
        name = movie.get('name')
        description = movie.get('description')
        rating_value = movie.get('aggregateRating', {}).get('ratingValue')
        content_rating = movie.get('contentRating')
        genre = movie.get('genre')
        movies.append({
            'name': name,
            'description': description,
            'ratingValue': rating_value,
            'contentRating': content_rating,
            'genre': genre
        })
    return movies

# Fetching url
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  
    json_string = js_to_html(response.content)
    
    #Checking the presense of json in the HTML content
    if not json_string:
        print("JSON data not found in the HTML content.")
    
    else:
        json_data = json.loads(json_string)
        movies = extract_movie_data(json_data)
        print(f"Extracted {len(movies)} movies.")
        csv_file_name = 'imdb_top_250.csv'
        
        # Saving fetchd data into .csv file
        with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'description', 'ratingValue', 'contentRating', 'genre']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(movies)
        print(f"Data saved to '{csv_file_name}'.")
        json_file_name = 'imdb_top_250.json'
        
        # Saving fetchd data into .json file
        with open(json_file_name, 'w', encoding='utf-8') as jsonfile:
            json.dump(movies, jsonfile, ensure_ascii=False, indent=4)
        print(f"Data saved to '{json_file_name}'.")

# Exception catching in the request
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")