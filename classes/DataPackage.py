class DataPackage:
    """
    Class which represents data package acquired from an API call. It may be
    a forecast or historichal data

    Attributes:
        - raw_data: raw data created from JSON
        - clean_dict: contains only needed data from the raw_dict
        - API_name: name of the API from which data was acquired
        - ?Station
    """

    def __init__(self, raw_data, station_name, api_name):
        self.raw_data = raw_data
        self.station_name = station_name
        self.api_name = api_name


class Forecast(DataPackage):
    """
    Class to handle daily or hourly weather forecasts
    """

    def __init__(self, raw_data, station_name, api_name):
        super().__init__(raw_data, station_name, api_name)


class History(DataPackage):
    """
    Class to handle daily or hourly weather history
    """

    def __init__(self, raw_data, station_name, api_name):
        super().__init__(raw_data, station_name, api_name)
