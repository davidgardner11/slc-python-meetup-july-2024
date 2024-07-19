import random
import json
import requests
from bs4 import BeautifulSoup

# crawl IMDB Top 250 and randomly select a movie

# Define a User-Agent string that mimics a common browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# set URL
URL = 'http://www.imdb.com/chart/top'

def main():
    response = requests.get(URL, headers=headers)
    # print("URL: " + URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the script element with type="application/ld+json"
    script_element = soup.find('script', type='application/ld+json')
    if script_element:
        # Extract the JSON content
        json_content = script_element.string
        
        # Parse the JSON content
        json_data = json.loads(json_content)
        
        # Now json_data contains the parsed JSON object
        print("JSON object extracted successfully.")
        print("Type of json_data:", type(json_data))
        # print("Contents of json_data:")
        # print(json.dumps(json_data, indent=2))
    else:
        print("No <script type=\"application/ld+json\"> element found in the HTML.")
        exit
    
    movie_names = []
    # movie_ratings = []
    # movie_releaseDate = []
    for item in json_data['itemListElement']:
        if item['item']['@type'] == 'Movie':
            movie_names.append(item['item']['name'])
           # movie_ratings.append(item['item']['aggregateRating'])
           # movie_release_dates.append(item['item']['releaseDate'])

    n_movies = len(movie_names)

    while(True):
        idx = random.randrange(0, n_movies)
        
        # print(f'{movie_names[idx]} {movie_release_dates[idx]}, Rating: {movie_ratings[idx]}' )
        print(f'{movie_names[idx]}')

        # comment the next line out to test user input with docker run -t -i
        # break
    
        user_input = input('Do you want another movie (y/[n])? ')
        if user_input != 'y':
            break
    

if __name__ == '__main__':
    main()
