import csv
from models import company

def get_data_set ():
    data_set = []
    i = 0
    with open('data/dataset.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if i != 0:
                data_set.append(
                    company.Company(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                        row[13],
                        row[14],
                        row[15],
                        row[16],
                        row[17],
                        row[18],
                        row[19],
                        row[20],
                        row[21],
                        row[22],
                        row[23],
                        row[24],
                        row[25],
                        row[26],
                        row[27],
                        row[28],
                        row[29],
                        row[30],
                        row[31],
                        row[32],
                        row[32],
                        row[33],
                    )
                )
            else:
                i = 1
    return data_set

#list = get_data_set()
#for i in list:
#    print(i.domain)
