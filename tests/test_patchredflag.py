import unittest
from api.routes.endpoints import app
from api.models.incident import Incidents
from api.models.user import Users
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_edit_redflag_record_location(self):
        response = self.app.patch('/api/v1/redflags/1/location')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')

    def test_edit_redflag_record_comment(self):
        response = self.app.patch('/api/v1/redflags/1/comment')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')



if __name__== '__main__':
 unittest.main()
