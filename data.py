import csv

with open("data.csv")as f:
    reader = csv.reader(f)
    # for row in reader:
    #     print(row[0])
    #     print(row[2])
    data = list(reader)[1:]

outcome = []
for each in data:
    date = each[0]
    print(date)
