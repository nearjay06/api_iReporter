import datetime

class Incidents():
    def __init__(self,incident_id,created_on,created_by,incident_type,location,status,
                 images,videos,comment):
      self.incident_id = incident_id
      self.created_on = datetime.datetime.now()
      self.created_by = created_by
      self.incident_type = incident_type
      self.location = location
      self.status = status
      self.images = images
      self.videos = videos
      self.comment = comment

class Redflags(Incidents):
    def __init__(self,redflag_id,redflag):
      Incidents.__init__(self,incident_id,created_on,created_by,incident_type,location,status,
                 images,videos,comment)
      self.redflag_id = redflag_id
      self.redflag = redflag

    def getRedflag(self,redflag):
      # print("This is a redflag")
      return "{} reporting {}".format(self.incident_type,redflag)

    def issueRedflag(self,draft):
      #print("The redflag is a draft")
      return "{} issuing {}".format(self.status,draft)

    def reportRedflag(self,under_investigation):
      print("This is a redflag")
      return "{} reporting {}".format(self.status,under_investigation)

    def complainRedflag(self,resolved):
      print("This is a redflag")
      return "{} complaining {}".format(self.status,resolved)  

    def alertRedflag(self,rejected):
      print("This is a redflag")
      return "{} alerting {}".format(self.status,rejected)
      
    def create_redflag(self):
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
    def __init__(self,intervention_id,intervention):
        Incidents.__init__(self,incident_id,created_on,created_by,incident_type,location,status,
                 images,videos,comment)
        self.intervention_id = intervention_id
        self.intervention = intervention

    def getIntervention(self,intervention):
      # print("This is an intervention")
      return "{} reporting {}".format(self.incident_type,intervention)

    def issueIntervention(self,draft):
      return "{} issuing {}".format(self.status,draft)

    def reportIntervention(self,under_investigation):
      # print("The intervention is under investigation.")
      return "{} reporting {}".format(self.status,under_investigation)

    def complainIntervention(self,resolved):
      # print("The intervention has been resolved.")
      return "{} complaining {}".format(self.status,resolved)  

    def alertIntervention(self,rejected):
      # print("The intervention has been rejected.")
      return "{} alerting {}".format(self.status,rejected)
      
    def create_intervention(self):
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
