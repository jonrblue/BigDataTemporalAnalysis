import csv
import io
import sys

inFile = sys.argv[1]
outFile = "top100/" + inFile[-13:]

with open(outFile, 'wb') as f_out:
    with open(inFile, encoding='utf-8') as f:
        for line in f:
            f_out.write(line.encode("ascii", "ignore"))
