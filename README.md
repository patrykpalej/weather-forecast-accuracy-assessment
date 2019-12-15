# Weather Forecasting Accuracy Assessment (WFAA)

The objective of this project is to download and analyze weather data in order to find a relationship between the forecast time range and its accuracy. Data is acquired via public APIs such as Meteostat (maybe also others). 

 

## Repository content

### Folders 

- classes/        folder which contains all used classes
- config/        folder with configuration files (e.g. for APIs). For APIs config files name of the file is "config__api-name_" 
- functions/        folder with functions which can be used from the pipeline 

### Files 

- Get_Forecast.py        main script for acquiring forecast data from API

- ...

  

## Version history

v1.1

- Get_Forecast.py script implemented
- Main classes implemented: WebAPI (+ inheriting) and DataPackage (+ inheriting)
- Configuration files prepaired

v1.2

- Darksky API excluded (only Meteostat left)
- Saving forecast data to .json files implemented
- Four cities in the pipeline: Warsaw, Rome, London and Moscow



