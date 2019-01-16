import unittest
from api.routes.redflag_endpoints import app
from api.models.incident import Incidents, Redflags, redflags_list
from api.validations import valid
import json

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.test_client = app.test_client()
        self.redflag = {
                "created_on": "Thu, 29 Nov 2018 10:12:28 GMT",
                "created_by": 123,
                "incident_type":"redflag",
                "location":"dsdsds",
                "status": "under investigation",
                "images": "http://perilofafrica.com/uk-investors-irked-by-bureaucracy-corruption-in-uganda/",
                "videos": "https://www.youtube.com/watch?v=ZmD_VoCTeCc",
                "comment":"comment"	
                                       
                }

        
    def test_get_all_redflag_records(self):
        self.test_client.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(self.redflag))
        response = self.test_client.get('/api/v1/redflags')
        self.assertEqual(len(self.redflag),8)
        self.assertNotIsInstance('status',Redflags,"message")
        self.assertEqual(200,response.status_code)
        self.assertEqual(response.content_type,'application/json')

    def test_post_redflag_records(self):
        response = self.test_client.post('/api/v1/redflags')
        self.assertTrue({'incident id must not be a string','message'},True)
    
    def test_create_redflag_records(self):
        response = self.test_client.post('/api/v1/redflags',
                                  content_type='application/json',
                                  data=json.dumps(self.redflag)
        
        )
        self.assertEqual(200,response.status_code)
        

    def test_get_specific_redflag_with_id(self):
        self.test_client.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(self.redflag))
        response = self.test_client.get('/api/v1/redflags/1')
        self.assertEqual(200,response.status_code)
        self.assertIsInstance(self.redflag,dict)    
        
    def test_update_redflag_record_location(self):
        response = self.test_client.patch('/api/v1/redflags/1/location') 
        self.assertTrue({'incident id must be a string','message'},True)   
    


    def test_edit_redflag_record_location(self):

        change_location = {
                            "location": "lugazi"
                          }
        
        self.test_client.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(self.redflag))
        response = self.test_client.patch('/api/v1/redflags/1/location', content_type= 'application/json', 
                                   data = json.dumps(change_location))
        res = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
              

    def test_edit_redflag_record_comment(self):
        edited_data = {
                         
                "comment":"like"	
	            }
         
        self.test_client.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(self.redflag))
        response = self.test_client.patch('/api/v1/redflags/1/comment',content_type= 'application/json',
                                  data = json.dumps(edited_data))
        res = json.loads(response.data.decode())
        self.assertEqual(200,response.status_code)
        self.assertIn("updated red-flag record comment", res['message']) 


    def test_delete_redflag_record_with_id(self):
        self.test_client.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(self.redflag))
        response = self.test_client.delete('/api/v1/redflags/1')
        self.assertEqual(200,response.status_code)
        self.assertEqual(response.content_type,'application/json')
        self.assertIsInstance(self.redflag,dict)

    def test_post_redflag_error(self):
        self.test_client.post('/api/v1/redflags', content_type= 'application/json', data = json.dumps(self.redflag))
        response = self.test_client.delete('/api/v1/redflags/1')
        self.assertEqual(400,response.status_code)









if __name__== '__main__':
 unittest.main()



# class TestEndpoints(unittest.TestCase):
#     def setUp(self):
#         self.app = app.test_client()

#     def tearDown(self):
#         redflags_list.clear()
