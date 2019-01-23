import psycopg2
from psycopg2.extras import RealDictCursor
from pprint import pprint

class DatabaseConnection():
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='ireporter_database' user='postgres' host='localhost'  port= '5432'"
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        except:
             pprint('cannot connect to database')

    def create_table_users(self):
      create_table_command = "CREATE TABLE user_data(user_id SERIAL PRIMARY KEY, firstname VARCHAR(100),\
                             lastname VARCHAR(100), othernames VARCHAR(100),email VARCHAR(50) UNIQUE,\
                             phonenumber VARCHAR(50),username VARCHAR(20) UNIQUE, password VARCHAR(10),\
                             registered DATE,isAdmin BOOLEAN)"
      self.cursor.execute(create_table_command)
    
    def insert_users(self, firstname ,lastname , othernames,email ,phonenumber,
                     username,password ,registered,isAdmin):

        user = f"INSERT INTO user_data (firstname, lastname, othernames,email,\
                phonenumber,username,password,registered,isAdmin) VALUES('{firstname}', '{lastname}',\
                '{othernames}','{email}','{phonenumber}','{username}', '{password}','{registered}','{isAdmin}')\
                 RETURNING *;"
        pprint(user)
        self.cursor.execute(user)
        return self.cursor.fetchone()
                                       
    def insert_admins(self, firstname ,lastname , othernames,email ,phonenumber,
                     username,password ,registered,isAdmin):

        admin = f"INSERT INTO user_data (firstname, lastname, othernames,email,\
                phonenumber,username,password,registered,isAdmin) VALUES('{firstname}', '{lastname}',\
                '{othernames}','{email}','{phonenumber}','{username}', '{password}','{registered}','True')\
                 RETURNING *;"
        pprint(admin)
        self.cursor.execute(admin)
        return self.cursor.fetchone()
    
    def get_users(self,username):
    
        query = """SELECT * FROM user_data """ 
        self.cursor.execute(query)
        return self.cursor.fetchall()  
    
    
    
    def get_specific_user(self,username,password):
        
        query = """SELECT username FROM user_data WHERE username = '{}' AND password = '{}'""".format(username, password) 
        self.cursor.execute(query)
        return self.cursor.fetchone() 
        

    # INCIDENTS DATABASE    

    def create_table_incidents(self):
      create_table_command = "CREATE TABLE incident_data(incident_id SERIAL PRIMARY KEY, createdon DATE,\
                             createdby INT, incident_type VARCHAR(100),location VARCHAR(100),\
                             status VARCHAR(100),images VARCHAR(100), videos VARCHAR(100),\
                             comment VARCHAR(140));"
      self.cursor.execute(create_table_command)

    
    def put_incidents(self,createdon, createdby, incident_type, location, status, images, videos, comment):

        incident = f"INSERT INTO incident_data (createdon, createdby, incident_type, location,\
                    status, images, videos, comment) VALUES ('{createdon}', '{createdby}',\
                    '{incident_type}','{location}','{status}','{images}', '{videos}','{comment}') RETURNING *;"
        
        self.cursor.execute(incident) 
        return self.cursor.fetchone()                                      

    def get_incidents(self, incident_type):
    
        query = """SELECT * FROM incident_data WHERE incident_type =  '{}'""".format(incident_type) 
        self.cursor.execute(query)
        return self.cursor.fetchall()  









    
    
    
if __name__ == '__main__':
   database_connection = DatabaseConnection()
   database_connection.create_table_users()
   database_connection.create_table_incidents()

