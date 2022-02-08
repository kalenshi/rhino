#! /usr/bin/python
"""
Will house the coinbase operator that performs several get
requests on different endpoints
"""
import hashlib
import hmac

import requests, time
from datetime import datetime
from requests.auth import AuthBase

from airflow.models import BaseOperator


class CoinbaseAuth(AuthBase):
    def __init__(self, api_key, api_secret):
        """
        Initialize coinbase authentication
        :param api_key:
        :param api_secret:
        """
        self.api_key = api_key
        self.api_secret = api_secret

    def __call__(self, request, *args, **kwargs):
        timestamp = str(time.time())
        message = f"{timestamp}{request.method}{request.path_url}{request.body or ''}".encode()

        signature = hmac.new(
            self.api_secret.encode(),
            message,
            hashlib.sha256
        ).hexdigest()

        request.headers.update({
            "CB-ACCESS-SIGN": signature,
            "CB-ACCESS-TIMESTAMP": timestamp,
            "CB-ACCESS-KEY": self.api_key,
            "CB-ACCESS-VERSION": datetime.date(datetime.now()).__str__().encode()
        })

        return request


class CoinbaseOperator(BaseOperator):
    """
    Coinbase operator will provide access to multiple coinbase endpoints
    """
    template_fields = ["api_key", "api_secret", "query"]
    template_fields_renderers = {
        "query": "sql"

    }

    def __str__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, context):
        pass
