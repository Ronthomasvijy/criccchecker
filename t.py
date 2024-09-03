# import requests
# from bs4 import BeautifulSoup
from datetime import datetime, date
import re
import os
import pandas as pd
# import os


# url_2008 = 'https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494/match-schedule-fixtures-and-results'
# url_2009 = 'https://www.espncricinfo.com/series/indian-premier-league-2009-374163/match-schedule-fixtures-and-results'
# url_2010 = 'https://www.espncricinfo.com/series/indian-premier-league-2009-10-418064/match-schedule-fixtures-and-results'
# url_2011 = 'https://www.espncricinfo.com/series/indian-premier-league-2011-466304/match-schedule-fixtures-and-results'
# url_2012 = 'https://www.espncricinfo.com/series/indian-premier-league-2012-520932/match-schedule-fixtures-and-results'
# url_2013 = 'https://www.espncricinfo.com/series/indian-premier-league-2013-586733/match-schedule-fixtures-and-results'
# url_2014 = 'https://www.espncricinfo.com/series/pepsi-indian-premier-league-2014-695871/match-schedule-fixtures-and-results'
# url_2015 = 'https://www.espncricinfo.com/series/pepsi-indian-premier-league-2015-791129/match-schedule-fixtures-and-results'
# url_2016 = 'https://www.espncricinfo.com/series/ipl-2016-968923/match-schedule-fixtures-and-results'
# url_2017 = 'https://www.espncricinfo.com/series/ipl-2017-1078425/match-schedule-fixtures-and-results'
# url_2018 = 'https://www.espncricinfo.com/series/ipl-2018-1131611/match-schedule-fixtures-and-results'
# url_2019 = 'https://www.espncricinfo.com/series/ipl-2019-1165643/match-schedule-fixtures-and-results'
# url_2020 = 'https://www.espncricinfo.com/series/ipl-2020-21-1210595/match-schedule-fixtures-and-results'
# url_2021 = 'https://www.espncricinfo.com/series/ipl-2021-1249214/match-schedule-fixtures-and-results'
# url_2022 = 'https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/match-schedule-fixtures-and-results'
# url_2023 = 'https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/match-schedule-fixtures-and-results'
# url_2024 = 'https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results'
# match_year = [url_2008, url_2009, url_2010, url_2011, url_2012, url_2013, url_2014, url_2015,
#               url_2016, url_2017, url_2018, url_2019, url_2020, url_2021, url_2022, url_2023, url_2024]
# matches = []
# matches.clear


# def get_dates(url):
#     matches = []
#     prev = ""
#     webpage = requests.get(url)
#     web = webpage.content
#     soup = BeautifulSoup(web, "html.parser")
#     q = soup.find_all(
#         'div', class_='ds-text-compact-xs ds-font-bold ds-w-24')
#     for i in q:
#         if len(i.text) == 0:
#             matches.append(prev)
#         else:
#             prev = i.text
#             matches.append(i.text)
#     return matches


# year = int(input("enter year: "))
# matches = get_dates(match_year[year-2008])
# print(len(matches))
# for i in matches:
#     print(i)
# filename = "data.csv"
# # opening the file with w+ mode truncates the file
# f = open(filename, "w+")
# f.close()
# columns = ['match_no', 'match_date', 'team_name1', 'score1', 'overs_batted1',
#            'team_name2', 'score2', 'overs_batted2', 'target', 'dls_affected']
# df = pd.DataFrame(columns=columns)
# # Save the DataFrame to a CSV file
# df.to_csv('data.csv', index=False)


# k = "8.8/9.8 ov"
# print(k)
# overs1 = k.split('ov')[0].split('/')[1]
# print(float(overs1)//1)
# print(int(9.0))


# def get_table():
#     df = pd.read_csv('data.csv')
#     row1 = df['team_name1'].unique()
#     dict_table = {}
#     dict_table = {key: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for key in row1}
#     print(dict_table)
#     for i in range(len(df)-3):
#         row = df.iloc[i]
#         if (row['dls_affected'] == False):
#             if row['victory'] == None:
#                 print(i, row['victory'])


# get_table()

# from difflib import get_close_matches
# import pandas as pd
# import re
# valid_teams = ["Deccan Chargers", "Delhi Daredevils", "Mumbai Indians", "Chennai Super Kings", "Kolkata Knight Riders", "Punjab Kings", "Lucknow Super Giants", "Gujarat Titans", "Sunrisers Hyderabad",
#                "Delhi Capitals", "Royal Challengers Bengaluru", "Royal Challengers Bengalore", "Rajasthan Royals", "Kings XI Punjab", "Kochi Tuskers Kerala", "Rising Pune Super Giants", "Gujarat Lions"]


# def extract_team_names_from_string(match_string, valid_teams):
#     team_names = []
#     match = get_close_matches(match_string.strip(),
#                               valid_teams, n=1, cutoff=0.6)
#     print(match)
#     if match:
#         team_names.append(match[0])
#         starting_index = match_string.find(match[0])
#         if starting_index == 0:
#             team_names.append(match_string[len(match[0]):len(match_string)])
#         else:
#             team_names.append(match_string[0:starting_index])
#         team_names.reverse()
#     print(team_names)


# extract_team_names_from_string(
#     "Sunrisers HyderabadGujarat Titans", valid_teams)


ov_pattern1 = r"\(([\d\.]+\/\d+ ov)"
ov_pattern2 = r"\((\d+ ov)"
overs = re.findall(
    ov_pattern1, "Punjab Kings191/5Kolkata Knight Riders(16/16 ov, T:154) 146/7")
overs.extend(re.findall(
    ov_pattern2, "Punjab Kings191/5Kolkata Knight Riders(16/16 ov, T:154) 146/7"))
overs2 = []
overs2 = re.findall(r"\(([\d\.]+\/\d+\.\d+ ov)",
                    "Punjab Kings191/5Kolkata Knight Riders(16/16 ov, T:154) 146/7")
overs.extend(overs2)
print(overs)
if len(overs) != 2:
    ov1 = "20/20 ov"
    ov2 = overs[0]
    if overs2:
        ov1 = "20/20 ov"
        ov2 = overs[0]
        # dls = find_present_substring(
        #     winners[j], "DLS", "XXXXXXXXXXXXXXX")
        # if dls == "DLS":
        #     dict_match['dls_affected'].append(True)
        # else:
        #     dict_match['dls_affected'].append(False)
    else:
        if ov2 == "20 ov":
            ov2 = "20/20 ov"
            # dls = find_present_substring(
            #     winners[j], "DLS", "XXXXXXXXXXXXXXX")
            # if dls == "DLS":
            #     dict_match['dls_affected'].append(True)
            # else:
            #     dict_match['dls_affected'].append(False)
        else:
            ov2 = overs[0]
            # dls = find_present_substring(
            #     winners[j], "DLS", "XXXXXXXXXXXXXXX")
            # if dls == "DLS":
            #     dict_match['dls_affected'].append(True)
            # else:
            #     dict_match['dls_affected'].append(False)
else:
    ov1 = overs[0]
    ov2 = overs[1]
    # dict_match["dls_affected"].append(True)
print(ov1, ov2)
