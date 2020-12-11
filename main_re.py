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


if __name__ == "__main__":
    sc = SparkContext()
    inFile = sys.argv[1]
    outFile = inFile[-13:-3] + "out"
    tf = sc.textFile(inFile, 1)
    tf = tf.mapPartitions(lambda x: reader(x))
    header = tf.first()
    cols = len(header)

    words = ['date', 'time', 'hour', 'year', "dt", "tm", "month", "yr"]

    results = []
    for h in header:
        if any(i in h for i in words):
            results.append(h)

    sc.parallelize([results]).coalesce(1).saveAsTextFile(outFile)

    sc.stop()
