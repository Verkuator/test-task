import requests
from functools import lru_cache


class Weather():
    def __init__(self) -> None:
        self.url: str = "https://api.openweathermap.org/data/2.5/weather?"
        self.units: str = "&units=metric"
        self.appid: str = "4cc428405eb5f164ee303a44d930ee92"

    @lru_cache(maxsize=16)
    def get_weather_in_city(self, city: str) -> str:
        
        req = Weather._make_url(self, city)
        answer = requests.get(req).json()
        answer_dict = {}
        answer_dict['temperature'] = answer['main']['temp']
        answer_dict['feels'] = answer['main']['feels_like']
        answer_dict['wind'] = answer['wind']
        answer_dict['visibility'] = answer['visibility']
        answer_dict['humidity'] = answer['main']['humidity']
        return answer_dict
        
        
    def _make_url(self, city) -> str:
        return (self.url + 'q=' + city + 
                "&appid=" + self.appid + self.units)


