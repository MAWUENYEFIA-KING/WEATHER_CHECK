import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
    else:
        print("City not found.")

def main():
    city = input("Enter city name: ")
    api_key = "b915c2e0d55f1b38114f82ff712bcf8c"  
    get_weather(city, api_key)

if __name__ == "__main__":
    main()