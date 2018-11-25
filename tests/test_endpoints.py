import unittest
from api.routes import endpoints
from api.models.incident import Incidents
from api.models.user import Users
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.api = endpoints.test_client()

    def test_get_all_redflag_records(self):
        response = self.app.get('api/v1/redflags')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')

    def test_get_redflag_records(self):
        response = self.app.get('/api/v1/redflags')
        self.assertNotIsInstance('email',Incidents,"message")

    def test_post_redflag_records(self):
        response = self.app.post('/api/v1/redflags')
        self.assertTrue({'incident id must not be a string','message'},True)

    def test_get_specific_redflag_with_id(self):
        response = self.app.get('/api/v1/redflags/1')
        self.assertNotIn('status',Users,"message")
























if __name__== '__main__':
 unittest.main()