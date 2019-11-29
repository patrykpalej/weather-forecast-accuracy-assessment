from dateutil import parser
from datetime import datetime


def convert_from_str_timestamps(original_timestamps, target_format):
    """
    Converts list of timestapms from string format to datetime or unix
    """

    if target_format == "datetime":
        output_timestamps = [parser.parse(elem)
                             for elem in original_timestamps]

    elif target_format == "unix":
        output_timestamps \
            = [round(datetime.strptime(elem, "%Y-%m-%d %H:%M:%S")
                     .timestamp())
               for elem in original_timestamps]
    else:
        raise ValueError("Invalid target_format name")

    return output_timestamps


def convert_from_unix_timestamps(original_timestamps, target_format):
    """
    Converts list of timestapms from unix format to datetime or string
    """

    if target_format == "datetime":
        output_timestamps = [datetime.fromtimestamp(elem)
                             for elem in original_timestamps]
    elif target_format == "str":
        output_timestamps \
            = [datetime.fromtimestamp(elem).strftime("%Y-%m-%d %H:%M:%S")
               for elem in original_timestamps]
    else:
        raise ValueError("Invalid target_format name")

    return output_timestamps
