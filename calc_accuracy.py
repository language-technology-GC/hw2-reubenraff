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
            phone1_list = sorted("".join(phone1))
            phone1_list.remove("\t")
            phone2_list = sorted("".join(phone2))  # this is probs redundant
            if phone1_list == phone2_list:
                count += 1
            wer = ((len(phone1List) - count) / len(phone1List)) * 100
    return wer #17
calc_accuracy()
