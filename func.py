import operator


def majority_vote(*args):
    list1 = list(*args)
    lenl = len(list1)
    set1 = set(list1)
    list2 = list(set1)
    lens = len(set1)
    listv = []
    dict1 = {}

    if lenl == 0: return None

    for i in range(0, lens):
        k = list2[i]

        y = 0
        for j in range(0, lenl):

            if k == list1[j]:
                y += 1

        listv.append(y)

    dict1 = dict(zip(list2, listv))


    for m in range(len(listv)):
        if listv[m] > lenl / 2:

            return print(max(dict1.items(), key=operator.itemgetter(1))[0])
        else:
            return None


majority_vote(["A", "A", "A", "B", "C", "A", "C"])


import csv

def read_csv_2(f = '../Resources/data1.csv'):

    with open(f, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] != None and row[3] != None and row[2].isalnum() and row[3].isalnum():

                try:
                    if int(row[3]) > 2000:
                        print(row[2], row[3])
                except ValueError:
                    return print(row[2], row[3])
    f.close()

read_csv_2()