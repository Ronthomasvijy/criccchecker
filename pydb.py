#this  is used only for testing different part of codes for debugging and error correction even without this file the code works.
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
