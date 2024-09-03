# from datetime import datetime
# f = ["Fri, 22 Mar '24", "Sat, 23 Mar '24", "Sat, 23 Mar '24", "Sun, 24 Mar '24", "Sun, 24 Mar '24", "Mon, 25 Mar '24", "Tue, 26 Mar '24", "Wed, 27 Mar '24", "Thu, 28 Mar '24", "Fri, 29 Mar '24", "Sat, 30 Mar '24", "Sun, 31 Mar '24", "Sun, 31 Mar '24", "Mon, 01 Apr '24", "Tue, 02 Apr '24", "Wed, 03 Apr '24", "Thu, 04 Apr '24", "Fri, 05 Apr '24", "Sat, 06 Apr '24", "Sun, 07 Apr '24", "Sun, 07 Apr '24", "Mon, 08 Apr '24", "Tue, 09 Apr '24", "Wed, 10 Apr '24", "Thu, 11 Apr '24", "Fri, 12 Apr '24", "Sat, 13 Apr '24", "Sun, 14 Apr '24", "Sun, 14 Apr '24", "Mon, 15 Apr '24", "Tue, 16 Apr '24", "Wed, 17 Apr '24", "Thu, 18 Apr '24", "Fri, 19 Apr '24", "Sat, 20 Apr '24", "Sun, 21 Apr '24", "Sun, 21 Apr '24",
#      "Mon, 22 Apr '24", "Tue, 23 Apr '24", "Wed, 24 Apr '24", "Thu, 25 Apr '24", "Fri, 26 Apr '24", "Sat, 27 Apr '24", "Sat, 27 Apr '24", "Sun, 28 Apr '24", "Sun, 28 Apr '24", "Mon, 29 Apr '24", "Tue, 30 Apr '24", "Wed, 01 May '24", "Thu, 02 May '24", "Fri, 03 May '24", "Sat, 04 May '24", "Sun, 05 May '24", "Sun, 05 May '24", "Mon, 06 May '24", "Tue, 07 May '24", "Wed, 08 May '24", "Thu, 09 May '24", "Fri, 10 May '24", "Sat, 11 May '24", "Sun, 12 May '24", "Sun, 12 May '24", "Mon, 13 May '24", "Tue, 14 May '24", "Wed, 15 May '24", "Thu, 16 May '24", "Fri, 17 May '24", "Sat, 18 May '24", "Sun, 19 May '24", "Sun, 19 May '24", "Tue, 21 May '24", "Wed, 22 May '24", "Fri, 24 May '24", "Sun, 26 May '24"]
# for i in f:
#     parsed_date = datetime.strptime(i, "%a, %d %b '%y")
#     print(parsed_date)
#     formatted_date = parsed_date.strftime("%Y-%m-%d")
#     print(type(formatted_date))
import re


def extract_match_details(match_string):
    # Patterns for extraction
    team_pattern = r"([A-Za-z\s]+)"
    score_pattern = r"(\d+\/\d+)"
    ov_pattern = r"\(([\d\.]+\/\d+ ov)\)"
    target_pattern = r"T: (\d+)"

    # Initialize variables
    team1, team2 = None, None
    ov1, ov2 = None, None
    score1, score2 = None, None
    target = None
    dls_affected = None

    # Find teams
    teams = re.findall(team_pattern, match_string)
    if teams:
        team1, team2 = teams[:2]

    # Find scores and overs
    scores = re.findall(score_pattern, match_string)
    if scores:
        score1 = scores[0]
        if len(scores) > 1:
            score2 = scores[1]

    # Find overs
    overs = re.findall(ov_pattern, match_string)
    if overs:
        ov1 = overs[0]
        if len(overs) > 1:
            ov2 = overs[1]

    # Find target
    target_match = re.search(target_pattern, match_string)
    if target_match:
        target = int(target_match.group(1))

    # Determine DLS affected
    if ov1 and ov1 != "20/20":
        dls_affected = True
    elif ov1:
        dls_affected = False

    # Print results
    print(f"team1 = {team1.strip() if team1 else None}")
    print(f"ov1 = {ov1 if ov1 else None}")
    print(f"score1 = {score1 if score1 else None}")
    print(f"team2 = {team2.strip() if team2 else None}")
    print(f"ov2 = {ov2 if ov2 else None}")
    print(f"score2 = {score2 if score2 else None}")
    print(f"target = {target if target else None}")
    print(f"dls_affected = {dls_affected}")


# Test cases
match_string1 = "Royal Challengers Bangalore(15/15 ov) 211/3Kings XI Punjab(14/14 ov, T: 203) 120/9"
match_string2 = "Royal Challengers Bangalore173/6Chennai Super Kings(18.4/20 ov, T: 174) 176/4"
match_string3 = "Rajasthan RoyalsKolkata Knight Riders"

print("Match 1:")
extract_match_details(match_string1)
print("\nMatch 2:")
extract_match_details(match_string2)
print("\nMatch 3:")
extract_match_details(match_string3)
