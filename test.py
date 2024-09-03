from difflib import get_close_matches
import pandas as pd
import re
valid_teams = ["Deccan Chargers", "Delhi Daredevils", "Mumbai Indians", "Chennai Super Kings", "Kolkata Knight Riders", "Punjab Kings", "Lucknow Super Giants",
               "Gujarat Titans", "Sunrisers Hyderabad", "Delhi Capitals", "Royal Challengers Bengaluru", "Royal Challengers Bengalore", "Rajasthan Royals", "Kings XI Punjab", "Kochi Tuskers Kerala", "Rising Pune Super Giants", "Gujarat Lions"]


def extract_team_names(string_list, valid_teams):
    # Filter out potential team names from the string list using difflib's get_close_matches
    team_names = []
    for item in string_list:
        match = get_close_matches(item.strip(), valid_teams, n=1, cutoff=0.6)
        if match:
            team_names.append(match[0])
    return team_names


def extract_team_names_from_string(match_string, valid_teams):
    team_names = []
    match = get_close_matches(match_string.strip(),
                              valid_teams, n=1, cutoff=0.6)
    if match:
        team_names.append(match[0])
        starting_index = match_string.find(match[0])
        if starting_index == 0:
            team_names.append(match_string[len(match[0]):len(match_string)])
        else:
            team_names.append(match_string[0:starting_index])
        team_names.reverse()
    return team_names


# match_string1 = "Royal Challengers Bangalore(15/15 ov) 211/3Kings XI Punjab(14/14 ov, T:203) 120/9"
# match_string2 = "Royal Challengers Bangalore173/6Chennai Super Kings(18.4/20 ov, T:174) 176/4"
# m = [match_string1, match_string2, "Lucknow Super Giants181/5Royal Challengers Bengaluru(19.4/20 ov, T:182) 153", "Gujarat Titans89Delhi Capitals(8.5/20 ov, T:90) 92/4",
#      "Kolkata Knight Riders174/6Rajasthan Royals(20 ov, T:175) 137/9", "Lucknow Super Giants(19.2/20 ov) 125/7Chennai Super Kings", "Royal Challengers Bangalore(15/15 ov) 2332/213 Kings XI Punjab(14/14 ov, T:203) 1233"]
# hello = re.findall(
#     r"\(([\d\.]+\/\d+\.\d+ ov)", "Royal Challengers Bangalore(15.1/15.1 ov) 211/3Kings XI Punjab(14/14 ov, T:203) 120/9")
# print(hello)
# k = re.findall(r"\/[\d+.\d+]", hello[0])
# print(k)
