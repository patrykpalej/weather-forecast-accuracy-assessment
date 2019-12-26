import os
import json
import pandas as pd


def clean_subfolders(directory):
    for subfolder in os.listdir(directory):
        path = os.path.join(directory, subfolder)
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            os.remove(file_path)


def get_history_subset(history_path, start_timestamp, end_timestamp):
    """
    Takes location, start and end timestamps. Returns a dictionary which is
    a subset
    """
    with open(history_path) as f:
        full_history_dict = json.loads(f.read())

    start_index = 0
    end_index = len(full_history_dict["timestamp"])
    for i, timestamp in enumerate(full_history_dict["timestamp"]):
        if timestamp == start_timestamp:
            start_index = i
        if timestamp == end_timestamp:
            end_index = i

    history_dict = dict()
    history_dict["timestamp"] \
        = full_history_dict["timestamp"][start_index:end_index+1]
    history_dict["unix_timestamp"] \
        = full_history_dict["unix_timestamp"][start_index:end_index + 1]
    history_dict["temperature"] \
        = full_history_dict["temperature"][start_index:end_index + 1]

    return history_dict


def shorten_forecast_dict(forecast_dict, history_dict):
    """
    If forecast_dict is longer than history_dict (because forecast for
    the future (in relation to the time of analysis) is already present))
    this function adjusts forecast_dict to the length of history_dict
    """
    history_length = len(history_dict["timestamp"])

    shortened_forecast_dict = dict()
    for key in list(forecast_dict.keys()):
        shortened_forecast_dict[key] = forecast_dict[key][:history_length]

    return shortened_forecast_dict


def collate_dicts(forecast_dict, history_dict):
    """
    Takes forecast and history dictionaries. Returns a dataframe which is a
    collation of them
    """
    for key in list(forecast_dict.keys()):
        forecast_dict["forecast_"+key] = forecast_dict.pop(key)

    for key in list(history_dict.keys()):
        history_dict["history_"+key] = history_dict.pop(key)

    combined_dict = forecast_dict
    combined_dict.update(history_dict)

    collation_df = pd.DataFrame(combined_dict)

    return collation_df

