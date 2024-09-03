import pandas as pd
import os
import re
import csv
from datetime import datetime, date


def convert_dict_to_list(input_dict):
    output_list = []
    for team, stats in input_dict.items():
        output_list.append([[team], stats])
    return output_list

# Example usage


def convert_list_to_dict(input_list):
    output_dict = {}
    for item in input_list:
        team = item[0][0]  # Extract the team name
        stats = item[1]    # Extract the statistics list
        output_dict[team] = stats
    return output_dict


def get_table():
    output_string_list = [[], [], [], [], [], []]
    output = []
    # print(f"Data successfully copied from {source_file} to {destination_file}.")
    # if year==2021:
    #     df = pd.read_csv('2021.csv')
    # else:
    df = pd.read_csv('data.csv')
    row1 = df['team_name1'].unique()
    dict_table = {}
    dict_values = {}
    dict_table = {key: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for key in row1}
    dict_scored = {key: [] for key in row1}
    dict_over = {key: [] for key in row1}
    # print(dict_table)
    parsed_date1 = datetime.strptime(df.iloc[0]['match_date'], "%Y-%m-%d")
    date_string = "2010-01-01"
    parsed_date2 = datetime.strptime(date_string, "%Y-%m-%d")
    if parsed_date1 < parsed_date2:
        n = 3
    else:
        n = 4
    for i in range(len(df)-n):
        row = df.iloc[i]
        t1 = row['team_name1']
        t2 = row['team_name2']
        if row['victory'] == t1:
            dict_table[t1][1] += 1
            dict_table[t1][7] += 2
            dict_table[t2][2] += 1
        elif row['victory'] == t2:
            dict_table[t2][1] += 1
            dict_table[t2][7] += 2
            dict_table[t1][2] += 1
        else:
            dict_table[t1][7] += 1
            dict_table[t2][7] += 1
        dict_table[t1][0] += 1
        dict_table[t2][0] += 1
        if (row['dls_affected'] == False):
            if row['victory'] != "NO RESULT" and row['victory'] != None:
                score1 = str(row['score1']).split('/')[0]
                dict_table[t1][3] += float(score1)
                dict_table[t1][4] += 20
                dict_table[t2][5] += float(score1)
                dict_table[t2][6] += 20
# /////////////////////////////////////////////////////////////////////////////////////////////////////////
                dict_scored[t1].append(float(score1))
                dict_over[t1].append(20)
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                # if t2 == "Kolkata Knight Riders":
                #     print(float(score1), "+")
                score2 = str(row['score2']).split('/')[0]
                # print(row['target'])
                if int(row['target']) > int(score2) or int(score1) == int(score2):
                    dict_table[t2][3] += float(score2)
                    dict_table[t2][4] += 20
                    dict_table[t1][5] += float(score2)
                    dict_table[t1][6] += 20


# ////////////////////////////////////////////////////////////////////////////////////////////////
                    dict_scored[t2].append(float(score2))
                    dict_over[t2].append(20)
# ///////////////////////////////////////////////////////////////////////////////////////////////////
                    # if t1 == "Kolkata Knight Riders":
                    #     print(float(score2), "+")

                elif int(row['target']) <= int(score2):
                    dict_table[t2][3] += float(score2)
                    dict_table[t2][4] += float(
                        row['overs_batted2'].split('/')[0])//1
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    dict_scored[t2].append(float(score2))
                    dict_over[t2].append(
                        float(row['overs_batted2'].split('/')[0])//1)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    if int(float(row['overs_batted2'].split('/')[0])*10) % 10 != 0:
                        dict_table[t2][8] += int(
                            float(row['overs_batted2'].split('/')[0])*10) % 10

                        if t2 == "Rising Pune Supergiants":
                            print("\n", dict_table[t2][8], float(row['overs_batted2'].split('/')[0]),
                                  "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")

                    dict_table[t1][5] += float(score2)
                    dict_table[t1][6] += float(
                        row['overs_batted2'].split('/')[0])//1

                    # if t1 == "Kolkata Knight Riders":
                    #     print(
                    #         float(score2), "+")

                    if int(float(row['overs_batted2'].split('/')[0])*10) % 10 != 0:
                        dict_table[t1][9] += int(
                            float(row['overs_batted2'].split('/')[0])*10) % 10

                    # if t1 == "Kolkata Knight Riders":
                    #     print(
                    #         int(float(row['overs_batted2'].split('/')[0])*10) % 10, "+")

        elif (row['dls_affected'] == True) and row['victory'] != "NO RESULT":
            score1 = str(row['score1']).split('/')[0]
            dict_table[t1][3] += float(row['target'])-1
            overs1 = float(row['overs_batted2'].split('ov')
                           [0].split('/')[1])//1
            dict_table[t1][4] += overs1
            print("-------------", t1, t2, overs1,
                  "+++++++++++++++++++++\n")
            dict_scored[t1].append(float(row['target'])-1)
            dict_over[t1].append(overs1)

            dict_table[t2][5] += float(row['target'])-1
            dict_table[t2][6] += overs1
            score2 = str(row['score2']).split('/')[0]
            if int(float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10 != 0:
                dict_table[t1][8] += int(
                    float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10

                if t1 == "Rising Pune Supergiants":
                    print("\n", dict_table[t1][8],
                          float(row['overs_batted1'].split('/')[0]),
                          "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")

                dict_table[t2][9] += int(
                    float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10

                # if t2 == "Kolkata Knight Riders":
                #     print("-----------------------",
                #           float(score1), "+")

            if int(row['target']) > int(score2) or int(score1) == int(score2):
                dict_table[t2][3] += float(score2)
                dict_table[t2][4] += float(row['overs_batted2'].split('ov')
                                           [0].split('/')[1])//1

# //////////////////////////////////////////////////////////////////////////////////////////////
                dict_scored[t2].append(float(score2))
                dict_over[t2].append(
                    float(row['overs_batted2'].split('ov')[0].split('/')[1])//1)
# //////////////////////////////////////////////////////////////////////////////////////////////
                if int(float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10 != 0:
                    dict_table[t2][8] += int(
                        float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10

                    if t2 == "Rising Pune Supergiants":
                        print("\n", dict_table[t2][8], float(row['overs_batted2'].split('/')[0]),
                              "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")

                    dict_table[t1][9] += int(
                        float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10

                    # if t1 == "Kolkata Knight Riders":
                    #     print(int(float(row['overs_batted2'].split(
                    #         'ov')[0].split('/')[1])*10) % 10, "+")

                dict_table[t1][5] += float(score2)

                dict_table[t1][6] += float(row['overs_batted2'].split('ov')
                                           [0].split('/')[1])//1
                if t1 == "Kolkata Knight Riders":
                    print(float(score2), "+")

            elif int(row['target']) <= int(score2):
                dict_table[t2][3] += float(score2)
                dict_table[t2][4] += float(
                    row['overs_batted2'].split('/')[0])//1

# /////////////////////////////////////////////////////////////////////////////////////////////////////////

                dict_scored[t2].append(float(score2))
                dict_over[t2].append(
                    float(row['overs_batted2'].split('/')[0])//1)


# /////////////////////////////////////////////////////////////////////////////////////////////
                if int(float(row['overs_batted2'].split('/')[0])*10) % 10 != 0:
                    dict_table[t2][8] += int(float(
                        row['overs_batted2'].split('/')[0])*10) % 10

                    if t2 == "Rising Pune Supergiants":
                        print("\n", dict_table[t2][8], float(row['overs_batted2'].split('/')[0]),
                              "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")

                    dict_table[t1][9] += int(float(
                        row['overs_batted2'].split('/')[0])*10) % 10

                    # if t1 == "Kolkata Knight Riders":
                    #     print(
                    #         int(float(row['overs_batted2'].split('/')[0])*10) % 10, "+")

                dict_table[t1][5] += float(score2)
                dict_table[t1][6] += float(
                    row['overs_batted2'].split('/')[0])//1

                # if t1 == "Kolkata Knight Riders":
                #     print(float(score2), "+")

    # print(dict_table)
    sorted_teams = dict(
        sorted(dict_table.items(), key=lambda item: item[1][7], reverse=True))
    # print("++++++++\n", sorted_teams)
    for i in sorted_teams:
        sorted_teams[i][10] = (sorted_teams[i][3]/(sorted_teams[i][4]+(sorted_teams[i][8]/6)))-(
            sorted_teams[i][5]/(sorted_teams[i][6]+(sorted_teams[i][9]/6)))
        # print(i, "-->", sorted_teams[i], "---->", (sorted_teams[i][3]/(sorted_teams[i][4]+(
        #     sorted_teams[i][8]/6)))-(sorted_teams[i][5]/(sorted_teams[i][6]+(sorted_teams[i][9]/6))))
    sorted_d = dict(sorted(sorted_teams.items(),
                    key=lambda item: (-item[1][7], -item[1][10])))
    # output_string_list = list(sorted_d.items())
    output_string_list[0].append("TEAM")
    output_string_list[1].append("MATCHES")
    output_string_list[2].append("WON")
    output_string_list[3].append("LOST")
    output_string_list[4].append("POINTS")
    output_string_list[5].append("NRR")
    for d in sorted_d:
        output_string_list[0].append(d)
        output_string_list[1].append(sorted_d[d][0])
        output_string_list[2].append(sorted_d[d][1])
        output_string_list[3].append(sorted_d[d][2])
        output_string_list[4].append(sorted_d[d][7])
        output_string_list[5].append(sorted_d[d][10])

    return output_string_list
    # for i in sorted_d:
    #     print(i, "-->", sorted_d[i])
    #     output_string_list.append(i)
    #     output_string_list.append("")
    # for i in dict_over:
    #     print(i, "---->", dict_over[i])


def get_date_from_to():
    n = 0
    date_from_to = []
    df = pd.read_csv('data.csv')
    date1 = datetime.strptime(df.iloc[0]['match_date'], "%Y-%m-%d")
    date_string = "2010-01-01"
    date2 = datetime.strptime(date_string, "%Y-%m-%d")
    if date1 < date2:
        n = -4
    else:
        n = -5
    date3 = datetime.strptime(df.iloc[n]['match_date'], "%Y-%m-%d")
    date_from_to.append(df.iloc[0]['match_date'])
    date_from_to.append(df.iloc[n]['match_date'])
    date_from_to.append(date1)
    date_from_to.append(date3)
    return date_from_to

# get_table()


def get_ptable(date_entered):
    output_string_list = [[], [], [], [], [], []]
    output = []
    df = pd.read_csv('data.csv')
    row1 = df['team_name1'].unique()
    dict_table = {}
    dict_values = {}
    dict_table = {key: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for key in row1}
    dict_scored = {key: [] for key in row1}
    dict_over = {key: [] for key in row1}
    # print(dict_table)
    parsed_date1 = datetime.strptime(df.iloc[0]['match_date'], "%Y-%m-%d")
    date_string = "2010-01-01"
    parsed_date2 = datetime.strptime(date_string, "%Y-%m-%d")
    parsed_date3 = datetime.strptime(date_entered, "%Y-%m-%d")
    if parsed_date1 < parsed_date2:
        n = 3
    else:
        n = 4
    for i in range(len(df)-n):
        row = df.iloc[i]
        current_date = datetime.strptime(df.iloc[i]['match_date'], "%Y-%m-%d")
        if current_date < parsed_date3:
            t1 = row['team_name1']
            t2 = row['team_name2']
            if row['victory'] == t1:
                dict_table[t1][1] += 1
                dict_table[t1][7] += 2
                dict_table[t2][2] += 1
            elif row['victory'] == t2:
                dict_table[t2][1] += 1
                dict_table[t2][7] += 2
                dict_table[t1][2] += 1
            else:
                dict_table[t1][7] += 1
                dict_table[t2][7] += 1
            dict_table[t1][0] += 1
            dict_table[t2][0] += 1
            if (row['dls_affected'] == False):
                if row['victory'] != "NO RESULT" and row['victory'] != None:
                    score1 = str(row['score1']).split('/')[0]
                    dict_table[t1][3] += float(score1)
                    dict_table[t1][4] += 20
                    dict_table[t2][5] += float(score1)
                    dict_table[t2][6] += 20
# /////     ///////////////////////////////////////////////////////////////////////////////////////////////////
                    dict_scored[t1].append(float(score1))
                    dict_over[t1].append(20)
# /////     //////////////////////////////////////////////////////////////////////////////////////////////////////////////
                    # if t2 == "Kolkata Knight Riders":
                    #     print(float(score1), "+")
                    score2 = str(row['score2']).split('/')[0]
                    # print(row['target'])
                    if int(row['target']) > int(score2) or int(score1) == int(score2):
                        dict_table[t2][3] += float(score2)
                        dict_table[t2][4] += 20
                        dict_table[t1][5] += float(score2)
                        dict_table[t1][6] += 20


# /////     //////////////////////////////////////////////////////////////////////////////////////////
                        dict_scored[t2].append(float(score2))
                        dict_over[t2].append(20)
# /////     /////////////////////////////////////////////////////////////////////////////////////////////
                        # if t1 == "Kolkata Knight Riders":
                        #     print(float(score2), "+")

                    elif int(row['target']) <= int(score2):
                        dict_table[t2][3] += float(score2)
                        dict_table[t2][4] += float(
                            row['overs_batted2'].split('/')[0])//1
# /////     ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        dict_scored[t2].append(float(score2))
                        dict_over[t2].append(
                            float(row['overs_batted2'].split('/')[0])//1)
# /////     /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                        if int(float(row['overs_batted2'].split('/')[0])*10) % 10 != 0:
                            dict_table[t2][8] += int(
                                float(row['overs_batted2'].split('/')[0])*10) % 10

                            if t2 == "Rising Pune Supergiants":
                                print("\n", dict_table[t2][8], float(row['overs_batted2'].split('/')[0]),
                                      "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")

                        dict_table[t1][5] += float(score2)
                        dict_table[t1][6] += float(
                            row['overs_batted2'].split('/')[0])//1

                        # if t1 == "Kolkata Knight Riders":
                        #     print(
                        #         float(score2), "+")

                        if int(float(row['overs_batted2'].split('/')[0])*10) % 10 != 0:
                            dict_table[t1][9] += int(
                                float(row['overs_batted2'].split('/')[0])*10) % 10

                        # if t1 == "Kolkata Knight Riders":
                        #     print(
                        #         int(float(row['overs_batted2'].split('/')[0])*10) % 10, "+")

            elif (row['dls_affected'] == True) and row['victory'] != "NO RESULT":
                score1 = str(row['score1']).split('/')[0]
                dict_table[t1][3] += float(row['target'])-1
                overs1 = float(row['overs_batted2'].split('ov')
                               [0].split('/')[1])//1
                dict_table[t1][4] += overs1
                print("-------------", t1, t2, overs1,
                      "+++++++++++++++++++++\n")
                dict_scored[t1].append(float(row['target'])-1)
                dict_over[t1].append(overs1)

                dict_table[t2][5] += float(row['target'])-1
                dict_table[t2][6] += overs1
                score2 = str(row['score2']).split('/')[0]
                if int(float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10 != 0:
                    dict_table[t1][8] += int(
                        float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10

                    if t1 == "Rising Pune Supergiants":
                        print("\n", dict_table[t1][8],
                              float(row['overs_batted1'].split('/')[0]),
                              "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")

                    dict_table[t2][9] += int(
                        float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10

                    # if t2 == "Kolkata Knight Riders":
                    #     print("-----------------------",
                    #           float(score1), "+")

                if int(row['target']) > int(score2) or int(score1) == int(score2):
                    dict_table[t2][3] += float(score2)
                    dict_table[t2][4] += float(row['overs_batted2'].split('ov')
                                               [0].split('/')[1])//1

# /////////////////////////////////////////////////////////////////////////////////////////////
                    dict_scored[t2].append(float(score2))
                    dict_over[t2].append(
                        float(row['overs_batted2'].split('ov')[0].split('/')[1])//1)
# /////////////////////////////////////////////////////////////////////////////////////////////
                    if int(float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10 != 0:
                        dict_table[t2][8] += int(
                            float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10

                        if t2 == "Rising Pune Supergiants":
                            print("\n", dict_table[t2][8], float(row['overs_batted2'].split('/')[0]),
                                  "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")

                        dict_table[t1][9] += int(
                            float(row['overs_batted2'].split('ov')[0].split('/')[1])*10) % 10

                        # if t1 == "Kolkata Knight Riders":
                        #     print(int(float(row['overs_batted2'].split(
                        #         'ov')[0].split('/')[1])*10) % 10, "+")

                    dict_table[t1][5] += float(score2)

                    dict_table[t1][6] += float(row['overs_batted2'].split('ov')
                                               [0].split('/')[1])//1
                    if t1 == "Kolkata Knight Riders":
                        print(float(score2), "+")

                elif int(row['target']) <= int(score2):
                    dict_table[t2][3] += float(score2)
                    dict_table[t2][4] += float(
                        row['overs_batted2'].split('/')[0])//1

# /////     ///////////////////////////////////////////////////////////////////////////////////////////////////

                    dict_scored[t2].append(float(score2))
                    dict_over[t2].append(
                        float(row['overs_batted2'].split('/')[0])//1)


# /////     ///////////////////////////////////////////////////////////////////////////////////////
                    if int(float(row['overs_batted2'].split('/')[0])*10) % 10 != 0:
                        dict_table[t2][8] += int(float(
                            row['overs_batted2'].split('/')[0])*10) % 10

                        if t2 == "Rising Pune Supergiants":
                            print("\n", dict_table[t2][8], float(row['overs_batted2'].split('/')[0]),
                                  "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")

                        dict_table[t1][9] += int(float(
                            row['overs_batted2'].split('/')[0])*10) % 10

                        # if t1 == "Kolkata Knight Riders":
                        #     print(
                        #         int(float(row['overs_batted2'].split('/')[0])*10) % 10, "+")

                    dict_table[t1][5] += float(score2)
                    dict_table[t1][6] += float(
                        row['overs_batted2'].split('/')[0])//1

                    # if t1 == "Kolkata Knight Riders":
                    #     print(float(score2), "+")

    # print(dict_table)
    sorted_teams = dict(
        sorted(dict_table.items(), key=lambda item: item[1][7], reverse=True))
    # print("++++++++\n", sorted_teams)
    try:
        for i in sorted_teams:
            sorted_teams[i][10] = (sorted_teams[i][3]/(sorted_teams[i][4]+(sorted_teams[i][8]/6)))-(
                sorted_teams[i][5]/(sorted_teams[i][6]+(sorted_teams[i][9]/6)))
            # print(i, "-->", sorted_teams[i], "---->", (sorted_teams[i][3]/(sorted_teams[i][4]+(
            #     sorted_teams[i][8]/6)))-(sorted_teams[i][5]/(sorted_teams[i][6]+(sorted_teams[i][9]/6))))
    except ZeroDivisionError:
        return [], []

    sorted_d = dict(sorted(sorted_teams.items(),
                    key=lambda item: (-item[1][7], -item[1][10])))
    # for i in sorted_d:
    #     print(i,"    ",sorted_d[i])
    # output_string_list = list(sorted_d.items())
    output_string_list[0].append("TEAM")
    output_string_list[1].append("MATCHES")
    output_string_list[2].append("WON")
    output_string_list[3].append("LOST")
    output_string_list[4].append("POINTS")
    output_string_list[5].append("NRR")
    for d in sorted_d:
        output_string_list[0].append(d)
        output_string_list[1].append(sorted_d[d][0])
        output_string_list[2].append(sorted_d[d][1])
        output_string_list[3].append(sorted_d[d][2])
        output_string_list[4].append(sorted_d[d][7])
        output_string_list[5].append(sorted_d[d][10])

    return output_string_list, sorted_d


def get_rem(date_entered):
    output_string_list = [[], [], [], []]
    df = pd.read_csv('data.csv')
    # print(dict_table)
    parsed_date1 = datetime.strptime(df.iloc[0]['match_date'], "%Y-%m-%d")
    date_string = "2010-01-01"
    parsed_date2 = datetime.strptime(date_string, "%Y-%m-%d")
    parsed_date3 = datetime.strptime(date_entered, "%Y-%m-%d")
    if parsed_date1 < parsed_date2:
        n = 3
    else:
        n = 4
    for i in range(len(df)-n):
        row = df.iloc[i]
        current_date = datetime.strptime(df.iloc[i]['match_date'], "%Y-%m-%d")
        if current_date < parsed_date3:
            continue
        else:
            output_string_list[0].append(row['match_date'])
            output_string_list[1].append(row['team_name1'])
            output_string_list[2].append("v/s")
            output_string_list[3].append(row['team_name2'])
    return output_string_list


# output_here = get_table()
# for i in range(len(output_here[0])):
#     print(output_here[0][i], "\t\t", output_here[1][i], "\t", output_here[2][i], "\t",
#           output_here[3][i], "\t", output_here[4][i], "\t", output_here[5][i], "\t")
# print("\n")
# z1, z2 = get_ptable("2024-05-18")
# for i in range(len(z1[0])):
#     print(z1[0][i], "\t\t", z1[1][i], "\t", z1[2][i], "\t",
#           z1[3][i], "\t", z1[4][i], "\t", z1[5][i], "\t")
# print("\n")
# print(z2)
# print("\n")
# print(get_rem("2024-05-18"))
