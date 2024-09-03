import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
from datetime import datetime, date
from test import extract_team_names_from_string, extract_team_names

url_2008 = 'https://www.cricbuzz.com/cricket-series/2058/indian-premier-league-2008/matches'
url_2009 = 'https://www.cricbuzz.com/cricket-series/2059/indian-premier-league-2009/matches'
url_2010 = 'https://www.cricbuzz.com/cricket-series/2060/indian-premier-league-2010/matches'
url_2011 = 'https://www.cricbuzz.com/cricket-series/2037/indian-premier-league-2011/matches'
url_2012 = 'https://www.cricbuzz.com/cricket-series/2115/indian-premier-league-2012/matches'
url_2013 = 'https://www.cricbuzz.com/cricket-series/2170/indian-premier-league-2013/matches'
url_2014 = 'https://www.cricbuzz.com/cricket-series/2261/indian-premier-league-2014/matches'
url_2015 = 'https://www.cricbuzz.com/cricket-series/2330/indian-premier-league-2015/matches'
url_2016 = 'https://www.cricbuzz.com/cricket-series/2430/indian-premier-league-2016/matches'
url_2017 = 'https://www.cricbuzz.com/cricket-series/2568/indian-premier-league-2017/matches'
url_2018 = 'https://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/matches'
url_2019 = 'https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/matches'
url_2020 = 'https://www.cricbuzz.com/cricket-series/3130/indian-premier-league-2020/matches'
url_2021 = 'https://www.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/matches'
url_2022 = 'https://www.cricbuzz.com/cricket-series/4061/indian-premier-league-2022/matches'
url_2023 = 'https://www.cricbuzz.com/cricket-series/5945/indian-premier-league-2023/matches'
url_2024 = 'https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches'
match_year = [url_2008, url_2009, url_2010, url_2011, url_2012, url_2013, url_2014, url_2015,
              url_2016, url_2017, url_2018, url_2019, url_2020, url_2021, url_2022, url_2023, url_2024]
matches = []

def s_myear(i):
    i = i-2008
    if i < len(match_year):
        return match_year[i]
    
def get_winners(url):
    matches = []
    webpage = requests.get(url)
    web = webpage.content
    soup = BeautifulSoup(web, "html.parser")
    # print(soup)
    q = soup.find_all(
        'a', class_='cb-text-complete')
    # print(q)
    for i in q:
        # print(i.text)
        matches.append(i.text)
    return matches


# yearrr = int(input("enter year:"))
# matches = get_winners(match_year[yearrr-2008])
# print(matches)
# print(len(matches))
