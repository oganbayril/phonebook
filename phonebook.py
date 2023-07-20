import json
import os

class Phonebook:
    def __init__(self):
        self.contacts = {}
        
    # Getting the data from json and if json file doesn't exist creates it
    def getting_data(self):
        if os.path.exists("contacts.json") and os.path.getsize("contacts.json") > 0:
            with open("contacts.json", "r") as f:
                self.contacts = json.load(f)
        else:
            open("contacts.json", "w")
    
    # Adding the data to json        
    def adding_to_json(self):
        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f, indent=2)
        
    # Adding a new contact (Duplicate names aren't accepted)
    def add(self, name, number):
        if name in self.contacts.keys():
            print(f"You already have {name} in contacts, please enter a new name.\n")
            return choice
        
        self.contacts[name] = number
        print(f"{name} has been added to phonebook with phone number {number}.\n")
    
    # Removing an existing contact
    def remove(self, name):
        if name not in self.contacts:
            print(f"{name} isn't in contracts.\n")
            return choice
        
        self.contacts.pop(name)
        print(f"{name} has been removed from the phonebook.\n")
    
    # Updating name or phone number of an existing contact
    def update(self, name):
        if name not in self.contacts:
            print(f"{name} isn't in contacts.\n")
            return choice
        
        update = input("Type 'name' to update the name, type 'number' to update the phone number: ").lower()
        if update == "name": 
            new_name = input("New name: ")
            self.contacts[new_name] = self.contacts.pop(name)
            print(f"{name} has been changed to {new_name}.\n")
            
        elif update == "number":
            new_number = input("New number: ")
            self.contacts[name] = new_number
            print(f"{name}'s phone number has been changed to {new_number}.\n")
            
        else:
            print("Please enter a valid choice.\n")
    
    # Searching a single person by their name and showing their phone number
    def search(self):
        if name in self.contacts:
            print(f"The phone number of {name} is {self.contacts[name]}.\n")
        else:
            print(f"{name} is not in the phonebook.\n")
    
    # Viewing all contacts in the phonebook
    def view_all(self):
        # Sorting the phonebook by alphabetical order of names
        names = list(self.contacts.keys())
        names.sort()
        sorted_names = {i: self.contacts[i] for i in names}
        
        # Printing every contact in the sorted version of phonebook (name : phone number)
        for key, value in sorted_names.items():  
            print(key, ":", value)
        print(" ")
        
    
    

phonebook = Phonebook()
phonebook.getting_data()

while True:
    print("1. Add a contact")
    print("2. Remove a contact")
    print("3. Update a contact")
    print("4. Search for a contact")
    print("5. View all contacts")
    print("6. Quit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please Enter integers only.\n")
        continue
    
    print(" ")

    if choice == 1: 
        name = input("Name of the person you want to add: ")
        number = input("Phone number of the person you want to add: ")  
        phonebook.add(name, number)
        
    elif choice == 2: 
        name = input("Name of the person you want to remove: ")
        phonebook.remove(name)
        
    elif choice == 3: 
        name = input("Name of the person you want to update: ")
        phonebook.update(name)
    
    elif choice == 4: 
        name = input("Name of the person you want to search: ")
        phonebook.search()
            
    elif choice == 5:
        phonebook.view_all()
        
    elif choice == 6:
        phonebook.adding_to_json()
        print("Quitting.")
        break
    
    else:
        print("Invalid choice, please try again.")