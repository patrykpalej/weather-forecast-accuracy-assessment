import os
import json
import requests

from .DataPackage import Forecast, History


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
    Class to handle specifically Darksky API (for forecast)
    """

    def __init__(self):
        self.name = "darksky"
        super().__init__(self.name)

    def get_hourly_forecast(self, station_name):
        """
        Gets hourly forecast for a given station from Darksky API

        :param station_name:

        :return: list of dicts with forecast for subsequent timestamps in range
        """

        api_call_link_formatted = self.api_call \
            .format(self.key, self.stations[station_name]["lat"],
                    self.stations[station_name]["lon"])

        full_web_data = requests.get(api_call_link_formatted).json()
        full_forecast = full_web_data["hourly"]["data"]

        temperature_forecast \
            = [{k: timestamp[k] for k in ["time", "temperature"]}
               for timestamp in full_forecast]

        return Forecast(temperature_forecast, station_name, self.name)


class WebAPIMeteostat(WebAPI):
    """
    Class to handle specifically Meteostat API (for historichal data)
    """

    def __init__(self):
        self.name = "meteostat"
        super().__init__(self.name)

    def get_hourly_history(self, station_name, start_timestamp, end_timestamp):
        """
        Gets hourly weather history for a given station and time range
        from Meteostat API

        :param station_name:
        :param start_timestamp: "yyyy-mm-dd" format
        :param end_timestamp: "yyyy-mm-dd" format

        :return: list of dicts with history for subsequent timestamps in range
        """

        api_call_link_formatted = self.api_call \
            .format(self.stations[station_name]["id"], start_timestamp,
                    end_timestamp, self.key)

        full_web_data = requests.get(api_call_link_formatted).json()
        full_history = full_web_data["data"]

        temperature_history \
            = [{k: timestamp[k] for k in ["time", "temperature"]}
               for timestamp in full_history]

        return History(temperature_history, station_name, self.name)
