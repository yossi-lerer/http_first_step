import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("PIXEL_API")

base_url = "https://pixabay.com/api/"


def get_pixabay(query):
    if os.path.exists(f"{query}.jpg"):
        return True
    base_url = "https://pixabay.com/api/"
    api_key = os.getenv("PIXEL_API")
    res = requests.get(f"{base_url}?key={api_key}&q={query}")
    res = res.json()
    
    image_url = res["hits"][0]["webformatURL"]
    image_data = requests.get(image_url).content
    with open(f"{query}.jpg", "wb") as f:
        f.write(image_data)
    return res