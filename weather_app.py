import click
import requests

API_BASE_URL = 'https://www.metaweather.com/api/location/'

@click.group()
def main():
    """Simple CLI for querying weather forecasts from the Metaweather API
    """
    pass


def search_weather_by_woeid(woeid: int, days_from_today: int = 1):
    """Search the weather using a woeid

    Args:
        woeid (int): The ID to search
        days_from_today (int, optional): Number of days starting from today for which we want a forecast. Defaults to 1.
    """
    url_format = API_BASE_URL + '{}'

    if days_from_today <= 5:
        response = requests.get(url_format.format(woeid))
        if 'title' in response.json() and 'consolidated_weather' in response.json():
            city_name = response.json()['title']
            relevant_forecast = response.json()['consolidated_weather'][days_from_today]
            if 'weather_state_name' in relevant_forecast and 'weather_state_name' in relevant_forecast:
                relevant_forecast_state = relevant_forecast['weather_state_name']
                applicable_date = relevant_forecast['applicable_date']
                click.echo(city_name + ': ' + relevant_forecast_state.lower() + ' (' + applicable_date + ')')
            else:
                click.echo('Error: Missing crucial data for the requested city and date.')
        else:
            click.echo('Error: The consolidated weather data could not be found for this city.')
    else:
        click.echo('Error: Forecasts cannot be made reliably more than 5 days ahead.')


def search_multiple_weather_forcasts(cities_dict: dict, limit: int, days_from_today: int):
    """A generic method used to retrieve a weather forecast from a list of cities
    This may be called regardless of how the list of cities was determined (woeid, name, coordinates, etc...)

    Args:
        response (dict): the API response
        limit (int): the maximum number of forecasts to display
        days_from_today (int): the number of days starting from today for which we want a forecast
    """
    ## We iterate in the list of cities using i
    for i in range(min(limit, len(cities_dict.json()))):
        if 'woeid' in cities_dict.json()[i]:
            city_woeid = cities_dict.json()[i]['woeid']
            search_weather_by_woeid(city_woeid, days_from_today=days_from_today)
        else:
            click.echo('Error: Unexpected response from the API. The woeid could not be found.')

@main.command()
@click.argument('city', type=str)
@click.option('--limit', '-l', default=10, type=int, help='The maximum number of cities you want displayed')
def search(city: str, limit: int):
    """This searches a city from the available cities of the API

    Args:
        city (str): The name of the city
    """
    url_format = API_BASE_URL + 'search/?query={}'

    response = requests.get(url_format.format(city))

    ## We iterate in the list of cities using i
    for i in range(min(limit, len(response.json()))):
        if 'title' in response.json()[i]:
            click.echo(response.json()[i]['title'])
        else:
            click.echo('Error: The data retrieved from the API did not contain the city name required to proceed.')

@main.command()
@click.option('--latitude', '--lat', required=True)
@click.option('--longitude', '--long', required=True)
@click.option('--limit', '-l', default=1, type=int, help='The maximum number of cities you want displayed')
@click.option('--days-from-today', '-d', default=1, type=int)
def coord(latitude: float, longitude: float, limit: int, days_from_today: int):
    """Search a city from GPS coordinates
    """
    url_format = API_BASE_URL + 'search/?lattlong={}'
    response = requests.get(url_format.format(latitude + ',' + longitude))  
    search_multiple_weather_forcasts(response, limit=limit, days_from_today=days_from_today)


@main.command()
@click.argument('city', type=str)
@click.option('--limit', '-l', default=1, type=int, help='The maximum number of cities you want displayed')
@click.option('--days-from-today', '-d', default=1, type=int, help='The number of days from today for which you want a forecast')
def weather(city: str, limit: int, days_from_today: int):
    """This searches the weather using a city name
    """
    url_format = API_BASE_URL + 'search/?query={}'
    response = requests.get(url_format.format(city))
    search_multiple_weather_forcasts(response, limit=limit, days_from_today=days_from_today)


if __name__ == "__main__":
    main()