# Weather Forecasting Accuracy Assessment

The objective of this project is to download and analyze weather data in order to find a relationship between the forecast time range and its accuracy. Data is acquired via Meteostat API.



## Repository content

### Folders 

| Name       | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| classes/   | folder which contains all used classes                       |
| config/    | folder with configuration files (e.g. for APIs). For APIs config files name of the file is "config__api-name_" |
| data/      | folder with forecasts, historical data and collations of them |
| functions/ | folder with functions which can be used from the pipeline    |
| results/   | visualization of the relationship between forecasts and actual weather |



### Files 

| Name             | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| Get_Forecast.py  | script for acquiring forecast data from API                  |
| Get_Results.py   | script for preparing collations and plotting them            |
| getHistory.py    | file containing get_history() function which is called in order to acquire historical weather data from API |
| makeCollation.py | file containing make_collation() function for acquiring collations of forecasts and historical data for the further analysis |



## Sample results



<img src="results/2020-01-10 ~ 2020-02-20/forecast_vs_actual_averaged.png" alt="forecast_vs_actual" style="zoom:50%;" />



<img src="results/2020-01-10 ~ 2020-02-20/corr_vs_time_separate.png" alt="correlation_vs_time" style="zoom:50%;" />



<img src="results/2020-01-10 ~ 2020-02-20/corr_vs_location_and_time.png" alt="correlation_vs_time_and_location" style="zoom:50%;" />