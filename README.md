# Weather Forecasting Accuracy Assessment (WFAA)

The objective of this project is to download and analyze weather data in order to find a relationship between the forecast time range and its accuracy. Data is acquired via Meteostat API.



## Repository content

### Folders 

| Name       | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| classes/   | folder which contains all used classes                       |
| config/    | folder with configuration files (e.g. for APIs). For APIs config files name of the file is "config__api-name_" |
| functions/ | folder with functions which can be used from the pipeline    |



### Files 

| Name             | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| Get_Forecast.py  | main script for acquiring forecast data from API             |
| Get_Collation.py | main script for acquiring collations of forecasts and historical data for the further analysis |
| getHistory.py    | file containing get_history() function which is called in order to acquire historical weather data from API |



## Version history

v1.1

- Get_Forecast.py script implemented
- Main classes implemented: WebAPI (+ inheriting) and DataPackage (+ inheriting)
- Configuration files prepaired

v1.2

- Darksky API excluded (only Meteostat left)
- Saving forecast data to .json files implemented
- Four cities in the pipeline: Warsaw, Rome, London and Moscow

v1.3

- Acquiring historical data from Meteostat API implemented in Get_History.py script

v1.4

- Get_History transformed into a function
- Make_Collation script added for preparing collations of forecasts and historical data in .csv files

