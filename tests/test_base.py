from api.database.db import DatabaseConnection
from api import app
import unittest


class BaseTests(unittest.TestCase):
    def setUp(self):
        
        self.test_client = app.test_client()
        self.db = DatabaseConnection()
        self.db.create_table_incidents()
        self.db.create_table_users()
        
        self.user = {
            "email": "joan@gmail.com",
            "first_name": "dalai",
            "last_name": "ann",
            "other_names": "mermaid",
            "phone_number": "abcdefg",
            "password":"lalaland",
            "username": "trickster"              
                }

        self.signin = {
            "password":"lalaland",
            "username": "trickster"

            }

        self.intervention = {
                "comment": "blaj",
                "created_by": 456,
                "created_on": "Thu, 29 Nov 2018 14:34:43 GMT",
                "images": "https://www.monitor.co.ug/News/National/688334-1286590-a2a4psz/index.html",
                "incident_type": "intervention",
                "location": "karamoja",
                "status": "under investigation",
                "videos": "https://www.youtube.com/watch?v=hqJ8StaE4CY"
                                                       
                }


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

    


    def tearDown(self):
         self.db.drop_table_incidents()
         self.db.drop_table_users()
         

