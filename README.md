## D - Build a command line API client

Using the [Metaweather API](https://www.metaweather.com/api/), make a command line tool that receives a city name as an argument and says whether it’s going to rain tomorrow in this city or not. Here again, packaging and tests are optional (but always appreciated). This can be done quite shortly if you’re on a schedule and stick to the minimum.

## How to run the project

Clone the project:
```
git clone https://github.com/Beertran/TrustPair.git
```

Build and run the Docker image
```
docker build -t trustpair:latest .
docker run -it trustpair
```

# Run the project

To start the API, run the following command:
```
 python3 weather_app.py
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