import datetime

user_list = []
class Users:
    
    def __init__(self, user_id, first_name, last_name, other_names, email, phone_number, username,
                 password,registered):
      self.user_id = user_id
      self.first_name = first_name
      self.last_name = last_name
      self.other_names = other_names
      self.email = email
      self.phone_number = phone_number
      self.username = username
      self.password = password
      self.registered = datetime.datetime.now()
      self.isAdmin = False
 
    def user_dict(self):
      users = {
             "user_id":self.user_id,
             "first_name":self.first_name,
             "last_name":self.last_name,
             "other_names":self.other_names,
             "email":self.email,
             "phone_number":self.phone_number,
             "username":self.username,
             "password":self.password,
             "registered":self.registered,
             "isAdmin":self.isAdmin
        }

      return users

def admin_access():
  for user in user_list:
    if user.isAdmin:
      return True


class Admin(Users):
    def __init__(self, user_id,first_name,last_name, othernames,email,
                 phonenumber, username, password,registered):
      Users.__init__(self, user_id,first_name,last_name, othernames,email,
                 phonenumber, username, password,registered)
      self.isAdmin = True

    
    


if __name__=='__main__':
  joan=Admin(7,'joan','whitre','abs','joan@gmail.com','abcgd','joan','14462681','14/01/2019')
  tom=Users(7,'joan','whitre','abs','joan@gmail.com','abcgd','joan','14462681','14/01/2019')
  print(joan.isAdmin)
  print(tom.isAdmin)