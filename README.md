## D - Build a command line API client

Using the [Metaweather API](https://www.metaweather.com/api/), make a command line tool that receives a city name as an argument and says whether it’s going to rain tomorrow in this city or not. Here again, packaging and tests are optional (but always appreciated). This can be done quite shortly if you’re on a schedule and stick to the minimum.

## How to run the project


# Available commands
## search
Allows you to search for a city available in the API.
If you search 'san' the program will suggest cities such as San Francisco, San Diego, San Jose
By default, up to 10 suggestions will be displayed. You may change this limit using the --limit option

## weather
Allows you to display the weather for a chosen city.
By default, only 1 city will be displayed. You may change this limit using the --limit option.
By default, the weather will be shown for tomorrow. You may change how many days ahead you want a forecast for, using --days-from-today. 0 is today, 1 is tomorrow, 2 is the day after tomorrow, etc...

## coord
This works similarly to the weather command, but with GPS coordinates instead of the city's name.
You must input both a latitude and longitude, using --latitude and --longitude respectively.
Similar to weather, you may set a limit using --limit and/or use --days-from-today to determine when the forecast should apply.

## help
This will guide you through using the program

# Run the project

## Retrieve and run the project

Clone the project:
```
git clone https://github.com/Beertran/TrustPair.git
```

Go to the new folder, build and run the Docker image
```
docker build --network=host -t trustpair:latest .
docker run -it trustpair
```

You may then open the app's CLI and run the following command to run the program:
```
 python3 weather_app.py
```

Expected output:
```
Usage: weather_app.py [OPTIONS] COMMAND [ARGS]...

  Simple CLI for querying weather forecasts from the Metaweather API

Options:
  --help  Show this message and exit.

Commands:
  coord    Search a city from GPS coordinates
  search   This searches a city from the available cities of the API
  weather  This searches the weather using a city name
```

Here are a few examples of commands you may use to try out the program:
```
 python3 weather_app.py search mar

 python3 weather_app.py weather London

 python3 weather_app.py weather San -l 3

 python3 weather_app.py coord --latitude 42.69 --longitude 69.42 --limit 5
```

At any moment, the help command may guide you through the CLI's features:
```
 python3 weather_app.py coord --help
```

# Test the API

To test the API, run the following command:
```
python3 -m pytest
```


Expected output:
```
(.venv) root@Bobby:~/TrustPair# python3 -m pytest
============================================================================================= test session starts ==============================================================================================
platform linux -- Python 3.10.2, pytest-7.0.1, pluggy-1.0.0
rootdir: /root/TrustPair
collected 3 items                                                                                                       

test_weather_app.py ...                                                                                                                                                                                  [100%]

============================================================================================== 3 passed in 3.69s ===============================================================================================
(.venv) root@Bobby:~/TrustPair#
```
