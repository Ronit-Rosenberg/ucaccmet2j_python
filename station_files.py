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


# PART 2
# ASSIGNMENT: Calculate the sum of the precipitation over the whole year
values_year = sum(values_month)
print(f' the precipitation for Seattle for the whole year is {values_year}')

# ASSIGNMENT: Calculate the relative precipitation per month 
# (percentage compared to the precipitation over the whole year)

# empty list for relative values per month
relative_values_month = []

# make list with relative values for all months
for value in values_month:
    # calculate relative values and add to the empty list
    relative_values_month.append(value*100/values_year)

# print the relative values
print(relative_values_month)

# Store the output in a JSON file.
with open('Seattle_relative_values_month.json', 'w') as file:
    json.dump(relative_values_month, file)