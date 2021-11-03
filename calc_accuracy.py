#!/usr/bin/env python
import csv
import logging

print("in ccheck accuracy file")

def calc_accuracy():
    count = 0
    print("count: ", count)
    with open("column_phones.tok", "r") as source:
        csv_reader = csv.reader(source, delimiter="\t")
        phone1List = []
        for phone1, phone2 in csv_reader:
            phone1List.append(phone1)
            if phone1 == phone2:
                count += 1
            wer = ((len(phone1List) - count) / len(phone1List)) * 100 #17.0
    return wer
print(calc_accuracy())
