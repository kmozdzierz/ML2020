#!/usr/bin/python
# -*- coding: utf-8 -*-

### Machine Learning 2022
### Lab. 7 - SVM
### Imię i nazwisko: Kacper Mozdzierz
### Nr albumu: 401733
### Data: 26.04.2022

### Grupa: wtorek 9:30 - 11:00


import csv

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # DONE: Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}



    try:
        with open(file='data/vocab.txt', mode= 'r') as vocabFile:
            lines = vocabFile.readlines()
        
        vocabDict = {}

        for line in lines:           
            line_split = line.split('\t')
            vocabDict[int(line_split[0])] = line_split[1][:-1]
        return vocabDict
            
    except FileNotFoundError:
        print("File not found")
        return 0
