#!/usr/bin/env python
import csv
import logging

count = 0
lengths = []
with open("column_phones.tok","r") as source:
    csv_reader = csv.reader(source, delimiter='\t')
    for phone1,phone2 in csv_reader:
        print(len(phone1), len(phone2))
        #print("".join(phone2))
        #lengths.append(len(phone2))
        for char1, char2  in zip(phone1,phone2):
            if char1 == char2:
                pass

    print(lengths)
        #any("hi" for element in s)

"""
        phone1List.append(phone1)
        #x = len(phone1)
        #first_col_len = len(next(zip(*csv_reader)))
        phone1_list = sorted("".join(phone1))

        phone1_list.remove("\t")
        phone2_list = sorted("".join(phone2)) #this is probs redundant

        #print(phone1_list == phone2_list)
        if phone1_list == phone2_list:
            print(phone1_list,phone2_list)
            count +=1
"""
#print(phone1_list)
#wer = len(phone1List) - count
#print(wer)
