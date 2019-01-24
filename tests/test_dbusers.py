
# import json
# from tests.test_base import BaseTests 
# from api.secure.safe import encode_token

# class TestEndpoints(BaseTests):
     
#     def test_get_all_users(self):

#         response = self.test_client.get(
#             '/api/v2/users',
#             headers={'Authorization': encode_token(1)},
#             content_type='application/json')
#         data = response.data.decode()
#         message = {"message","Created intervention record"}
#         self.assertEqual(response.status_code,200)
#         self.assertTrue(json.loads(data),message )

     
    # def test_user_signup(self):
    #     response = self.test_client.post(
    #         'api/v2/auth/admins/signup',
    #         content_type='application/json',
    #         data=json.dumps(self.user)
    #     )
    #     auth = json.loads(response.data.decode())
    #     response = self.test_client.post(
    #         '/api/v2/auth/admins/signup',
    #         headers={'Authorization': auth['token']},
    #         content_type='application/json',
    #         data=json.dumps(self.user)
    #     )
    #     result = json.loads(response.data.decode())
    #     self.assertEqual(201,response.status_code)
    #     self.assertTrue({'user id is required and it should be an integer','message'},True)
    #     self.assertEqual(len(self.user),9)
        


        # response = self.test_client.post(
        #     '/api/v2/users',
        #     headers={'Authorization': encode_token(1)},
        #     content_type='application/json')
        # data = response.data.decode()
        # message = {"message","Created intervention record"}
        # self.assertEqual(response.status_code,200)
        # self.assertTrue(json.loads(data),message )
        # self.assertEqual(201,response.status_code)
        # self.assertTrue({'user id is required and it should be an integer','message'},True)
        # self.assertEqual(len(self.user),9)
        
   
    # def test_admin_signup(self):
    #     response = self.test_client.post(
    #         'api/v2/auth/admins/signup',
    #         content_type='application/json',
    #         data=json.dumps(self.user)
    #     )
    #     auth = json.loads(response.data.decode())
    #     response = self.test_client.post(
    #         '/api/v2/auth/admins/signup',
    #         headers={'Authorization': auth['token']},
    #         content_type='application/json',
    #         data=json.dumps(self.user)
    #     )
    #     result = json.loads(response.data.decode())
    #     self.assertEqual(201,response.status_code)
    #     self.assertTrue({'user id is required and it should be an integer','message'},True)
    #     self.assertEqual(len(self.user),9)
        

    #     response = self.test_client.post('/api/v2/auth/admins/signup', content_type= 'application/json',
    #                               data = json.dumps(self.user))
    #     self.assertEqual(201,response.status_code)
    #     self.assertTrue({'user id is required and it should be an integer','message'},True)
    #     self.assertEqual(len(self.user),9)


    # def test_user_signin(self):
    #     items={
    #         "password":"lalaland",
    #         "username": "trickster"
                       
    #         }

    #     response = self.test_client.post('/api/v2/auth/signin', content_type= 'application/json',
    #                               data = json.dumps(items))
    #     self.assertEqual(200,response.status_code)
    #     self.assertTrue({'created user','message'},True)
           
       
    # def test_empty_firstname_error(self):
    #     self.user["first_name"] = " "
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)
    
    # def test_firstname_integer_error(self):
    #     self.user["first_name"] = 123
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_lastname_error(self):
    #      self.user["last_name"] = " "
    #      response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #      self.assertEqual(400,response.status_code)

    # def test_lastname_integer_error(self):
    #     self.user["last_name"] = 456
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_othernames_error(self):
    #     self.user["other_names"] = " "
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_othernames_integer_error(self):
    #     self.user["other_names"] = 123
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_email_error(self):
    #     self.user["email"] = " "
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_email_integer_error(self):
    #     self.user["email"] = 123456
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_email_syntax_error(self):
    #     self.user["email"] = "joangmail"
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_password_error(self):
    #     self.user["password"] = " "
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_password_integer_error(self):
    #     self.user["password"] = 123456
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_password_length_error(self):
    #     self.user["password"] = "abcdefghijklmnopqrst"
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_username_integer_error(self):
    #     self.user["username"] = 1234
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_username_error(self):
    #     self.user["username"] = " "
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    # def test_empty_phonenumber_error(self):
    #     self.user["phone_number"] = " "
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)
    
    # def test_phonenumber_integer_error(self):
    #     self.user["phone_number"] = 345678
    #     response = self.test_client.post('/api/v2/auth/signup', content_type= 'application/json', data = json.dumps(self.user))
    #     self.assertEqual(400,response.status_code)

    

        





