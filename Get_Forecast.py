"""
Calls API to obtain the forecast and exports the results to a proper
output form
"""

from classes.WebAPI import WebAPI

webapi = WebAPI("darksky")

print(webapi.config)
print(webapi.name)
