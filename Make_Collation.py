"""
Gets a history for a given location via get_history() and prepairs a
collation of historichal data and the forecast
"""
import os
import json
import pandas as pd

from getHistory import get_history
from functions.get_forecast_period import get_forecast_limits
from functions.collation_utils import clean_subfolders, get_history_subset, \
    shorten_forecast_dict, collate_dicts


clean_subfolders(os.getcwd() + "/data/history/")
clean_subfolders(os.getcwd() + "/data/collations/")

locations = os.listdir(os.getcwd() + "/data/forecasts")

for location in locations:
    get_history(location)


for location in locations:
    forecast_dir = os.getcwd() + "/data/forecasts/" + location
    forecast_jsons = [forecast_dir + "/" + file_name
                      for file_name in os.listdir(forecast_dir)]

    collation_dfs = []
    for file in forecast_jsons:
        with open(file) as f:
            forecast_dict = json.loads(f.read())

        start_timestamp, end_timestamp = get_forecast_limits(forecast_dict)

        history_dir = os.getcwd() + "/data/history/" + location
        history_path = history_dir + "/" + os.listdir(history_dir)[0]
        history_dict = get_history_subset(history_path, start_timestamp,
                                          end_timestamp)

        if len(forecast_dict["timestamp"]) > len(history_dict["timestamp"]):
            forecast_dict = shorten_forecast_dict(forecast_dict, history_dict)

        collation_dfs.append(collate_dicts(forecast_dict, history_dict))

    overall_collation_df = pd.concat(collation_dfs, ignore_index=True)
    collation_file_name = os.listdir(history_dir)[0]
    overall_collation_df.to_csv(os.getcwd() + "/data/collations/" + location
                                + "/" + collation_file_name[:-5] + ".csv",
                                sep='\t')
