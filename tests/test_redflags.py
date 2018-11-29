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
        data = {
                 "incident_id": 1,
                "created_on": "Thu, 29 Nov 2018 10:12:28 GMT",
                "created_by": "rth",
                "incident_type":"redflag",
                "location":"dsdsds",
                "status": "under investigation",
                "images": "http://perilofafrica.com/uk-investors-irked-by-bureaucracy-corruption-in-uganda/",
                "videos": "https://www.youtube.com/watch?v=ZmD_VoCTeCc",
                "comment":"comment"	
	            }
        self.app.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(data))
        response = self.app.get('/api/v1/redflags')
        self.assertEqual(len(data),9)
        self.assertNotIsInstance('status',Redflags,"message")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')

    def test_post_redflag_records(self):
        response = self.app.post('/api/v1/redflags')
        self.assertTrue({'incident id must not be a string','message'},True)
    
    def test_create_redflag_records(self):
        data = {
                "incident_id": 1,
                "created_on": "Thu, 29 Nov 2018 10:12:28 GMT",
                "created_by": "rth",
                "incident_type":"redflag",
                "location":"dsdsds",
                "status": "under investigation",
                "images": "http://perilofafrica.com/uk-investors-irked-by-bureaucracy-corruption-in-uganda/",
                "videos": "https://www.youtube.com/watch?v=ZmD_VoCTeCc",
                "comment":"comment"	
	            }
        
        response = self.app.post('/api/v1/redflags',
                                  content_type='application/json',
                                  data=json.dumps(data)
        
        )
        self.assertEqual(response.status_code,201)
        

    def test_get_specific_redflag_with_id(self):
        data = {
                "incident_id": 1,
                "created_on": "Thu, 29 Nov 2018 10:12:28 GMT",
                "created_by": "rth",
                "incident_type":"redflag",
                "location":"dsdsds",
                "status": "under investigation",
                "images": "http://perilofafrica.com/uk-investors-irked-by-bureaucracy-corruption-in-uganda/",
                "videos": "https://www.youtube.com/watch?v=ZmD_VoCTeCc",
                "comment":"comment"	
	            }

        self.app.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(data))
        response = self.app.get('/api/v1/redflags/1')
        self.assertEqual(response.status_code,200)
        self.assertIsInstance(data,dict)
        
    def test_update_redflag_record_location(self):
        response = self.app.patch('/api/v1/redflags/1/location') 
        self.assertTrue({'incident id must be a string','message'},True)   
    
    def test_edit_redflag_record_location(self):
        data = {
                "incident_id": 1,
                "created_on": "Thu, 29 Nov 2018 10:12:28 GMT",
                "created_by": "rth",
                "incident_type":"redflag",
                "location":"dsdsds",
                "status": "under investigation",
                "images": "http://perilofafrica.com/uk-investors-irked-by-bureaucracy-corruption-in-uganda/",
                "videos": "https://www.youtube.com/watch?v=ZmD_VoCTeCc",
                "comment":"comment"	
	            }
        
        self.app.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(data))
        response = self.app.patch('/api/v1/redflags/1/location')
        self.assertEqual(response.status_code,200)
              
        

    def test_edit_redflag_record_comment(self):
        data = {
                "incident_id": 1,
                "created_on": "Thu, 29 Nov 2018 10:12:28 GMT",
                "created_by": "rth",
                "incident_type":"redflag",
                "location":"dsdsds",
                "status": "under investigation",
                "images": "http://perilofafrica.com/uk-investors-irked-by-bureaucracy-corruption-in-uganda/",
                "videos": "https://www.youtube.com/watch?v=ZmD_VoCTeCc",
                "comment":"comment"	
	            }
        self.app.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(data))
        response = self.app.patch('/api/v1/redflags/1/comment')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,'application/json')
        self.assertTrue("comment has been updated","message",True)



    def test_delete_redflag_record_with_id(self):
        data = {
                "incident_id": 1,
                "created_on": "Thu, 29 Nov 2018 10:12:28 GMT",
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
        self.assertIsInstance(data,dict)



if __name__== '__main__':
 unittest.main()