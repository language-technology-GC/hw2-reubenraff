#!/usr/bin/env python

import argparse
import csv
import os



def main():

    path = "prepped_data/"

    # Join various path components
    print(os.path.join(path, "train.ice.g")) #do this for every file

    transformer_path = "transformer/prepped_data"

    #os.mkdir("prepped_data")
    with open(os.path.join(path, "train.ice.g"),"r") as train, open(os.path.join(transformer_path, "train.ice.g"),"w") as sink:
        csv_reader = csv.reader(train,delimiter="\t")
        for grapheme,phoneme in csv_reader:
            print(" ".join(grapheme), file=sink)
"""
    with open("ice_train.tsv","r") as train, open("prepped_data/train.ice.p" ,"w") as sink:
        csv_reader = csv.reader(train,delimiter="\t")
        for grapheme,phoneme in csv_reader:
            print(" ".join(grapheme), file=sink)

    with open("ice_dev.tsv","r") as dev, open("prepped_data/dev.ice.p","w") as sink:
        csv_reader = csv.reader(dev,delimiter="\t")
        for grapheme,phoneme in csv_reader:
            print(" ".join(phoneme), file=sink)


    with open("ice_test.tsv","r") as test, open(os.path.join("prepped_data/test.ice.p"),"w+") as sink:
        csv_reader = csv.reader(test,delimiter="\t")
        for grapheme,phoneme in csv_reader:
            print(" ".join(phoneme), file=sink)
"""
main()
