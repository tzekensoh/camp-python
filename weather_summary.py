import json

with open("death_valley_2021_full.csv") as weather :
    lines = weather.readlines()

##print(lines[0])
##print(len(lines))

## the column number of maximum temperature of the day
## initialize to an invalid number first
column_number_of_tmax = -1
column_number_of_date = -1

## loop throught the header row to find the position of "TMAX"
for pointer, column_name in enumerate(lines[0].split(',')) :
    if column_name == '"TMAX"' :
        column_number_of_tmax = pointer
    if column_name == '"DATE"' :
        column_number_of_date = pointer    

weather_summary = {}
weather_summary["max_tmax"] = -1
weather_summary["max_date"] = ""
for day_weather in lines[1:] :
    fields = day_weather.split(',')
    current_date = fields[column_number_of_date + 1].replace('"', '')
    try:
        current_tmax = float(fields[column_number_of_tmax + 1].replace('"', ''))
    except ValueError:
        print("Line with ValueError is: " + day_weather)
    else: 
        if current_tmax > weather_summary["max_tmax"] :
            weather_summary["max_tmax"] = current_tmax
            weather_summary["max_date"] = current_date

with open("weather_summary.txt", "w") as weather_summary_file :
    json.dump(weather_summary, weather_summary_file)

