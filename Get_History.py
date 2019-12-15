"""
Calls API to obtain the history and exports the results to a proper
output form
"""

from classes.WebAPI import WebAPIMeteostat
from functions.get_forecast_period import get_forecast_period

import os


meteostat_api = WebAPIMeteostat()

path_to_data = os.getcwd() + "/data/"
history_start_date, history_end_date = get_forecast_period(path_to_data,
                                                           "London")

cities = ["Warsaw", "Rome", "London", "Moscow", "New York", "Novosibirsk"]

for city in cities:
    history = meteostat_api.get_hourly_data(city, history_start_date,
                                            history_end_date, "history",
                                            cut_off=False)

    history.dump_history()
