import datetime

class Incidents():
    def __init__(self,incidentid,createdOn,createdBy,type,location,status,images,videos,comment):
      self.incidentid = incidentid
      self.createdOn = datetime.datetime.now()
      self.createdBy = createdBy
      self.type = type
      self.location = location
      self.status = status
      self.images = images
      self.videos = videos
      self.comment = comment


    def create_redflag(self):
      flags = {
         "incidentid":self.incidentid,
         "createdOn": self.createdOn,
         "createdBy": self.createdBy,
         "type": self.type,
         "location": self.location,
         "status": self.status,
         "images": self.images,
         "videos": self.videos,
         "comment": self.comment

       }

      return flags
