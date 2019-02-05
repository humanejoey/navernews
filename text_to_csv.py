import csv

table = []
temp_table = []

for i in range(6):
    filename = "result/" + str((i+1)*10) + ".txt"
    with open(filename, 'r') as textfile:
        for line in textfile.readlines():
            temp_table.append(line.strip().decode('utf-8'))
    table.append(temp_table)
    temp_table = []

with open('result.csv', 'wb') as fout:
    writer = csv.writer(fout)
    for row in zip(*table):
        row = [s.encode('utf-8') for s in row]
        writer.writerows([row])
