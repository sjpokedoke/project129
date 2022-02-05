import csv

data1list = []
data2list = []

with open("brightstars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data1list.append(row)

with open("dwarfstars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data2list.append(row)

headers1 = data1list[0]
data1 = data1list[1:]

headers2 = data2list[0]
data2 = data2list[1:]

headers = headers1+headers2
data = []

for index, datarow in enumerate(data1):
    data.append(data1[index]+data2[index])

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerow(data)