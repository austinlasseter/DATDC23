'''
Getting Data from APIs
What is an API?
- Application Programming Interface
- Structured way to expose specific functionality and data access to users
- Web APIs usually follow the "REST" standard
How to interact with a REST API:
- Make a "request" to a specific URL (an "endpoint"), and get the data back in a "response"
- Most relevant request method for us is GET (other methods: POST, PUT, DELETE)
- Response is often JSON format
- Web console is sometimes available (allows you to explore an API)
'''

# read IMDb data into a DataFrame: we want a year column!
import pandas as pd
import requests 
api_key = ''
# movies = pd.read_csv('imdb_1000.csv')
movies = pd.read_csv('https://raw.githubusercontent.com/josephofiowa/GA-DSI/master/intro-to-apis-python/assets/data/imdb_1000.csv')

# relative path?
movies = pd.read_csv('')

movies.head()

# use requests library to interact with a URL
r = requests.get('http://www.omdbapi.com/?t=the shawshank redemption&r=json&type=movie&apikey=' + api_key)

# check the status: 200 means success, 4xx means error
r.status_code

# view the raw response text
r.text

# decode the JSON response body into a dictionary
r.json()

# extracting the year from the dictionary
r.json()['Year']

# what happens if the movie name is not recognized?
r = requests.get('http://www.omdbapi.com/?t=john tate is good at data science&r=json&type=movie&apikey=' + api_key)
r.status_code
r.json()

# define a function to return the year
def get_movie_year(title):
    r = requests.get('http://www.omdbapi.com/?t=' + title + '&r=json&type=movie&apikey=' + api_key)
    info = r.json()
    if info['Response'] == 'True':
        return int(info['Year'])
    else:
        return None

# test the function
get_movie_year('The Shawshank Redemption')
get_movie_year('blahblahblah')

# create a smaller DataFrame for testing
top_movies = movies.head().copy()

# write a for loop to build a list of years
from time import sleep
years = []
for title in top_movies.title:
    years.append(get_movie_year(title))
    sleep(1)

# check that the DataFrame and the list of years are the same length
assert(len(top_movies) == len(years))

# save that list as a new column
top_movies['year'] = years

top_movies.head()

# enumerate in class example
years = []
for position, title in enumerate(top_movies.title):
    year = get_movie_year(title)
    years.append(year)
    sleep(1)
    print 'Completed ', year, position

# churck norris business
import requests
resp = requests.get('https://api.chucknorris.io/jokes/random')
resp.status_code
resp.json()['value']

from time import sleep

for x in range(1,11):
    resp = requests.get('https://api.chucknorris.io/jokes/random')
    print(resp.json()['value'])