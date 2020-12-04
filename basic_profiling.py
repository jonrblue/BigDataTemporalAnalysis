import datamart_profiler
import pandas
import json

df_data = pandas.read_csv('/mnt/c/Users/njuli/Desktop/MS/Motor_Vehicle_Collisions_-_Vehicles.csv')
prof = datamart_profiler.process_dataset(df_data)

# possible extra processing here

with open('basic_profiling.txt','w') as file:
    file.write(json.dumps(prof))

