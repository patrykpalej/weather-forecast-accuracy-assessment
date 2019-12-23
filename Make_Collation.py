"""
Gets a history for a given location via get_history() and prepairs a
collation of historichal data and the forecast
"""
from getHistory import get_history


locations = ["Warsaw", "Rome", "London", "Moscow", "New York", "Novosibirsk"]
for location in locations:
    get_history(location)

