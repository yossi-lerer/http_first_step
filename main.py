from weatherapi import get_weather
from json_holider import get_json, write_json
from input import userinput

def main():
    city_name = userinput()
    weather = get_weather(city_name)
    write = write_json(weather)

main()