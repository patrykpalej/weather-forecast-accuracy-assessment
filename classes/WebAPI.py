import os
import json


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
        self.name = api_name

        path_to_file = os.getcwd() + "/config/config_{}.json".format(api_name)
        with open(path_to_file) as handle:
            config = json.loads(handle.read())

        self.stations = config["stations"]
        self.key = config["key"]
        self.api_call = config["API_call"]

    def call_api(self):
        """
        :return: output from an API call
        """
        pass
