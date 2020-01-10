"""
Calls API to obtain the history and exports the results to a proper
output form
"""
import os
from datetime import datetime

from classes.WebAPI import WebAPIMeteostat
from functions.getForecastPeriod import get_forecast_start_date


def get_history(location):
    meteostat_api = WebAPIMeteostat()

    path_to_data = os.getcwd() + "/data/"
    history_start_date = get_forecast_start_date(path_to_data, location)
    history_end_date = "{}-{}-{}".\
        format(datetime.now().year, datetime.now().month, datetime.now().day)

    history = meteostat_api.get_hourly_data(location, history_start_date,
                                            history_end_date, "history",
                                            cut_off=False)

    history.dump_history()
