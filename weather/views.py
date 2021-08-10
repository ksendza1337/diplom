from django.shortcuts import render
import requests
from .models import City
from .forms import CityFrom
# Create your views here.
def index(request):
    appid = '38770e827a6eac817219d5471d373d5f'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=" + appid
    if(request.method == 'POST'):
        form = CityFrom(request.POST)
        form.save()

    form = CityFrom

    cities = City.objects.all()
    all_cities= []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city':city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']

        }
        all_cities.append(city_info)


    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)

    #def index1():
        #appid = '38770e827a6eac817219d5471d373d5f'
        #url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=" + appid
        #city = 'London'
        #res = requests.get(url.format(city))
       # print(res.text)
   # index1()