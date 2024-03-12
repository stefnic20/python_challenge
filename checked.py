import os
import csv

total = 0
candidate_list = []
v_pct = []
v_ct = []

find_path = ("Desktop/GitHub/python_challenge/PyPoll/Resources/election_data.csv")
with open(find_path, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(reader, None)

    for row in reader:
        total += 1

    if row[2] not in candidate_list:
        candidate_list.append(row[2])
        index = candidate_list.index(row[2])
        v_ct.append(1)

    else:
        index = candidate_list.index(row[2])
        v_ct[index] +=1

    for votes in v_ct:
        percentage = (votes/v_ct) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        v_pct.append(percentage)

    winner = max(v_ct)
    index = v_ct.index(winner)
    winning_candidate = candidate_list[index]

    print("Election Results")
    print("_________________________________________________")
    print(f"Total Votes: {str(total)}")
    print("_________________________________________________")
    for i in range(len(candidate_list)):
    print(f"{candidate_list[i]}: {str(v_pct[i])} ({str(v_ct[i])})")
    print("__________________________")
    print(f"Winner: {winning_candidate}")
    print("______________________________")