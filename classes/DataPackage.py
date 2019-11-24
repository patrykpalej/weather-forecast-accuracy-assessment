from datetime import datetime
from dateutil import parser


class DataPackage:
    """
    Class which represents data package acquired from an API call. It may be
    a forecast or historichal data

    Attributes:
        - raw_data: raw data created from JSON
        - station_name:
        - API_name: name of the API from which data was acquired
        - ts_datetime: timestamp in datetime() format
        - ts_unix: unix timestamp
        - ts_str: timestamp in string format
    """

    def __init__(self, raw_data, station_name, api_name):
        self.raw_data = raw_data
        self.station_name = station_name
        self.api_name = api_name

        self.ts_datetime, self.ts_unix, self.ts_str = self.convert_timestamps()
        self.temperature = self.get_forecasted_values()

    def convert_timestamps(self):
        """
        Gets timestamps from raw data and transforms it into three different
        timestamps: datetime object, unix timestamp and string timestamp
        """

        original_timestamps = [elem["time"] for elem in self.raw_data]

        if type(original_timestamps[0]) == int:
            datetime_timestamps = [datetime.fromtimestamp(elem)
                                   for elem in original_timestamps]
            unix_timestamps = original_timestamps
            string_timestamps \
                = [datetime.fromtimestamp(elem).strftime("%Y-%m-%d %H:%M:%S")
                   for elem in original_timestamps]

        else:
            datetime_timestamps = [parser.parse(elem)
                                   for elem in original_timestamps]
            unix_timestamps \
                = [round(datetime.strptime(elem, "%Y-%m-%d %H:%M:%S")
                         .timestamp())
                   for elem in original_timestamps]
            string_timestamps = original_timestamps

        return datetime_timestamps, unix_timestamps, string_timestamps

    def get_forecasted_values(self):
        temperature = self.raw_data["temperature"]

        return temperature


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
