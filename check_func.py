import time

def check_cashing(city_name, data):
    for city in data:
        if city["name_city"] == city_name:
            if (float(city["current_type"]) - time.time()) < 3600:
                return city
            else:
                return False
    return False