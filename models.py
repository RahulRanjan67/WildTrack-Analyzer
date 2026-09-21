class ob:
    def __init__(self,id,species,location,date,count):
        self.id=id
        self.species=species
        self.location=location
        self.date=date
        self.count=count
    def details(self):
        return "No extra details"
class mammalobs(ob):
    def __init__(self,id,species,location,date,count,weight_kg):
        super().__init__(id,species,location,date,count)
        self.weight_kg=weight_kg
    def details(self):
        return f"Weight: {self.weight_kg} kg"
class birdobs(ob):
    def __init__(self,id,species,location,date,count,wingspan_cm):
        super().__init__(id,species,location,date,count)
        self.wingspan_cm=wingspan_cm
    def details(self):
        return f"Wingspan: {self.wingspan_cm} cm"
class reptileobs(ob):
    def __init__(self,id,species,location,date,count,length_m):
        super().__init__(id,species,location,date,count)
        self.length_m=length_m
    def details(self):
        return f"Length: {self.length_m} m"
