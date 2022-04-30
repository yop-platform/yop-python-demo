# -*- coding: utf-8 -*-

from yop_python_sdk.client.yopclient import YopClient
import yop_python_sdk.utils.yop_logger as yop_logger


class YopPay(object):
    def __init__(self):
        """
        Run the init test.

        Args:
            self: write your description
            app_key: write your description
            secret_key: write your description
            yop_server: write your description
        """
        self.logger = yop_logger.get_logger()
        self.client = YopClient()

    def pay(self, merchantNo):
        """
        Run the get test.

        Args:
            self: write your description
            client: write your description
        """
        api = '/rest/v1.0/cnppay/bank-limit/query'
        params = {
            'merchantNo': merchantNo
        }
        res = self.client.get(api, params)
        self.logger.warn(res)


if __name__ == "__main__":
    yop_pay = YopPay()
    yop_pay.pay('10001')
