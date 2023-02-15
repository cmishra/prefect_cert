import requests
from prefect import flow, task

@task
def get_location_temp(lat, lon):
    resp = requests.get('https://api.open-meteo.com/v1/forecast', params={"longitude": lon, "latitude": lat, "current_weather": True})
    return resp.json()['current_weather']

@flow
def test_flow():
    res = get_location_temp("40.7098767","-74.0146772")
    print('New York temperature', res)
    res = get_location_temp("40.7098767","74.0146772")
    print('New York flipped 1 temperature', res)
    res = get_location_temp("-40.7098767","74.0146772")
    print('New York flipped 2 temperature', res)


if __name__ == "__main__":
    test_flow()

