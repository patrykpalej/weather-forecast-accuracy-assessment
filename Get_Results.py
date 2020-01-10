"""
Takes files with collations and creates plots based on them
"""
import os
import pandas as pd
import matplotlib.pyplot as plt 

from makeCollation import make_collation
from functions.createPlots import forecast_vs_actual_separate, \
    forecast_vs_actual_averaged, corr_vs_time_separate, \
    corr_vs_time_averaged, corr_vs_location, corr_vs_location_and_time
from functions.collationUtils import clean_subfolders


clean_subfolders(os.getcwd() + "/data/history/")
clean_subfolders(os.getcwd() + "/data/collations/")

locations = os.listdir(os.getcwd() + "/data/forecasts/")
for loc in locations:
    make_collation(loc)

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
corr_vs_time_separate(collations_dict, file_name[:-4])
corr_vs_time_averaged(collations_dict, file_name[:-4])
corr_vs_location(collations_dict, file_name[:-4])
corr_vs_location_and_time(collations_dict, file_name[:-4])

plt.close('all')
