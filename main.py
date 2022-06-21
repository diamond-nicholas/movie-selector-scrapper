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
 movietag0 = movietag[0]

 def get_year(movie_tag):
  moviesplit = movie_tag.text.split()
  year = moviesplit[-1]
  return year
 
 years = [get_year(tag) for tag in movietag]

 # print(moviesplit)
 



if __name__ == '__main__':
 main()