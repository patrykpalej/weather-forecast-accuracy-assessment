"""
Calls API to obtain the forecast and exports the results to a proper
output form
"""

from classes.WebAPI import WebAPIMeteostat


meteostat_api = WebAPIMeteostat()
forecast = meteostat_api.get_hourly_data("Warsaw", "2019-11-25",
                                         "2019-11-30", "forecast")

# print(forecast)
# print(history.ts_str)
forecast.dump_forecast()
