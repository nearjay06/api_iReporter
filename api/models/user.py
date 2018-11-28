import datetime

class Users:
    def __init__(self, user_id, first_name, last_name, other_names, email, phone_number, username,
                 registered,isAdmin):
      self.user_id = user_id
      self.first_name = first_name
      self.last_name = last_name
      self.other_names = other_names
      self.email = email
      self.phone_number = phone_number
      self.username = username
      self.registered = datetime.datetime.now()
      self.isAdmin = isAdmin


    def user_dict(self):
      users = {
             "user_id":self.user_id,
             "first_name":self.first_name,
             "last_name":self.last_name,
             "other_names":self.other_names,
             "email":self.email,
             "phone_number":self.phone_number,
             "username":self.username,
             "registered":self.registered,
             "isAdmin":self.isAdmin
        }

      return users