import os

import requests

FILTERING = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY", None)


def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}")
    try:
        response = requests.get(
            URL, params={"key": API_KEY, "q": FILTERING}
        ).json()
        location = (f"{response['location'].get('name')}/"
                    + response["location"].get("country"))
        localtime = response["location"].get("localtime")
        temperature = response["current"].get("temp_c")
        condition = response["current"]["condition"].get("text")

        print(
            f"{location} {localtime} Weather: "
            f"{temperature} Celsius, {condition}"
        )
    except Exception:
        print("Error! Something went wrong!")


if __name__ == "__main__":
    get_weather()
