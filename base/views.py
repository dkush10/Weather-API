from django.shortcuts import render, redirect
import requests

# Create your views here.

api_key='66343e8b7226baa70baafa29f2a15b3c'
weather_data=None

def home(request):
    global city
    global weather_data
    if request.method=="POST":
        city=request.POST['city']
        weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
        print(weather_data.json())
        return redirect('showdata')
    return render(request,'home.html')

def showdata(request):
    temperature = 0
    temp1 = weather_data.json()
    temp2 = temp1['main']
    temperature = round(temp2['temp'] - 273.15)
    feels_lke = round(temp2['feels_like'] - 273.15)

    context={
        'data':weather_data.json(),
        'city':city,
        'temp':temperature,
        'feels_like':feels_lke,
    }
    return render(request,'showdata.html',context)