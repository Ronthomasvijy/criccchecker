import pandas as pd
import os
import re
import csv
from datetime import datetime, date
from c_table import get_ptable, get_rem, get_table


def nextmatch_update(win,flag,result2, first_batting, second_batting, score1, score2, ov2):
    output_string_list = [[], [], [], [], [], []]
    temp_result = result2
    print("\n")
    for i in temp_result:
        print(i,"    ", temp_result[i])
    if flag==0:
        print("hello")
        temp_result[first_batting][0] += 1
        temp_result[second_batting][0] += 1
        temp_result[first_batting][7] += 1
        temp_result[second_batting][7] += 1
    
    elif flag==1:
        print("hello")
        temp_result[first_batting][3] += score1
        temp_result[second_batting][5] += score1
        temp_result[first_batting][4] += 20
        temp_result[second_batting][6] += 20

        temp_result[first_batting][5] += score2
        temp_result[second_batting][3] += score2
        temp_result[first_batting][6] += int(ov2//1)
        temp_result[first_batting][9] += int((ov2*10) % 10)
        temp_result[second_batting][4] += int(ov2//1)
        temp_result[second_batting][8] += int((ov2*10) % 10)
        temp_result[first_batting][0] += 1
        temp_result[second_batting][0] += 1
        if score1 > score2:
            temp_result[first_batting][7] += 2
        elif score2 > score1:
            temp_result[second_batting][7] += 2
        # temp_result[win][7]+=2
        try:
            for i in temp_result:
                temp_result[i][10] = (temp_result[i][3]/(temp_result[i][4]+(temp_result[i][8]/6)))-(
                    temp_result[i][5]/(temp_result[i][6]+(temp_result[i][9]/6)))
        except ZeroDivisionError:
            return [], []
        
    if flag==1 and score1==score2:
        temp_result[win][7]+=2


    sorted_d = dict(sorted(temp_result.items(),
                    key=lambda item: (-item[1][7], -item[1][10])))
    print("\n")
    for i in sorted_d:
        print(i, "    ", sorted_d[i])
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





#code given below is used for testing the functions.





# output_here = get_table()
# for i in range(len(output_here[0])):
#     print(output_here[0][i], "\t\t", output_here[1][i], "\t", output_here[2][i], "\t",
#           output_here[3][i], "\t", output_here[4][i], "\t", output_here[5][i], "\t")

# print("\n")
# output1, output2 = get_ptable("2024-05-18")
# output3 = get_rem("2024-05-18")
# for i in range(len(output1[0])):
#     print(output1[0][i], "\t\t", output1[1][i], "\t", output1[2][i],
#           "\t", output1[3][i], "\t", output1[4][i], "\t", output1[5][i], "\t")
# print("\n")
# for i in output2:
#         print(i, "    ", output2[i])

# print("\n-----------------\n")
# print(output2)
# print("\n")
# print(output3)
# print("\n")
# score1=int(input("Enter score1 for : "))
# score2=int(input("Enter score2 for : "))
# ov2=float(input("Enter ov2 : "))
# output4,output5=nextmatch_update("Royal Challengers Bengaluru",0,output2,output3[1][0],output3[3][0],score1,score2,ov2)
# print("\n")
# for i in range(len(output4[0])):
#     print(output4[0][i], "\t\t", output4[1][i], "\t", output4[2][i],
#           "\t", output4[3][i], "\t", output4[4][i], "\t", output4[5][i], "\t")
# print("\n")
# for i in output5:
#         print(i, "    ", output5[i])
