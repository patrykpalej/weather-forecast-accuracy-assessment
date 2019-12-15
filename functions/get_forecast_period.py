import os
import json
from datetime import datetime


def get_forecast_start_date(path_to_data, city_name):
    """
    Gets first timestamp from forecasts for a given city
    """
    directory_to_search = path_to_data + "/forecasts/" + city_name

    json_files = [directory_to_search + "/" + file_name
                  for file_name in list(os.walk(directory_to_search))[0][2]]

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