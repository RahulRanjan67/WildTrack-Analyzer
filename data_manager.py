import csv
from datetime import datetime
from models import mammalobs,birdobs,reptileobs
from analyzer import summary
def loadobs(filename):
    observations=[]
    with open(filename,newline="") as file:
        reader=csv.DictReader(file)
        for row in reader:
            id=int(row["id"])
            count=int(row["count"])
            value=float(row["specific_value"])
            if row["type"]=="mammal":
                obs=mammalobs(id,row["species"],row["location"],row["date"],count,value)
            elif row["type"]=="bird":
                obs=birdobs(id,row["species"],row["location"],row["date"],count,value)
            elif row["type"]=="reptile":
                obs=reptileobs(id,row["species"],row["location"],row["date"],count,value)
            else:
                raise ValueError("Unknown type: "+row["type"])
            observations.append(obs)
    return observations
def addobs(observations,species,type,location,date,count,value):
    id=max([obs.id for obs in observations])+1
    if type=="mammal":
        obs=mammalobs(id,species,location,date,count,value)
    elif type=="bird":
        obs=birdobs(id,species,location,date,count,value)
    else:
        obs=reptileobs(id,species,location,date,count,value)
    observations.append(obs)
    return obs
def saveobs(filename,observations):
    with open(filename,"w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["id","species","type","location","date","count","specific_value"])
        for obs in observations:
            if isinstance(obs,mammalobs):
                kind="mammal"
                value=obs.weight_kg
            elif isinstance(obs,birdobs):
                kind="bird"
                value=obs.wingspan_cm
            else:
                kind="reptile"
                value=obs.length_m
            writer.writerow([obs.id,obs.species,kind,obs.location,obs.date,obs.count,value])
def save(observations,filename):
    with open(filename,"w") as file:
        file.write("WildTrack Analyzer Report\n")
        file.write("Generated on "+datetime.now().strftime("%Y-%m-%d %H:%M")+"\n\n")
        file.write(summary(observations))