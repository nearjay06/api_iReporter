import datetime

class Users:
    def __init__(self,userid,firstname,lastname,othernames,email,phonenumber,username,registered,isAdmin):
      self.userid = userid
      self.firstname = firstname
      self.lastname = lastname
      self.othernames = othernames
      self.email = email
      self.phonenumber = phonenumber
      self.username = username
      self.registered = datetime.datetime.now()
      self.isAdmin = isAdmin


    def create_users(self):
      uploads = {
             "userid":self.userid,
             "firstname":self.firstname,
             "lastname":self.lastname,
             "othernames":self.othernames,
             "email":self.email,
             "phonenumber":self.phonenumber,
             "username":self.username,
             "registered":self.registered,
             "isAdmin":self.isAdmin
        }

      return uploads