import unittest
from api.routes.redflag_endpoints import app
from api.models.incident import Incidents, Redflags, redflags_list
from api.validations import valid

import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        redflags_list.clear()
        

    def test_get_all_redflag_records(self):
        response = self.app.get('/api/v1/redflags')
        response = json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')
        self.assertNotIsInstance('email',Redflags,"message")
        self.assertEqual(len(response),9)

    def test_post_redflag_records(self):
        response = self.app.post('/api/v1/redflags')
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.content_type,'application/json')
        self.assertTrue({'incident id must not be a string','message'},True)

    def test_get_specific_redflag_with_id(self):
        response = self.app.get('/api/v1/redflags/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')
        self.assertNotIn('username',Redflags,"message")

    def test_edit_redflag_record_location(self):
        response = self.app.patch('/api/v1/redflags/1/location')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')
        self.assertFalse({'incident id must be a string','message'},False)

    def test_edit_redflag_record_comment(self):
        response = self.app.patch('/api/v1/redflags/1/comment')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')
        self.assertTrue("comment has been updated","message",True)

    def test_delete_redflag_record_with_id(self):
        data = {
                "created_by": "rth",
                "incident_type":"redflag",
                "location":"dsdsds",
                "status": "under investigation",
                "images": "http://perilofafrica.com/uk-investors-irked-by-bureaucracy-corruption-in-uganda/",
                "videos": "https://www.youtube.com/watch?v=ZmD_VoCTeCc",
                "comment":"comment"	
	            }
        self.app.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(data))
        response = self.app.delete('/api/v1/redflags/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')

    














if __name__== '__main__':
 unittest.main()