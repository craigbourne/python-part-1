contacts = {}

def add_contact():
    while True:
        # collect name and number
        name = input("Contact name: ")
        phone = input("Phone number: ")

        # contacts key is name and value is phone number
        contacts[name] = phone
        print(contacts)

        # break out of loop asking for new contact
        if input("Would you like to add another contact? (y/n) : ").lower() != 'y':
            break

def search_contact():
    #checks if content list is empty
    if contacts == {}: print("Contacts list is empty.")
    else:
        while True:
            #prints list of current contacts
            print("\nCurrent contact list:")
            for contact in contacts.keys():
                print(contact)

            # asks for contact to search
            contact_name = input("\nWhich contact from the list above would you like to view? ")

            # checks if contact exists in the list
            if contact_name in contacts:
                print(f"\nContact details for {contact_name}:")

                for contact in contacts[contact_name]: 
                    # prints desired contact details
                    print(f"Name: {contact_name}\nNumber: {contacts[contact_name]}")
                # asks user to continue or break out of for loop
                if input("\nSearch contacts again? (y/n) ").lower() != 'y': break
                
            else: 
                    print("\nNo such contact exists.")

def delete_contact():
    #checks if content list has any data to delete
    if contacts == {}: print("\nContacts list is empty. Nothing to delete.")
    else:
        while True:
            #prints list of current contacts
            print("\nCurrent contact list:")
            for contact in contacts.keys():
                print(contact)
            
            # Ask user for a contact to delete
            delete_contact = input("\nWhich contact would you like to delete? ")

            #check if name exists in contacts dict
            if delete_contact in contacts:
                # if it does exist delete the contact and show the remaining contacts
                del contacts[delete_contact]
                print("\nContact deleted.")
                print("\nCurrent contact list:")
                for contact in contacts.keys():
                    print(contact)

                # Check if user wants to continue deleting contacts, if not then exit the delete functionality
                if input("\nWould you like to delete another contact? (y/n) ").lower() != 'y': break
                # Check again that contacts has data to delete
                if contacts == {}: 
                    print("Contacts list is empty. Nothing to delete.")
                    break
            #Otherwise tell user name is not in contacts list
            else: 
                print("\nThis contact cannot be deleted as it does not exist.")

# ask the user what they want to do
def user_choice():
    while True:
        choice = int(input("\n What would you like to do? \n[0] add contact \n[1] search contact \n[2] delete contact \n"))

        if choice in (0,1,2):
            if choice == 0: add_contact()
            elif choice == 1: search_contact()
            else: delete_contact()
        else:
            print("That choice is not valid, please try again.")

user_choice()