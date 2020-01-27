import os
import re
import numpy as np
import pandas as pd
import codecs
import io
import textwrap
import itertools
import csv


def Getrawformat():
    for each in os.listdir('data/'):
        parent = []
        print('file:' + each)
        fwrite = open('analysis/' + each , 'w' , encoding = 'utf-8')
        with open('data/' + each , encoding = 'utf-8') as fread:
            for line in fread:
                for l in line.split('\t\t'):
                    subline = l.split('\t\t')
                    for sub in subline:
                        print(sub.strip())
                        fwrite.write(sub.strip() + '\n')
        fwrite.close()


def Getrefined():
    import csv
    for each in os.listdir('analysis/'):
        with open('analysis/' + each , 'r' , encoding = 'utf-8') as f:
            reader = csv.reader(f , delimiter = '\t' , quoting = csv.QUOTE_NONE)
            # reader = csv.reader(f , dialect = 'excel' , delimiter = '\t')
            for row in reader:
                print(row)


def checktail(tail):
    tail = list(itertools.chain(*tail))


def checkheader(row):
    pass


def readerTesting():
    header = False

    tail = []
    rwrite = []

    fwrite = open('temp/TestWrite.txt' , 'w' , encoding = 'utf-8')
    with open('temp/testing.txt' , 'r' , encoding = 'utf-8') as f:
        reader = csv.reader(f , delimiter = '\t' , quoting = csv.QUOTE_NONE)
        for i , row in enumerate(reader):
            if str(row[0]).startswith('+92') or \
                    str(row[0]).startswith('03') or \
                    str(row[0]).startswith('8001') or \
                    str(row[0]).startswith('Ufone') or \
                    str(row[0]).startswith('UPaisa') or \
                    str(row[0]).startswith('Internet') or \
                    str(row[0]).startswith('HEC') or \
                    str(row[0]).startswith('UFONE') :

                header = True
                if header:
                    if len(row) == 4 and not tail:
                        print(row)
                        fwrite.write(str(row))
                        fwrite.write('\n')
                        continue
                    if len(row) == 4 and tail:
                        print(list(itertools.chain(*tail)))
                        fwrite.write(str(list(itertools.chain(*tail))))
                        fwrite.write('\n')
                        tail = []
                        print(row)
                        fwrite.write(str(row))
                        fwrite.write('\n')
                        continue
                    if len(row) < 4 and tail:
                        print(list(itertools.chain(*tail)))
                        fwrite.write(str(list(itertools.chain(*tail))))
                        fwrite.write('\n')
                        fwrite.write('\n')
                        tail = []
                        tail.append(row)
                        continue
                    if len(row) < 4:
                        if tail:
                            print(list(itertools.chain(*tail)))
                            fwrite.write(str(list(itertools.chain(*tail))))
                            fwrite.write('\n')
                            print(row)
                            fwrite(str(row))
                            fwrite.write('\n')
                            continue
                        else:
                            tail.append(row)
                else:
                    tail.append(row)
                    header = True
                    continue
            else:
                tail.append(row)
                continue
            header = False
    fwrite.close()

if __name__ == '__main__':
    # Getrawformat()
    # Getrefined()
    readerTesting()
