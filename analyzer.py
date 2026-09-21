import numpy as np
def getcounts(observations):
    return np.array([obs.count for obs in observations])
def totalobs(counts):
    return len(counts)
def totalanimals(counts):
    return int(np.sum(counts))
def avgcount(counts):
    return float(np.mean(counts))
def mediancount(counts):
    return float(np.median(counts))
def mincount(counts):
    return int(np.min(counts))
def maxcount(counts):
    return int(np.max(counts))
def stdcount(counts):
    return float(np.std(counts))
def totalspecies(observations):
    counts=getcounts(observations)
    species=np.array([obs.species for obs in observations])
    totals={}
    for name in np.unique(species):
        totals[str(name)]=int(counts[species==name].sum())
    return totals
def totalloc(observations):
    counts=getcounts(observations)
    locations=np.array([obs.location for obs in observations])
    totals={}
    for name in np.unique(locations):
        totals[str(name)]=int(counts[locations==name].sum())
    return totals
def search_species(observations,text):
    results=[]
    for obs in observations:
        if text.lower() in obs.species.lower():
            results.append(obs)
    return results
def search_location(observations,text):
    results=[]
    for obs in observations:
        if text.lower() in obs.location.lower():
            results.append(obs)
    return results
def filterspecies(observations,name):
    results=[]
    for obs in observations:
        if obs.species==name:
            results.append(obs)
    return results
def filterloc(observations,name):
    results=[]
    for obs in observations:
        if obs.location==name:
            results.append(obs)
    return results
def summary(observations):
    counts=getcounts(observations)
    text=f"Total observations: {totalobs(counts)}\n"
    text+=f"Total animals: {totalanimals(counts)}\n"
    text+=f"Average animals per observation: {avgcount(counts):.2f}\n"
    text+=f"Median animals per observation: {mediancount(counts):.1f}\n"
    text+=f"Minimum in one observation: {mincount(counts)}\n"
    text+=f"Maximum in one observation: {maxcount(counts)}\n"
    text+=f"Standard deviation: {stdcount(counts):.2f}\n"
    text+="\nAnimals per species:\n"
    for name,total in totalspecies(observations).items():
        text+=f"{name:<22}{total}\n"
    text+="\nAnimals per location:\n"
    for name,total in totalloc(observations).items():
        text+=f"{name:<22}{total}\n"
    return text