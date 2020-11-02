import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm
import pandas as pd
import numpy as np

movie_date = []
movie_name = []
movie_point = []

date = pd.date_range('2020-10-1', periods=30, freq='D')

#tqdm_notebook deprecated 되어 새로운 것 사용
for today in tqdm(date):
    html ="http://movie.naver.com/" +"movie/sdb/rank/rmovie.nhn?sel=cur&date={date}"

    response = urlopen(html.format(date=urllib.parse.quote(today.strftime('%Y%m%d'))))
    #response = urlopen(html.format(date=today))

    soup = BeautifulSoup(response,  "html.parser")

    end = len(soup.find_all('td','point'))

    movie_date.extend(today for n in range(0,end))
    movie_name.extend([soup.find_all('div','tit5')[n].a.string for n in range(0,end)])
    movie_point.extend([soup.find_all('td', 'point')[n].string for n in range(0, end)])

movie = pd.DataFrame({'date':movie_date, 'name':movie_name,'point':movie_point})
#소수점 계산 위해 추가함
movie['point'] = movie['point'].astype(float)
movie.head()

movie_unique = pd.pivot_table(movie, index=['name'], aggfunc=np.average)
movie_best = movie_unique.sort_values(by='point', ascending=False)

movie_best.head()
print(movie_best.head())

