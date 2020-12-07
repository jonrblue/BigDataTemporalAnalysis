from __future__ import print_function
import sys
from pyspark import SparkContext
import csv
from csv import reader
import io

from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *



def d_check(x):
    try:
        d = parse(x)
        return 1
    except ValueError:
        return 0
    except OverflowError:
        return 0

def list_check(x):
    for i in range(len(x)):
        x[i] = d_check(x[i])
    return x

def col_sums(x, y):
    for i in range(len(y)-1):
        y[i] += x[i]
    y[-1] += 1
    return y


if __name__ == "__main__":
    sc = SparkContext()
    inFile = sys.argv[1]
    outFile = inFile[-13:-3] + "out"
    tf = sc.textFile(inFile, 1)
    tf = tf.mapPartitions(lambda x: reader(x))
    header = tf.first()
    cols = len(header)
    trips = tf.filter(lambda x: x != header)

    tf = tf.map(list_check)
    totals = [0] * (cols + 1)
    res = tf.fold(totals, col_sums)
    cnt = float(res[-1] - 1)
    results = []
    for i in range(cols):
        if res[i] / cnt > .98:
            results.append(header[i])
    sc.parallelize([results]).coalesce(1).saveAsTextFile(outFile)

    sc.stop()
