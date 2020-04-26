import requests


class CovidClient:
    def get(self):
        response = requests.get('https://api.covid19api.com/summary')
        return response.json()
