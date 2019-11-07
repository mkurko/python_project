import csv
sumaa = 0
with open("test.csv") as csv_file:
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        print(row)
        if (row[4].isdigit()):
            wiek = int(row[4])
            sumaa = sumaa + wiek

print(sumaa)