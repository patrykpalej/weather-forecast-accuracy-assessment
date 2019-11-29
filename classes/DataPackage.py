from datetime import datetime
import json
import os

from functions.convert_timestamp_format import convert_from_str_timestamps, \
    convert_from_unix_timestamps


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
        self.temperature = self.get_values_from_raw_data()

    def convert_timestamps(self):
        """
        Gets timestamps from raw data and transforms it into three different
        timestamps: datetime object, unix timestamp and string timestamp
        """

        orig_timestamps = [elem["time"] for elem in self.raw_data]

        if type(orig_timestamps[0]) == int:
            datetime_timestamps = \
                convert_from_unix_timestamps(orig_timestamps, "datetime")
            unix_timestamps = orig_timestamps
            string_timestamps = \
                convert_from_unix_timestamps(orig_timestamps, "str")
        else:
            datetime_timestamps = \
                convert_from_str_timestamps(orig_timestamps, "datetime")
            unix_timestamps = \
                convert_from_str_timestamps(orig_timestamps, "unix")
            string_timestamps = orig_timestamps

        return datetime_timestamps, unix_timestamps, string_timestamps

    def get_values_from_raw_data(self):
        temperature = [elem["temperature"] for elem in self.raw_data]

        return temperature


class Forecast(DataPackage):
    """
    Class to handle daily or hourly weather forecasts

    Attributes:
        - hours_ahead: list of hours ahead for subsequent forecasted values
    """

    def __init__(self, raw_data, station_name, api_name):
        super().__init__(raw_data, station_name, api_name)
        self.hours_ahead = self.calculate_number_of_hours_ahead()

    def calculate_number_of_hours_ahead(self):
        hours_ahead = []
        for ts in self.ts_unix:
            hours_ahead.append(round((datetime.fromtimestamp(ts)
                                      - datetime.now()).total_seconds()/3600))

        return hours_ahead

    def dump_forecast(self, file_name):
        data_dict = dict()
        data_dict["timestamp"] = self.ts_str
        data_dict["temperature"] = self.temperature
        data_dict["hours_ahead"] = self.hours_ahead

        if not os.path.exists("data/forecasts/" + self.station_name):
            os.mkdir("data/forecasts/" + self.station_name)

        with open("data/forecasts/{}/{}.json".format(self.station_name,
                                                     file_name), "w") as file:
            json.dump(data_dict, file)


class History(DataPackage):
    """
    Class to handle daily or hourly weather history
    """

    def __init__(self, raw_data, station_name, api_name):
        super().__init__(raw_data, station_name, api_name)
