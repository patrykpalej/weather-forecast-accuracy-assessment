"""
Calls API to obtain the forecast and exports the results to a proper
output form
"""

from classes.WebAPI import WebAPIDarksky, WebAPIMeteostat

darksky_api = WebAPIDarksky()
forecast = darksky_api.get_hourly_forecast("Warsaw")


meteostat_api = WebAPIMeteostat()
history = meteostat_api.get_hourly_history("Warsaw", "2018-01-01",
                                           "2018-01-03")

# print(forecast)
# print(history)
