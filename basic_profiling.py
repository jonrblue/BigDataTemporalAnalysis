import datamart_profiler
import pandas
import json
import sys
import io


if len(sys.argv) != 2:
    print("Invalid numebr of arguments")
    exit(-1)
data_file = sys.argv[1]
temporal_columns = []
df_data = pandas.read_csv(data_file)
prof = datamart_profiler.process_dataset(df_data)
for i in range(len(prof["columns"])):
    if "temporal_resolution" in prof["columns"][i].keys():
        temporal_columns.append(prof["columns"][i]["name"])
with open(data_file[-13:-3] + "out",'w') as file:
    file.write("Number of columns:  %d\n" % (prof["nb_columns"]))
    file.write("Number of temporal columns: %d\n" % (len(temporal_columns)))
    for i in range(len(temporal_columns)):
        file.write(temporal_columns[i] + '\n')

