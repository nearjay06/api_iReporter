import unittest
from api.routes.endpoints import app
from api.models.incident import Incidents
from api.models.user import Users
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_all_redflag_records(self):
        response = self.app.get('/api/v1/redflags')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')

    def test_get_redflag_records(self):
        response = self.app.get('/api/v1/redflags')
        self.assertNotIsInstance('email',Incidents,"message")

if __name__== '__main__':
 unittest.main()
