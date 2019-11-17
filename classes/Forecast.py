"""
Class which represents a forecast processed from JSON data

Attributes:
    - start_timestamp: timestamp when the forecast was called
    - forecast_dict: dictionary with the following keys: "datetime",
                     "temperature", (maybe "precipitation" etc.) where the
                     values are lists with an hourly forecast per list element
"""


class Forecast:
    def __init__(self):
        pass
