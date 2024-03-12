import os
import csv

find_path = ("Desktop/GitHub/python_challenge/PyBank/Resources/budget_data.csv")

with open(find_path, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile, None)

    tot_mon = 0
    tot = 0
    pl = 0
    dt = 0
    chg_pl = 0
    pl_chg = []
    mon = []

    for row in reader:
        tot_mon += 1
        dt = int(row[1])
        tot += dt

        if (tot_mon == 1):
            pl = dt

            else:
                chg_pl = dt - pl
                mon.append(row[0])
                pl_chg.append(chg_pl)
                pl = dt
            
sum = sum(pl_chg)
average = round(sum/(tot_mon - 1), 2)

grt_inc = max(pl_chg)
grt_dec = min(pl_chg)

hgst_date = pl_chg.index(grt_inc)
lwst_date = pl_chg.index(grt_dec)

bst_mon = mon[hgst_date]
wst_mon = mon[lwst_date]

print(f"budget_analysis")
print(f"________________________")
print(f"tot_mon: {tot_mon}")
print(f"total: ${tot}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {bst_mon} (${grt_inc})")
print(f"Greatest Decrease in Profits: {wst_mon} (${grt_dec})")

bank_file = ("Desktop/GitHub/python_challenge/PyBank/Resources/budget_data.txt")
with open (bank_file, "w") as outfile:
    outfile.write("budget_analysis\n")
    outfile.write("__________________________\n")
    outfile.write(f"Total Months: {tot_mon}\n")
    outfile.write(f"Total: ${tot}\n")
    outfile.write(f"Average Change: ${average_pl}\n")
    outfile.write(f"Greatest Increase in Profits: {bst_mon} (${grt_inc})n")
    outfile.write(f"Greatest Decrease in Losses: {wst_mon} (${grt_dec})\n")