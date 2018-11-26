import unittest
from api.routes.user_endpoints import app
from api.models.user import Users
from api.validations import user_valid

import json


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
















if __name__== '__main__':
 unittest.main()