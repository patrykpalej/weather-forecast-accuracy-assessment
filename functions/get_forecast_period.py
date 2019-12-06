import json
import os
from datetime import datetime


def get_forecast_period(path_to_data, city_name):
    """
    Gets first and last timestamp from forecasts for a given city
    """
    directory_to_search = path_to_data + "/forecasts/" + city_name

    json_files = [directory_to_search + "/" + file_name
                  for file_name in list(os.walk(directory_to_search))[0][2]]

    start_dates = list()
    end_dates = list()

    for file_path in json_files:
        with open(file_path, 'r') as f:
            forecast_data = json.load(f)
            start_dates.append(
                datetime.fromtimestamp(forecast_data["unix_timestamp"][0]))
            end_dates.append(
                datetime.fromtimestamp(forecast_data["unix_timestamp"][-1]))

    # print("start for all files: ", start_dates)
    # print("end for all files: ", end_dates)
    #
    # print("total start: ", min(start_dates))
    # print("total end: ", max(end_dates))

    start_date, end_date = min(start_dates), max(end_dates)
    start_date_str, end_date_str \
        = start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")

    return start_date_str, end_date_str
