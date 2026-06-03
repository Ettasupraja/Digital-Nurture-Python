import requests

try:
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=11&longitude=78&current_weather=true"
    )

    data = response.json()

    print("Temperature:", data["current_weather"]["temperature"])
    print("Wind Speed:", data["current_weather"]["windspeed"])

except requests.exceptions.RequestException:
    print("Network Error")