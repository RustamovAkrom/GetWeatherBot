import requests
from config import *
from dotenv import load_dotenv
import datetime

load_dotenv()


def get_weather(city, open_weather_token):
    smiles = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Snow": "Snow \U0001F328",
        "Wind": "Wind \U00002600",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Mist": "Mist \U00001F328"
    }

    try:
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + open_weather_token + '&units=metric')
        data = response.json()
        print(data)
        smile_weather = data['weather'][0]['main']
        if smile_weather in smiles:
            wd = smiles[smile_weather]
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_temestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_temestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = sunset_temestamp - sunrise_temestamp

        return f"""\t{city}\n
        havo harorati: {temperature}℃   {wd}\n
        Namligi: {humidity} \n
        Bosim: {pressure} mm.pt.ct\n
        Shamol tezligi: {wind} m/s"\n
        Quyosh chiqishi: {sunrise_temestamp}\n
        Quyosh botishi: {sunset_temestamp}\n
        Kun dovomiligi: {length_of_the_day}"""

    except Exception as ex:
        pass


def main():

    get_weather(input("CITY: "), OPEN_WEATHER_SECRET_KEY)


if __name__ == '__main__':
    main()