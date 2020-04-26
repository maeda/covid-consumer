import datetime

import pytz

import settings
from client import CovidClient
from storage import Storage


class CovidConsumer:
    def __init__(self, storage, client):
        self.storage = storage
        self.client = client

    def __call__(self):
        response = self.client.get()
        self.storage.store(response)


def run(request):
    from google.cloud import storage
    app = CovidConsumer(Storage(storage.Client()), CovidClient())
    app()
