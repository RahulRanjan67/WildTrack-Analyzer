import csv
from models import mammalobs,birdobs,reptileobs
def load_obs(filename):
    observations=[]
    with open(filename, newline="") as file:
        reader=csv.DictReader(file)
        for row in reader:
            id=int(row["id"])
            count=int(row["count"])
            value=float(row["specific_value"])
            if row["type"]=="mammal":
                obs=mammalobs(id,row["species"],row["location"],row["date"],count,value)
            elif row["type"]=="bird":
                obs=birdobs(id,row["species"],row["location"],row["date"],count,value)
            elif row["type"] == "reptile":
                obs=reptileobs(id, row["species"],row["location"],row["date"],count,value)
            else:
                raise ValueError("Unknown type: "+row["type"])
            observations.append(obs)
    return observations
