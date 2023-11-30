# import required modules
# pip install requests
import requests, json

# Enter your API key here
with open("default_key.txt", "r+") as file1:
    # Reading from a file
    api_key= file1.read().rstrip()

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_weather_dict = {}

def print_weather_dict(d) :
    print(" Temperature (in celsius unit) = " +
                                            str(d['current_temperature']) +
                    "\n atmospheric pressure (in hPa unit) = " +
                                            str(d['current_pressure']) +
                    "\n humidity (in percentage) = " +
                                            str(d['current_humidity']) +
                    "\n description = " +
                                            d['weather_description'])    

while (True) :
    # Give city name
    city_name = input("Enter city name : ")

    if city_name == 'QUIT' :
        break

    weather_dict = city_weather_dict.get(city_name)
    if (weather_dict == None) :
        # complete_url variable to store
        # complete url address
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # get method of requests module
        # return response object
        response = requests.get(complete_url)

        # json method of response object 
        # convert json format data into
        # python format data
        x = response.json()

        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":

            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = round(y["temp"] - 273.15)

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding 
            # to the "description" key at 
            # the 0th index of z
            weather_description = z[0]["description"]

            city_weather_dict[city_name] = {
                'current_temperature' : current_temperature,
                'current_pressure' : current_pressure,
                'current_humidity' : current_humidity,
                'weather_description' : weather_description}
            # print following values

            print_weather_dict(city_weather_dict[city_name])

        else:
            print("Weather data for " + city_name + " is not available")
    else:
        print_weather_dict(weather_dict)
