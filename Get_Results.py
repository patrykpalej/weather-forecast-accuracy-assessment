"""
Takes files with collations and creates plots based on them
"""
import os
import pandas as pd

from functions.createPlots import forecast_vs_actual_separate, \
    forecast_vs_actual_averaged, r2_vs_time_separate, r2_vs_time_averaged, \
    r2_vs_location, r2_vs_location_and_time


locations = os.listdir(os.getcwd() + "/data/collations/")
collations_dict = dict((loc, 0) for loc in locations)

file_name = "no_file_name"
for location in locations:
    collation_dir = os.getcwd() + "/data/collations/" + location + "/"
    file_name = os.listdir(collation_dir)[0]
    collation_path = collation_dir + file_name

    collation_df = pd.read_csv(collation_path, sep='\t')
    collations_dict[location] = collation_df


forecast_vs_actual_separate(collations_dict, file_name[:-4])
forecast_vs_actual_averaged(collations_dict, file_name[:-4])
r2_vs_time_separate(collations_dict, file_name[:-4])
r2_vs_time_averaged(collations_dict, file_name[:-4])
r2_vs_location(collations_dict, file_name[:-4])
r2_vs_location_and_time(collations_dict, file_name[:-4])
