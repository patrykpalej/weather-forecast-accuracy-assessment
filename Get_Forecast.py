"""
Calls API to obtain the forecast and exports the results to a proper
output form
"""

from classes.WebAPI import WebAPIMeteostat
from datetime import datetime, timedelta


meteostat_api = WebAPIMeteostat()

forecast_start_date = datetime.now().strftime("%Y-%m-%d")
forecast_end_date = (datetime.now() + timedelta(days=5))\
    .strftime("%Y-%m-%d")

forecast = meteostat_api.get_hourly_data("Warsaw", forecast_start_date,
                                         forecast_end_date, "forecast")
forecast.dump_forecast()
