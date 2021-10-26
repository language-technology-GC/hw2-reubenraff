#!/usr/bin/env python
import csv


with open("predictions.txt","r") as source:
    csv_reader = csv.reader(source, delimiter='\t')
    #for tag,number,phone in csv_reader:
    h_list = []
    t_list = []
    for line in csv_reader:
        tag = line[0]
        if "S-" in tag:
            #print("".join(line[-1].rstrip()))
            h_list.append("".join(line[-1]) + "\t")
        if "T-" in tag:
            #print(line)
            t_list.append("".join(line[-1]))

stuff = zip(tuple(h_list),tuple(t_list))
#print(stuff)
with open("column_phones.tok","w+") as dump:
    writer = csv.writer(dump,delimiter="\t")
    writer.writerows(stuff)
