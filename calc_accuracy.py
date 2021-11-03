#!/usr/bin/env python
import csv
import logging


def calc_accuracy():

    count = 0
    with open("column_phones.tok", "r") as source:
        csv_reader = csv.reader(source, delimiter="\t")
        phone1List = []
        for phone1, phone2 in csv_reader:
            phone1List.append(phone1)
            phone1_list = list("".join(phone1))
            phone1_list.remove("\t")
            phone1 = "".join(phone1_list)
            if phone1  == phone2:
                print(phone1,phone2)
                count += 1
            wer = ((len(phone1List) - count) / len(phone1List)) * 100
    return wer
print(calc_accuracy())

# 17.0
