import datetime
class Incidents():
    def __init__(self,incident_id,created_on,created_by,location,status,
                 images,videos,comment):
      self.incident_id = incident_id
      self.created_on = datetime.datetime.now()
      self.created_by = created_by
      self.location = location
      self.status = status
      self.images = images
      self.videos = videos
      self.comment = comment

class Redflags(Incidents):
    def __init__(self,incident_id,created_on,created_by,location,status,
                         images,videos,comment):
      Incidents.__init__(self,incident_id,created_on,created_by,location,status,
                         images,videos,comment)
      
      self.incident_type = 'redflag'

    def to_dict_redflag(self):
      flags = {

         "incident_id":self.incident_id,
         "redflag_id": self.redflag_id,
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

class Interventions(Incidents):
    def __init__(self,incident_id,created_on,created_by,location,status,
                 images,videos,comment):
        Incidents.__init__(self,incident_id,created_on,created_by,location,status,
                 images,videos,comment)
        self.incident_type = 'intervention'

    def to_dict_intervention(self):
      intervene = {
         "incident_id":self.incident_id,
         "intervention_id" : self.intervention_id,
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
