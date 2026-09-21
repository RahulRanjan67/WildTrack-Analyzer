from data_manager import loadobs,addobs,saveobs,save
from analyzer import summary,search_species,search_location,filterspecies,filterloc
from utils import getint,positive,date,text,type,choose
csv_file="data/observations.csv"
def showobs(observations):
    if len(observations)==0:
        print("No observations found.")
        return
    print("Showing",len(observations),"observation(s)")
    print(f"{'ID':<4}{'Species':<22}{'Location':<22}{'Date':<12}{'Count':<7}Details")
    for obs in observations:
        print(f"{obs.id:<4}{obs.species:<22}{obs.location:<22}{obs.date:<12}{obs.count:<7}{obs.details()}")
def save_to_csv(observations):
    try:
        saveobs(csv_file,observations)
    except OSError:
        print("Could not save the CSV file. Make sure it is not open in another program.")
        return False
    print("Saved",len(observations),"observations to",csv_file)
    return True
def addob(observations):
    print("Add a new observation")
    species=text("Species name: ")
    for obs in observations:
        if obs.species.lower()==species.lower():
            species=obs.species
    animal_type=type()
    location=text("Location: ")
    for obs in observations:
        if obs.location.lower()==location.lower():
            location=obs.location
    date=date("Date (YYYY-MM-DD): ")
    count=getint("Number of animals seen: ",1,10000)
    if animal_type=="mammal":
        value=positive("Weight in kg: ")
    elif animal_type=="bird":
        value=positive("Wingspan in cm: ")
    else:
        value=positive("Length in m: ")
    newobs=addobs(observations,species,animal_type,location,date,count,value)
    print("Observation",newobs.id,"added:",newobs.species,"-",newobs.details())
    answer=input("Save all observations to the CSV file now? (y/n): ")
    if answer.lower()=="y":
        return save_to_csv(observations)
    print("Not saved yet. The new observation only lives in memory while the program runs.")
    return False
def main():
    try:
        observations=loadobs(csv_file)
    except FileNotFoundError:
        print("Could not find data/observations.csv. Run the program from the project folder.")
        return
    except (KeyError,ValueError) as error:
        print("There is a problem with the CSV file:",error)
        return
    if len(observations)==0:
        print("The CSV file has no observations.")
        return
    print("  Welcome to WildTrack Analyzer, wildlife enthusiasts!")
    print()
    print("WildTrack Analyzer is a small tool for exploring wildlife")
    print("sightings. Browse mammal, bird and reptile observations,")
    print("search or filter them, check quick statistics, add your")
    print("own sightings and save a report of your findings.")
    print("The sample observations that come with it are made up.")
    print("Happy tracking!")
    print("Loaded",len(observations),"observations")
    saved=True
    while True:
        print()
        print("WildTrack Analyzer")
        print("1. View observations")
        print("2. Search observations")
        print("3. Filter by species")
        print("4. Filter by location")
        print("5. View statistics")
        print("6. Add observation")
        print("7. Save report")
        print("8. Exit")
        choice=input("Choose an option: ").strip()
        if choice=="1":
            showobs(observations)
        elif choice=="2":
            field=choose("Search by:",["Species","Location"])
            searchtext=text("Enter the "+field.lower()+" to search for: ")
            if field=="Species":
                results=search_species(observations,searchtext)
            else:
                results=search_location(observations,searchtext)
            showobs(results)
        elif choice=="3":
            names=sorted(set([obs.species for obs in observations]))
            name=choose("Species in the records:",names)
            showobs(filterspecies(observations,name))
        elif choice=="4":
            names=sorted(set([obs.location for obs in observations]))
            name=choose("Locations in the records:",names)
            showobs(filterloc(observations,name))
        elif choice=="5":
            print("Statistics")
            print(summary(observations))
        elif choice=="6":
            saved=addob(observations)
        elif choice=="7":
            try:
                save(observations,"reports/wildtrack_report.txt")
                print("Report saved to reports/wildtrack_report.txt")
            except OSError:
                print("Could not save the report. Make sure the reports folder exists.")
        elif choice=="8":
            if not saved:
                answer=input("Some observations are not saved to the CSV file yet. Save them now? (y/n): ")
                if answer.lower()=="y":
                    save_to_csv(observations)
            print("Thank You for Visiting Us.Goodbye")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 8.")
if __name__=="__main__":
    main()