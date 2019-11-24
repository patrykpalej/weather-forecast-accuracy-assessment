"""
Calls API to obtain the forecast and exports the results to a proper
output form
"""

from classes.WebAPI import WebAPIDarksky

webapi = WebAPIDarksky()

forecast = webapi.call_api("Warsaw")

print(forecast)
