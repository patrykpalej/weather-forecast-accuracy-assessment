import os
import json


class WebAPI:
    """
    Class of all possible web APIs such as DarkSky or Meteostat.

    Attributes:
        - config: dictionary with configuration data for the specific API
        - name: name of the API
    """

    def __init__(self, api_name):
        self.name = api_name

        path_to_file = os.getcwd() + "/config/config_{}.json".format(api_name)
        with open(path_to_file) as handle:
            self.config = json.loads(handle.read())

        # TODO parse config and add new attributes of the class (change docstr)

    def call_api(self):
        """
        :return: output from an API call
        """
        pass
