import datetime
import json
import os


class Storage:

    def __init__(self, client):
        self.bucket_name = os.getenv('BUCKET_NAME')
        self.client = client

    def store(self, data):
        bucket = self.client.bucket(self.bucket_name)
        process_date = datetime.datetime.strptime(data.get('Date'), '%Y-%m-%dT%H:%M:%S%z')
        path = process_date.strftime('%Y/%m/')
        blob = bucket.blob(path + process_date.strftime('%Y-%m-%d') + '.json')

        blob.upload_from_string(json.dumps(data), content_type="application/json")
