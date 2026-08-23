from weatherapi import get_weather
from json_holider import get_json, write_json
from input import userinput
from check_func import check_cashing

def main():
    city_name = userinput()
    if get_json() != False:
        get = get_json()
        check = check_cashing(city_name, get)
        print(check)
        if check == False:
            weather = get_weather(city_name)
            print(weather)
            get.append(weather)
            write = write_json(get)
    else:
        get = get_json()
        weather = get_weather(city_name)
        print(weather)
        write = write_json(weather)
main()