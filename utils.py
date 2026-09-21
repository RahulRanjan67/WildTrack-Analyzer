from datetime import datetime
def getint(message,low,high):
    while True:
        try:
            number=int(input(message))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if low<=number<=high:
            return number
        print("Please enter a number between",low,"and",high)
def positive(message):
    while True:
        try:
            number=float(input(message))
        except ValueError:
            print("Please enter a number.")
            continue
        if 0<number<100000:
            return number
        print("The number must be greater than 0 and less than 100000.")
def date(message):
    while True:
        try:
            date=datetime.strptime(input(message).strip(),"%Y-%m-%d")
        except ValueError:
            print("Use the format YYYY-MM-DD, for example 2026-05-08.")
            continue
        if date.year<1900 or date>datetime.now():
            print("That date is not realistic. Use a date from 1900 up to today.")
        else:
            return date.strftime("%Y-%m-%d")
def text(message):
    while True:
        text=input(message).strip()
        if text!="":
            return text
        print("This cannot be empty.")
def choose(title,options):
    print(title)
    for i,option in enumerate(options,1):
        print(f"{i}. {option}")
    return options[getint("Enter your choice: ",1,len(options))-1]
def type():
    return choose("Animal type:",["Mammal","Bird","Reptile"]).lower()