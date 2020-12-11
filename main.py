from __future__ import print_function
import sys
from pyspark import SparkContext
import csv
from csv import reader
import io
import re

from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *



def d_check(x):
    # return 1 for any value that does not generate a parsing error
    try:
        d = parse(x)
        return 1
    except ValueError:
        return 0
    except OverflowError:
        return 0

def list_check(x):
    # call d_check for every cell in the current row
    for i in range(len(x)):
        x[i] = d_check(x[i])
    return x

def col_sums(x, y):
    # sum the individual columns
    # an extra column of 1's is included at the end to track the overall count
    for i in range(len(y)-1):
        y[i] += x[i]
    y[-1] += 1
    return y


if __name__ == "__main__":
    sc = SparkContext()
    inFile = sys.argv[1]
    # name the output file to match the input file
    outFile = inFile[-13:-3] + "out"
    tf = sc.textFile(inFile, 1)
    tf = tf.mapPartitions(lambda x: reader(x))
    header = tf.first()
    cols = len(header)

    tf = tf.filter(lambda x: x != header)

    # process each row
    tf = tf.map(list_check)
    # add an additional column that will fold 1's to track the overall count
    totals = [0] * (cols + 1)
    # sum the columns via fold
    res = tf.fold(totals, col_sums)
    # last value is the count
    cnt = float(res[-1] - 1)
    results = []
    for i in range(cols):
        # include column in results if >98% of the values parse successfully
        if res[i] / cnt > .98:
            results.append(header[i])
    sc.parallelize([results]).coalesce(1).saveAsTextFile(outFile)

    sc.stop()
