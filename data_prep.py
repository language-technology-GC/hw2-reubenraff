#!/usr/bin/env python
import csv


def main():
    with open("ice_train.tsv","r") as train, open("prepped_data/train.ice.g","w+") as sink:
        csv_reader = csv.reader(train,delimiter="\t")
        for grapheme,phoneme in csv_reader:
            print(" ".join(grapheme), file=sink)

            
    with open("ice_train.tsv","r") as train, open("prepped_data/train.ice.p","w+") as sink:
        csv_reader = csv.reader(train,delimiter="\t")
        for grapheme,phoneme in csv_reader:
            print(" ".join(grapheme), file=sink)

      
    with open("ice_dev.tsv","r") as dev, open("prepped_data/dev.ice.p","w+") as sink:
        csv_reader = csv.reader(dev,delimiter="\t")
        for grapheme,phoneme in csv_reader:
            print(" ".join(phoneme), file=sink)


    with open("ice_test.tsv","r") as test, open("prepped_data/test.ice.p","w+") as sink:
        csv_reader = csv.reader(test,delimiter="\t")
        for grapheme,phoneme in csv_reader:
            print(" ".join(phoneme), file=sink)
main()
