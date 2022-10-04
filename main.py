from fastapi import FastAPI, Query
from weather import Weather

app = FastAPI()


@app.get("/weather/city")
def read_params(params: str, city: str = Query() ) -> dict:
    params = params.split()
    weather = Weather()
    data = weather.get_weather_in_city(city)
    ans = {city: {param:data[param] for param in params}}
    return ans


@app.get("/weather/cities")
def read_params_cities(params: str, cities: list[str] = Query()) -> dict:
    ans = {}
    weather = Weather()
    params = params.split()
    for city in cities:
        data = weather.get_weather_in_city(city)
        ans[city] = {param:data[param] for param in params}
    return ans
