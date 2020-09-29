import requests
from django.shortcuts import render

from . import config

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + config.api_key + ''
    city = 'Noida'

    if request.method == 'POST':    
        city = request.POST.get('city') 
        res = requests.get(url.format(city)).json()
        print(res)
        if int(res['cod']) != 200:
            return render(request, 'weather/error.html', {'error': 'Invalid City'})    

    res = requests.get(url.format(city)).json()

    city_weather = {
        'city': res['name'],
        'temperature': res['main']['temp'],
        'description': res['weather'][0]['description'],
        'icon': res['weather'][0]['icon'],
        'longitude': res['coord']['lon'],
        'latitude': res['coord']['lat'],
    }

    context = {'city_weather': city_weather, 'mapbox_access_token' : config.mapbox_access_token}

    return render(request, 'weather/index.html', context)