import urllib.request
import json
from pprint import pprint

# API KEYS
from config import WEATHER_API_KEY, CONCERT_API_KEY

# Useful URLs
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
CONCERT_URL = "https://app.ticketmaster.com/discovery/v2/events.json"



def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

def get_temp(city,country_code):
    """
    Given a city and country code, return the current temperature of the given place. 
    """
    city = city.replace(" ", "%20")
    url = WEATHER_URL + f'?q={city},{country_code}&APPID={WEATHER_API_KEY}'
    response_data = get_json(url)
    temp = response_data['main']['temp'] - 273.15
    return round(temp,0)


def get_events(city,state_code,number):
    """
    Given city and state code, return the recent concert's date, name, picture, and url hold in the given place.
    """
    city = city.replace(" ", "%20")
    url = CONCERT_URL + f'?apikey={CONCERT_API_KEY}&city={city}&stateCode={state_code}'
    response_data = get_json(url)
    events = []
    i = 0
    for i in range (number):
        dic = {}
        dic['name'] = response_data['_embedded']['events'][i]['name']
        dic['pic'] = response_data['_embedded']['events'][i]['images'][0]['url']
        dic['date'] = response_data['_embedded']['events'][i]['dates']['start']['localDate']
        dic['link'] = response_data['_embedded']['events'][i]['url']
        events.append(dic)

    return events


def main():
    city = 'Boston'
    country_code = 'US'
    state_code = 'MA'
    number = 3
    print(get_temp(city,country_code))
    print(get_events(city,state_code,number))



if __name__ == '__main__':
    main()