import os
import json
import requests


class WebAPI:
    """
    Class of all possible web APIs such as DarkSky or Meteostat.

    Attributes:
        - name: name of the API
        - stations: list of dictionaries for all declared weather stations
        - key: API access key
        - api_call: link for the API call (with {} for parameters)
    """

    def __init__(self, api_name):
        path_to_file = os.getcwd() + "/config/config_{}.json".format(api_name)
        with open(path_to_file) as handle:
            config = json.loads(handle.read())

        self.stations = config["stations"]
        self.key = config["key"]
        self.api_call = config["API_call"][0]


class WebAPIDarksky(WebAPI):
    """
    Class to handle specifically Darksky API
    """

    def __init__(self):
        self.name = "darksky"
        super().__init__(self.name)

    def call_api(self, station_name):
        api_call_link_formatted = self.api_call \
            .format(self.key, self.stations[station_name]["lat"],
                    self.stations[station_name]["lon"])

        full_web_data = requests.get(api_call_link_formatted).json()
        forecast = full_web_data["hourly"]["data"]

        return forecast
