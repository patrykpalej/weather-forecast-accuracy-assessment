"""
Gets a history for a given location via get_history() and prepairs a
collation of historichal data and the forecast
"""
import os
import json

from getHistory import get_history
from functions.get_forecast_period import get_forecast_limits
from functions.collation_utils import get_history_subset, collate_dicts


locations = ["Warsaw", "Rome", "London", "Moscow", "New York", "Novosibirsk"]
for location in locations:
    get_history(location)


for location in locations:
    forecast_dir = os.getcwd() + "/data/forecasts/" + location
    json_files = [forecast_dir + "/" + file_name
                  for file_name in list(os.walk(forecast_dir))[0][2]]

    for file in json_files:
        with open(file) as f:
            forecast_dict = json.loads(f.read())

        start_timestamp, end_timestamp = get_forecast_limits(forecast_dict)

        history_dict = get_history_subset(location, start_timestamp,
                                          end_timestamp)

        collation_df = collate_dicts(forecast_dict, history_dict)

        # dump collation_df to a csv in data/collations
        # maybe whole collation for one location for the whole period in one df
