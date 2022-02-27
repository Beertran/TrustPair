import click
import responses
from click.testing import CliRunner
from weather_app import search, search_weather_by_woeid, weather

runner = CliRunner()

def test_search():
    result = runner.invoke(search, ['lon'])
    assert result.exit_code == 0
    assert result.output == 'London\nBarcelona\nLong Beach\n'
    result = runner.invoke(search, ['aeazeaze'])
    assert result.exit_code == 0
    assert result.output == ''
    result = runner.invoke(search, [''])
    assert result.exit_code == 1
    assert result.output == ''


@responses.activate
def test_search_fails():
    responses.add(responses.GET, 'https://www.metaweather.com/api/location/search/?query=Paris',
                  json=[{'title': 'Revoir Paris'}], status=404)
    result = runner.invoke(search, ['Paris'])
    assert result.exit_code == 0
    assert result.output == 'Revoir Paris\n'

    responses.add(responses.GET, 'https://www.metaweather.com/api/location/search/?query=Paris',
                  json=[{'title_is_missing': 'no_title'}], status=404)
    result = runner.invoke(search, ['Paris'])
    assert result.exit_code == 1
    assert result.output == ''

def test_weather():
    result = runner.invoke(weather, ['om', '--limit', '2'])
    print(result.output)
    assert result.output.count('\n') == 2
    
    result = runner.invoke(weather, ['sa', '--limit', '4'])
    print(result.output)
    assert result.output.count('\n') == 4
    assert 'San Francisco' in result.output
    assert 'Osaka' in result.output
    assert 'San Diego' in result.output