"""
Class of all possible web APIs such as DarkSky or Meteostat.

Attributes:
    - config: dictionary with configuration data for the specific API
    - name: name of the API
"""

import os
import json


class WebAPI:
    def __init__(self, api_name):
        self.name = api_name

        path_to_file = os.getcwd() + "/config/config_{}.json".format(api_name)
        with open(path_to_file) as handle:
            self.config = json.loads(handle.read())

    def call_api(self):
        """
        :return: output from an API call
        """
        pass
