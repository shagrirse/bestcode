import csv

with open('example.csv', 'w', newline='') as ff:
    writer=csv.writer(ff)
    w=['id', 'new_number']
    writer.writerow(w)
    for i in range (101):
        data = [[i, i+2]]
        writer.writerows(data)
