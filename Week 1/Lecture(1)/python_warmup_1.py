name = input("Enter your name: ") # grabs the user's name
birth_month = input("Enter your birth month: ") # grabs the users birth month

print(f"Hello, {name}!!!") # prints a message saying hello to the uer

print(f"There are {len(name)} letters in your name!")

if birth_month.lower() == "august": # checks the birth month variable to see if their month is august
    print("Happy birth month!!")

