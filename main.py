from data_manager import load_obs
def main():
    try:
        observations=load_obs("data/observations.csv")
    except FileNotFoundError:
        print("Could not find data/observations.csv. Run the program from the project folder.")
        return
    except (KeyError,ValueError) as error:
        print("There is a problem with the CSV file:", error)
        return
    print("WildTrack Analyzer")
    print("Loaded",len(observations),"observations")
    while True:
        print()
        print("1. View observations")
        print("2. Exit")
        choice=input("Choose an option: ")
        if choice=="1":
            print(f"{'ID':<4}{'Species':<22}{'Location':<22}{'Date':<12}{'Count':<7}Details")
            for obs in observations:
                print(f"{obs.id:<4}{obs.species:<22}{obs.location:<22}{obs.date:<12}{obs.count:<7}{obs.details()}")
        elif choice=="2":
            print("Thank You for Visiting Us.Goodbye")
            break
        else:
            print("Invalid option")
if __name__=="__main__":
    main()
