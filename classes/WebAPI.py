import os
import json
import requests

from .DataPackage import Forecast, History


class WebAPI:
    """
    Class of all possible web APIs (e.g. Meteostat)

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


class WebAPIMeteostat(WebAPI):
    """
    Class to handle specifically Meteostat API (for historichal and future
    data)
    """

    def __init__(self):
        self.name = "meteostat"
        super().__init__(self.name)

    def get_hourly_data(self, station_name, start_timestamp, end_timestamp,
                        data_type, cut_off):
        """
        Gets hourly weather history for a given station and time range
        from Meteostat API

        :param station_name:
        :param start_timestamp: "yyyy-mm-dd" format
        :param end_timestamp: "yyyy-mm-dd" format
        :param data_type: history or forecast
        :param cut_off: number of hours in data package. If no then =False

        :return: list of dicts with history for subsequent timestamps in range
        """

        api_call_link_formatted = self.api_call \
            .format(self.stations[station_name]["id"], start_timestamp,
                    end_timestamp, self.key)

        full_web_data = requests.get(api_call_link_formatted).json()
        weather_data = full_web_data["data"]

        temperature_history \
            = [{k: timestamp[k] for k in ["time", "temperature"]}
               for timestamp in weather_data]
        if cut_off:
            temperature_history = temperature_history[:cut_off]

        if data_type == "forecast":
            return Forecast(temperature_history, station_name, self.name)
        elif data_type == "history":
            return History(temperature_history, station_name, self.name)
        else:
            raise ValueError("Data type invalid. Use 'forecast' or 'history'")
