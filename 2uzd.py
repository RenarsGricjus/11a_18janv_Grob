import csv

otra_rinda = []

with open("2uzd.csv", "r", encoding="utf8") as readit:
    haha = csv.reader(readit)

    for rinda in haha:
        if len(rinda) >= 2: 
            otra_rinda.append(rinda[1])
            print(rinda[1])
