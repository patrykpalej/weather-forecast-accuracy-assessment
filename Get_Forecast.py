"""
Calls API to obtain the forecast and exports the results to a proper
output form
"""
from datetime import datetime, timedelta

from classes.WebAPI import WebAPIMeteostat


meteostat_api = WebAPIMeteostat()

n_of_days = 10
forecast_start_date = datetime.now().strftime("%Y-%m-%d")
forecast_end_date = (datetime.now() + timedelta(days=n_of_days))\
    .strftime("%Y-%m-%d")

cities = ["Warsaw", "Rome", "London", "Moscow", "New York", "Novosibirsk"]

for city in cities:
    forecast = meteostat_api.get_hourly_data(city, forecast_start_date,
                                             forecast_end_date, "forecast",
                                             cut_off=n_of_days*24 - 5)

    forecast.dump_forecast()
