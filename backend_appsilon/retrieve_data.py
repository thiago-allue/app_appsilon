import json
from datetime import datetime

import requests

# Constants
API_URL = 'https://query.wikidata.org/sparql'
HEADERS = {'Accept': 'application/sparql-results+json'}
SPARQL_QUERY = '''
SELECT DISTINCT ?imdbId ?movieLabel ?releaseDate WHERE {
  ?movie wdt:P31 wd:Q11424;  # Movie instance
        wdt:P577 ?releaseDate;  # Release date property
        wdt:P345 ?imdbId;  # IMDb ID property
        rdfs:label ?movieLabel.  # Movie label property
  FILTER (YEAR(?releaseDate) >= 2013)
  FILTER (LANG(?movieLabel) = "en")  # Filter by English label
}
'''


def remove_imdbId_duplicates(movies):
    # Create a set to keep track of unique imdbIds
    imdbId_set = set()
    unique_movies = []

    for movie in movies:
        imdbId = movie['imdbId']
        if imdbId not in imdbId_set:
            imdbId_set.add(imdbId)
            unique_movies.append(movie)

    return unique_movies


def convert_date_format(date_string):
    # Convert date string to datetime object
    date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')

    # Convert datetime object to desired format
    formatted_date = date_object.strftime('%Y-%m-%d')
    return formatted_date


# Function to retrieve movie data
def retrieve_movie_data():
    # Send the SPARQL query request
    response = requests.get(API_URL, params={'query': SPARQL_QUERY}, headers=HEADERS)

    # Parse the JSON response and extract relevant movie information
    if response.status_code == 200:
        data = response.json()
        movie_list = []

        for item in data['results']['bindings']:
            movie = {
                'imdbId': item['imdbId']['value'],
                'title': item['movieLabel']['value'],
                'release_date': item['releaseDate']['value']
            }
            movie_list.append(movie)

        return movie_list

    else:
        print('Error: Failed to retrieve movie data from the API.')
        return []


def run():
    # Retrieve movie data
    movies = retrieve_movie_data()

    # Convert date format
    for movie in movies:
        movie['release_date'] = convert_date_format(movie['release_date'])

    # Remove imdbId duplicates
    movies = remove_imdbId_duplicates(movies)

    # Export movies to data.json
    with open('data.json', 'w') as file:
        json.dump(movies, file)

    print('Data exported to data.json.')


if __name__ == '__main__':
    """
    # Print the number of movies retrieved
    print(f'Number of movies retrieved: {len(movies)}')

    # Print the movie data
    for movie in movies[0:5]:
        print(f"Title: {movie['title']}")
        print(f"Release Date: {movie['release_date']}")
        print(f"IMDb ID: {movie['imdbId']}")
    """
    pass
