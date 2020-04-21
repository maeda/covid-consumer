import settings
from storage import Storage


def run(request):
    from google.cloud import storage
    storage = Storage(storage.Client())
    data = request.get_json()
    storage.store(data)
