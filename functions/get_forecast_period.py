import os
import json
from datetime import datetime


def get_forecast_start_date(path_to_data, location):
    """
    Gets first timestamp from forecasts for a given location
    """
    directory_to_search = path_to_data + "/forecasts/" + location

    json_files = [directory_to_search + "/" + file_name
                  for file_name in os.listdir(directory_to_search)]

    start_dates = list()

    for file_path in json_files:
        with open(file_path, 'r') as f:
            forecast_data = json.load(f)
            start_dates.append(
                datetime.fromtimestamp(forecast_data["unix_timestamp"][0]))

    start_date = min(start_dates)
    start_date_str \
        = start_date.strftime("%Y-%m-%d")

    return start_date_str


def get_forecast_limits(forecast_dict):
    """
    Takes a dictionary with a forecast and returns first and last timestamps
    """

    return 1
