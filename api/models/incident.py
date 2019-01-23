import datetime

redflags_list = []
interventions_list = []
class Incidents():
    
    def __init__(self,created_by,incident_type,location,status,
                 images,videos,comment):
      
      
      self.created_on = datetime.datetime.now()
      self.created_by = created_by
      self.incident_type = incident_type
      self.location = location
      self.status = status
      self.images = images
      self.videos = videos
      self.comment = comment

    def to_dict_redflag(self):
      flags = {

         "incident_id":self.incident_id,
         "created_on": self.created_on,
         "created_by": self.created_by,
         "incident_type": self.incident_type,
         "location": self.location,
         "status": self.status,
         "images": self.images,
         "videos": self.videos,
         "comment": self.comment

       }

      return flags

    def to_dict_intervention(self):
      intervene = {
         "incident_id":self.incident_id,
         "created_on": self.created_on,
         "created_by": self.created_by,
         "incident_type": self.incident_type,
         "location": self.location,
         "status": self.status,
         "images": self.images,
         "videos": self.videos,
         "comment": self.comment

       }

      return intervene

class Redflags(Incidents):
    def __init__(self,incident_id,created_on,created_by,incident_type,location,status,
                         images,videos,comment):
      Incidents.__init__(self,incident_id,created_on,created_by,incident_type,location,status,
                         images,videos,comment)
    
class Interventions(Incidents):
    def __init__(self,incident_id,created_on,created_by,incident_type,location,status,
                 images,videos,comment):
        Incidents.__init__(self,incident_id,created_on,created_by,incident_type,location,status,
                 images,videos,comment)
        





