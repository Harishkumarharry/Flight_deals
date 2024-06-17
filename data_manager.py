import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEET_ENDPOINT = f"https://api.sheety.co/{os.environ['SHEET_API_KEY']}/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self._user = os.environ["SHEET_USERNAME"]
        self._password = os.environ["SHEET_PASSWORD"]
        self.headers = {
            "Authorization": os.environ["SHEET_AUTH"]
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )

    pass
