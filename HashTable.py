import csv

#import csv
with open('WGUPS.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        print(row)