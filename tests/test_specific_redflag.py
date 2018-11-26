import unittest
from api.routes.endpoints import app
from api.models.incident import Incidents
from api.models.user import Users
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_specific_redflag_with_id(self):
        response = self.app.get('/api/v1/redflags/1')
        self.assertNotIn('username',Incidents,"message")

    def test_get_specific_redflag_with_id(self):
        response = self.app.get('/api/v1/redflags/1')
        self.assertEqual(response.content_type,'application/json')







if __name__== '__main__':
 unittest.main()
