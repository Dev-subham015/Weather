from django.shortcuts import render
import requests

def index(request):
    city = request.GET.get("city", "Mumbai")
    api_key = 'f7f4f204da1166bf44e7e57d6f6b8e1c'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    # Check if the city is found
    if response.status_code == 200 and 'name' in data:
        payload = {
            'city': data["name"],
            'country': data["sys"]["country"],
            "icon": data["weather"][0]["icon"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
        }
        context = {
            "data": payload,
            "error": None
        }
    else:
        context = {
            "data": None,
            "error": "No result found for the specified city."
        }
    
    return render(request, "home/index.html", context)
