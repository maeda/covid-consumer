import json
import os
import unittest
from unittest import mock
from unittest.mock import patch, Mock

from flask import Flask, request

import main


class MainTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bucket_name = os.getenv('BUCKET_NAME')

        self.app = Flask(__name__)

        @self.app.route('/', methods=['POST'])
        def endpoint():
            return main.run(request)

    @mock.patch('flask.request')
    def test_should_save_summary_data(self, request_mock):
        request_mock.get_json.return_value = self._get_summary_data()

        with patch('google.cloud.storage.Client') as client_mock:
            upload_from_string_mock = Mock()
            bucket_mock = Mock()
            blob_mock = Mock()
            client_mock.return_value.bucket = bucket_mock
            bucket_mock.return_value.blob = blob_mock
            blob_mock.return_value.upload_from_string = upload_from_string_mock

            main.run(request_mock)

        self.assertEquals(self.bucket_name, bucket_mock.call_args_list[0][0][0])
        self.assertEquals('2020/04/2020-04-19.json', blob_mock.call_args_list[0][0][0])
        self.assertEquals(self._get_summary_data(), json.loads(upload_from_string_mock.call_args_list[0][0][0]))

    def _get_summary_data(self):
        with open(os.path.join(os.path.dirname(__file__), 'stubs', 'summary_2020-04-19.json'), 'r') as f:
            return json.loads(f.read())

