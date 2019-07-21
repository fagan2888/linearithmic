import csv

with open('states.csv') as f:
    data = list(csv.reader(f))

print(data[2][4])
