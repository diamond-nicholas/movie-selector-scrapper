from random import random
import random
import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top'


def main():
 response = requests.get(url)
 html = response.text

 soup = BeautifulSoup(html, 'html.parser')
 movietag = soup.select('td.titleColumn')
 inner_movietags = soup.select('td.titleColumn a')
 rating_tags = soup.select('td.posterColumn span[name=ir]')

 def get_year(movie_tag):
  moviesplit = movie_tag.text.split()
  year = moviesplit[-1]
  return year
 
 years = [get_year(tag) for tag in movietag]
 actors_list = [tag['title'] for tag in inner_movietags]
 titles = [tag.text for tag in inner_movietags]
 ratings = [float(tag['data-value']) for tag in rating_tags]


 n_movies = len(titles)
 print(n_movies)

 while(True):
  index = random.randrange(0, n_movies)
  print(f'{titles[index]} {years[index]}, rating: {ratings[index]:.1f}, starring: {actors_list[index]}')

  user_input = input('do you want another movie (y/[n]) ?')

  if user_input != 'y':
   break




if __name__ == '__main__':
 main()