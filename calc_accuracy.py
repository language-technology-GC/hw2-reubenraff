#!/usr/bin/env python
import csv
import logging


def calc_accuracy():
    count = 0
    print("count: ", count)
    with open("column_phones.tok", "r") as source:
        csv_reader = csv.reader(source, delimiter="\t")
        for phone1, phone2 in csv_reader:
            if phone1 == phone2:
                count += 1
            wer = ((len(phone1List) - count) / len(phone1List)) * 100 #17.0
    return wer
print(calc_accuracy())
