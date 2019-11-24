class DataPackage:
    """
    Class which represents data package acquired from an API call. It may be
    a forecast or historichal data

    Attributes:
        - raw_dict: raw dictionary created from JSON
        - clean_dict: contains only needed data from the raw_dict
        - API_name: name of the API from which data was acquired
        - ?Station
    """

    def __init__(self, raw_dict, station_name, api_name):
        self.station_name = station_name
        self.api_name = api_name
        self.raw_dict = raw_dict



