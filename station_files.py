# PART 1
# import json package
import json

# open json data file on stations
with open('precipitation.json', encoding='utf8') as file:
    station_information = json.load(file)

# ASSIGNMENT:Use this station code to select all the measurements belonging to it from the JSON data
# identify station code Seattle
Seattle_station_code = 'GHCND:US1WAKG0038'

# make an empty list of Seattle's precipitation 
Seattle_precipitation = []

# select the measurements of Seattle's station 
# (i.e. select the dictionaries within the list where the station (key) = station code (value) )
for measurement in station_information:
    # check if it is Seattle's station code
    if measurement['station'] == Seattle_station_code:
        # if so, add the data to Seattle's precipitation
        Seattle_precipitation.append(measurement)


# ASSIGNMENT: Sum all the measurement for that location for each month (i.e. create a 
# list with the total monthly precipitation).

# make a list with the values of all months being 0
values_month = [0]*12

# look only at data from the Seattle station
for measurement in Seattle_precipitation:    
    # select the month from the date
    date = measurement['date']
    new_date = date.split('-')
    month = new_date[1]

    # sum all the values for all months
    values_month[int(month)-1] += measurement['value']

print(values_month)

# Store the output in a JSON file.
with open('Seattle_values_month.json', 'w') as file:
    json.dump(values_month, file)