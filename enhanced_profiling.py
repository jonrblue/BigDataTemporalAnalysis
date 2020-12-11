import datamart_profiler
import pandas
import json
import sys
import io
import re
import time


def is_time(data):
    time_re = re.compile("24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]|[0-9]:[0-5][0-9]")
    time_am = re.compile("12:00AM|[0-1][0-9]:[0-5][0-9]AM|[0-9]:[0-5][0-9]AM")
    time_a = re.compile("12:00A|[0-1][0-9]:[0-5][0-9]A|[0-9]:[0-5][0-9]A")
    time_pm = re.compile("12:00PM|[0-1][0-9]:[0-5][0-9]PM|[0-9]:[0-5][0-9]PM")
    time_p = re.compile("12:00P|[0-1][0-9]:[0-5][0-9]P|[0-9]:[0-5][0-9]P")
    if time_re.match(data):
        return True
    if time_am.match(data):
        return True
    if time_a.match(data):
        return True
    if time_pm.match(data):
        return True
    if time_p.match(data):
        return True
    return False


def is_year(data):
    try:
        time.strptime(data,'%Y')
        return True
    except ValueError:
        return False


def is_month(data):
    try:
        time.strptime(data,'%m')
        return True
    except ValueError:
        return False


def is_timestamp(data):
    try:
        time.strptime(data,'%H:%M:%S')
        return True
    except ValueError:
        return False

def is_datetime_1(data):
    try:
        time.strptime(data,'%m%d%Y')
        return True
    except ValueError:
        return False

def is_datetime_2(data):
    try:
        time.strptime(data,'%Y%m%d')
        return True
    except ValueError:
        return False


if len(sys.argv) != 2:
    print("Invalid numebr of arguments")
    exit(-1)
data_file = sys.argv[1]
temporal_columns = []
df_data = pandas.read_csv(data_file)

threshold = 0.98
for col in list(df_data):
    column_data = df_data[col].values
    temporal = 0
    for i in range(column_data.size):
        cell = str(column_data[i])
        if is_time(cell) or is_year(cell) or is_month(cell) or is_timestamp(cell) or is_datetime_1(cell) or is_datetime_2(cell):
            temporal += 1
    if temporal/column_data.size >= threshold:
        temporal_columns.append(col)

prof = datamart_profiler.process_dataset(df_data)
for i in range(len(prof["columns"])):
    if "temporal_resolution" in prof["columns"][i].keys():
        temporal_columns.append(prof["columns"][i]["name"])
with open(data_file[-13:-3] + "out",'w') as file:
    file.write("Number of columns:  %d\n" % (prof["nb_columns"]))
    file.write("Number of temporal columns: %d\n" % (len(temporal_columns)))
    for i in range(len(temporal_columns)):
        file.write(temporal_columns[i] + '\n')

