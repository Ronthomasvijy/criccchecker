import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import os
import re
from datetime import datetime, date
from team_name_obtain import extract_team_names_from_string, extract_team_names
from getmatch import get_winners

url_2008 = 'https://www.espncricinfo.com/series/indian-premier-league-2007-08-313494/match-schedule-fixtures-and-results'
url_2009 = 'https://www.espncricinfo.com/series/indian-premier-league-2009-374163/match-schedule-fixtures-and-results'
url_2010 = 'https://www.espncricinfo.com/series/indian-premier-league-2009-10-418064/match-schedule-fixtures-and-results'
url_2011 = 'https://www.espncricinfo.com/series/indian-premier-league-2011-466304/match-schedule-fixtures-and-results'
url_2012 = 'https://www.espncricinfo.com/series/indian-premier-league-2012-520932/match-schedule-fixtures-and-results'
url_2013 = 'https://www.espncricinfo.com/series/indian-premier-league-2013-586733/match-schedule-fixtures-and-results'
url_2014 = 'https://www.espncricinfo.com/series/pepsi-indian-premier-league-2014-695871/match-schedule-fixtures-and-results'
url_2015 = 'https://www.espncricinfo.com/series/pepsi-indian-premier-league-2015-791129/match-schedule-fixtures-and-results'
url_2016 = 'https://www.espncricinfo.com/series/ipl-2016-968923/match-schedule-fixtures-and-results'
url_2017 = 'https://www.espncricinfo.com/series/ipl-2017-1078425/match-schedule-fixtures-and-results'
url_2018 = 'https://www.espncricinfo.com/series/ipl-2018-1131611/match-schedule-fixtures-and-results'
url_2019 = 'https://www.espncricinfo.com/series/ipl-2019-1165643/match-schedule-fixtures-and-results'
url_2020 = 'https://www.espncricinfo.com/series/ipl-2020-21-1210595/match-schedule-fixtures-and-results'
url_2021 = 'https://www.espncricinfo.com/series/ipl-2021-1249214/match-schedule-fixtures-and-results'
url_2022 = 'https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/match-schedule-fixtures-and-results'
url_2023 = 'https://www.espncricinfo.com/series/indian-premier-league-2023-1345038/match-schedule-fixtures-and-results'
url_2024 = 'https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/match-schedule-fixtures-and-results'
match_year = [url_2008, url_2009, url_2010, url_2011, url_2012, url_2013, url_2014, url_2015,
              url_2016, url_2017, url_2018, url_2019, url_2020, url_2021, url_2022, url_2023, url_2024]
matches = []
match_dates = []
matches.clear
match_dates.clear
valid_teams = ["Pune Warriors", "Deccan Chargers", "Delhi Daredevils", "Mumbai Indians", "Chennai Super Kings", "Kolkata Knight Riders", "Punjab Kings", "Lucknow Super Giants",
               "Gujarat Titans", "Sunrisers Hyderabad", "Delhi Capitals", "Royal Challengers Bengaluru", "Royal Challengers Bangalore", "Rajasthan Royals", "Kings XI Punjab", "Kochi Tuskers Kerala", "Rising Pune Supergiant", "Gujarat Lions"]

ur_2008 = 'https://www.cricbuzz.com/cricket-series/2058/indian-premier-league-2008/matches'
ur_2009 = 'https://www.cricbuzz.com/cricket-series/2059/indian-premier-league-2009/matches'
ur_2010 = 'https://www.cricbuzz.com/cricket-series/2060/indian-premier-league-2010/matches'
ur_2011 = 'https://www.cricbuzz.com/cricket-series/2037/indian-premier-league-2011/matches'
ur_2012 = 'https://www.cricbuzz.com/cricket-series/2115/indian-premier-league-2012/matches'
ur_2013 = 'https://www.cricbuzz.com/cricket-series/2170/indian-premier-league-2013/matches'
ur_2014 = 'https://www.cricbuzz.com/cricket-series/2261/indian-premier-league-2014/matches'
ur_2015 = 'https://www.cricbuzz.com/cricket-series/2330/indian-premier-league-2015/matches'
ur_2016 = 'https://www.cricbuzz.com/cricket-series/2430/indian-premier-league-2016/matches'
ur_2017 = 'https://www.cricbuzz.com/cricket-series/2568/indian-premier-league-2017/matches'
ur_2018 = 'https://www.cricbuzz.com/cricket-series/2676/indian-premier-league-2018/matches'
ur_2019 = 'https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/matches'
ur_2020 = 'https://www.cricbuzz.com/cricket-series/3130/indian-premier-league-2020/matches'
ur_2021 = 'https://www.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/matches'
ur_2022 = 'https://www.cricbuzz.com/cricket-series/4061/indian-premier-league-2022/matches'
ur_2023 = 'https://www.cricbuzz.com/cricket-series/5945/indian-premier-league-2023/matches'
ur_2024 = 'https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches'
_year = [ur_2008, ur_2009, ur_2010, ur_2011, ur_2012, ur_2013, ur_2014, ur_2015,
         ur_2016, ur_2017, ur_2018, ur_2019, ur_2020, ur_2021, ur_2022, ur_2023, ur_2024]


#returning link of match details
def s_year(i):
    i = i-2008
    if i < len(match_year):
        return match_year[i]

#scraping match details
def get_matches(url):
    matches = []
    webpage = requests.get(url)
    web = webpage.content
    soup = BeautifulSoup(web, "html.parser")
    q = soup.find_all(
        'div', class_='ds-flex ds-flex-col ds-mt-2 ds-mb-2')
    for i in q:
        matches.append(i.text)
    return matches

#scraping match dates
def get_dates(url):
    matches = []
    prev = ""
    webpage = requests.get(url)
    web = webpage.content
    soup = BeautifulSoup(web, "html.parser")
    q = soup.find_all(
        'div', class_='ds-text-compact-xs ds-font-bold ds-w-24')
    for i in q:
        if len(i.text) == 0:
            matches.append(prev)
        else:
            prev = i.text
            matches.append(i.text)
    return matches


count = 0


def find_present_substring(main_string, substring1, substring2):
    # print(main_string, "----", substring1, "----", substring2)
    if substring1 in main_string and substring2 in main_string:
        return (substring1, substring2)
    elif substring1 in main_string:
        return substring1
    elif substring2 in main_string:
        return substring2
    else:
        return "NO RESULT"

#if match year is 2021 match details is brought from 2021.csv
def add_to_csv_2021():
    with open('2021.csv', mode='r', newline='', encoding='utf-8') as infile:
        reader1 = csv.reader(infile)

        # Open the destination CSV file in write mode to empty it and prepare for new content
        with open('data.csv', mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)

            # Copy each row from the source to the destination file
            for row in reader1:
                writer.writerow(row)
    print(f"Data has been written to data.csv")



#entering scraped details to data.csv file
def add_to_csv(filename, matches, dates, winners):
    j = 0
    filename = "data.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w+")
    f.close()
    columns = ['match_no', 'match_date', 'team_name1', 'score1', 'overs_batted1',
               'team_name2', 'score2', 'overs_batted2', 'target', 'victory', 'dls_affected']
    df = pd.DataFrame(columns=columns)
    # Save the DataFrame to a CSV file
    df.to_csv('data.csv', index=False)

    dict_match = {key: [] for key in columns}
    team_pattern = r"([A-Za-z\s]+)"
    ov_pattern = r"\(([\d\.]+\/\d+ ov)"
    count = 0
    print(winners)
    for i in range(len(matches)):
        print("---------------------------------------------------------------------------------------------------------")

        print(i+1, matches[i])

        dict_match["match_no"].append(i+1)
        parsed_date = datetime.strptime(dates[i], "%a, %d %b '%y")
        formatted_date = parsed_date.strftime("%Y-%m-%d")
        dict_match["match_date"].append(formatted_date)
        if not re.fullmatch(team_pattern, matches[i]):
            count = count+1
            extracted_team_names = []
            teams = []

            teams = re.findall(team_pattern, matches[i])
            extracted_team_names = extract_team_names(teams, valid_teams)
            t1 = extracted_team_names[0]
            dict_match['team_name1'].append(t1)
            print(r"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
            print(t1)
            t2 = extracted_team_names[1]
            dict_match['team_name2'].append(t2)
            print(r"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
            print(t2)
            while winners[j] == "Match rescheduled due to Covid-19 pandemic" or winners[j] == "Match postponed due to Covid-19 pandemic":
                j = j+1
            vic = find_present_substring(winners[j], t1, t2)
            if vic == "NO RESULT":
                full_name = t1+" "+t2
                short_name = full_name.split()
                for short in short_name:
                    if short in winners[j] and short in t1:
                        vic = t1
                    elif short in winners[j] and short in t2:
                        vic = t2
            dict_match['victory'].append(vic)
            print(r"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
            print(vic)

            target_pattern1 = r"T:(\d+)"
            t = re.findall(target_pattern1, matches[i])
            if t:
                tar = int(t[0])
                dict_match['target'].append(tar)
                print(r"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
                print(tar)
                ov_pattern1 = r"\(([\d\.]+\/\d+ ov)"
                ov_pattern2 = r"\((\d+ ov)"
                overs = re.findall(ov_pattern1, matches[i])
                overs.extend(re.findall(ov_pattern2, matches[i]))
                overs2 = []
                overs2 = re.findall(r"\(([\d\.]+\/\d+\.\d+ ov)", matches[i])
                overs.extend(overs2)
                print(r"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
                print(overs)
                if len(overs) != 2:
                    ov1 = "20/20 ov"
                    ov2 = overs[0]
                    if overs2:
                        ov1 = "20/20 ov"
                        ov2 = overs[0]
                        dls = find_present_substring(
                            winners[j], "DLS", "D/L")
                        if dls == "DLS":
                            dict_match['dls_affected'].append(True)
                        elif dls == "D/L":
                            dict_match['dls_affected'].append(True)
                        else:
                            dict_match['dls_affected'].append(False)
                    else:
                        if ov2 == "20 ov":
                            ov2 = "20/20 ov"
                            dls = find_present_substring(
                                winners[j], "DLS", "D/L")
                            if dls == "DLS":
                                dict_match['dls_affected'].append(True)
                            elif dls == "D/L":
                                dict_match['dls_affected'].append(True)
                            else:
                                dict_match['dls_affected'].append(False)
                        else:
                            ov2 = overs[0]
                            dls = find_present_substring(
                                winners[j], "DLS", "D/L")
                            if dls == "DLS":
                                dict_match['dls_affected'].append(True)
                            elif dls == "D/L":
                                dict_match['dls_affected'].append(True)
                            else:
                                dict_match['dls_affected'].append(False)

                else:
                    ov1 = overs[0]
                    ov2 = overs[1]
                    if matches[i].find(ov1) > matches[i].find(ov2):
                        ov1, ov2 = ov2, ov1
                    dict_match["dls_affected"].append(True)
                dict_match['overs_batted1'].append(ov1)
                dict_match['overs_batted2'].append(ov2)
                print(r"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
                print(ov1, "    ---    ", ov2)
                score_pattern1 = r'\)\s(\d+(/\d+)?)'
                score_pattern2 = r'[a-zA-Z](\d+(/\d+)?)[a-zA-Z]'
                matches1 = re.findall(score_pattern1, matches[i])
                cleaned_matches1 = [match[0] for match in matches1]
                matches2 = re.findall(score_pattern2, matches[i])
                # Filter out any matches that do not meet the full pattern requirement
                # ensure the match starts with digits
                cleaned_matches2 = [match[0] for match in matches2]
                cleaned_matches1.extend(cleaned_matches2)
                if len(cleaned_matches1) == 2:
                    if matches[i].find(cleaned_matches1[0]) > matches[i].find(cleaned_matches1[1]):
                        cleaned_matches1[0], cleaned_matches1[1] = cleaned_matches1[1], cleaned_matches1[0]
                dict_match['score1'].append(cleaned_matches1[0])
                dict_match['score2'].append(cleaned_matches1[1])
                print(r"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
                print(cleaned_matches1[0], "          ", cleaned_matches1[1])
            else:
                dict_match["dls_affected"].append(False)
                dict_match['target'].append(None)
                dict_match['score1'].append(None)
                dict_match['score2'].append(None)
                dict_match['overs_batted1'].append(None)
                dict_match['overs_batted2'].append(None)

        else:
            print(matches[i])
            extracted_team_names = extract_team_names_from_string(
                matches[i], valid_teams)
            print(extract_team_names_from_string)
            t1 = extracted_team_names[0]
            dict_match['team_name1'].append(t1)
            t2 = extracted_team_names[1]
            dict_match['team_name2'].append(t2)
            extracted_team_names = []
            teams = []
            dict_match['dls_affected'].append(False)
            dict_match['target'].append(None)
            dict_match['score1'].append(None)
            dict_match['score2'].append(None)
            dict_match['overs_batted1'].append(None)
            dict_match['overs_batted2'].append(None)
            vic = find_present_substring(winners[j], t1, t2)
            dict_match['victory'].append(vic)
        j = j+1
    
    df = pd.DataFrame(dict_match)
    file_path = os.path.join(os.getcwd(), filename)

    try:
        df.to_csv(file_path, index=False)
        print(f"Data has been written to {file_path}")
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        df.to_csv(filename, index=False)

#code for testing functions



# yearrr = int(input("enter year:"))
# matches = get_matches(match_year[yearrr-2008])

# t = get_dates(match_year[yearrr-2008])
# winners = get_winners(_year[yearrr-2008])
# print(winners)
# add_to_csv("data.csv", matches, t, winners)
