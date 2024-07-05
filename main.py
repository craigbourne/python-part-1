contacts = {}
deleted_contacts = {}  # dictionary to store deleted contacts

def add_contact():
    while True:
        # collect name and number
        name = input("Contact name: ")
        phone = input("Phone number: ")

        # check first name of contact. Adding "Tom Jones" should output "Tom"
        first_name = name.split(" ")[0]
        print(f"\nFirst name of contact is {first_name}")

        # contacts key is name and value is phone number
        contacts[name] = phone
        print(contacts)

        # break out of loop asking for new contact
        if input("\nWould you like to add another contact? (y/n) : ").lower() != 'y':
            break

def search_contact():
    # checks if contact list is empty
    if contacts == {}:
        print("Contacts list is empty.")
    else:
        while True:
            # prints list of current contacts
            print("\nCurrent contact list:")
            for contact in contacts.keys():
                print(contact)

            # asks for contact to search
            contact_name = input("\nWhich contact from the list above would you like to view? ")

            # checks if contact exists in the list
            if contact_name in contacts:
                print(f"\nContact details for {contact_name}:")
                print(f"Name: {contact_name}\nNumber: {contacts[contact_name]}")
                
                # asks user to continue or break out of loop
                if input("\nSearch contacts again? (y/n) ").lower() != 'y':
                    break
            else: 
                print("\nNo such contact exists.")

def delete_contact():
    # checks if contact list has any data to delete
    if contacts == {}:
        print("\nContacts list is empty. Nothing to delete.")
    else:
        while True:
            # prints list of current contacts
            print("\nCurrent contact list:")
            for contact in contacts.keys():
                print(contact)
            
            # ask user for a contact to delete
            delete_contact = input("\nWhich contact would you like to delete? ")

            # check if name exists in contacts dict
            if delete_contact in contacts:
                # confirm deletion
                if input(f"Are you sure you want to delete {delete_contact}? (y/n) ").lower() == 'y':
                    # store deleted contact
                    deleted_contacts[delete_contact] = contacts[delete_contact]
                    # delete the contact and show the remaining contacts
                    del contacts[delete_contact]
                    print("\nContact deleted.")
                    print("\nCurrent contact list:")
                    for contact in contacts.keys():
                        print(contact)
                
                # check if user wants to continue deleting contacts, if not then exit the delete functionality
                if input("\nWould you like to delete another contact? (y/n) ").lower() != 'y':
                    break
                
                # check again that contacts has data to delete
                if not contacts:
                    print("Contacts list is empty. Nothing to delete.")
                    break
            # otherwise tell user name is not in contacts list
            else: 
                print("\nThis contact cannot be deleted as it does not exist.")

def restore_contact():
    if deleted_contacts == {}:
        print("No deleted contacts to restore.")
    else:
        while True:
            # prints list of deleted contacts
            print("\nDeleted contact list:")
            for contact in deleted_contacts.keys():
                print(contact)

            # asks for contact to restore
            restore_contact = input("\nWhich contact from the list above would you like to restore? ")

            # checks if contact exists in the deleted contacts list
            if restore_contact in deleted_contacts:
                # restore the contact
                contacts[restore_contact] = deleted_contacts[restore_contact]
                del deleted_contacts[restore_contact]
                print(f"\nContact {restore_contact} restored.")
                break
            else:
                print("\nNo such deleted contact exists.")

def sort_contacts():
    if contacts == {}:
        print("Contacts list is empty so cannot be sorted.")
    else:
        while True:
            # ask the user if they would like to sort alphabetically
            sort_prompt = input("\nWould you like to sort contacts alphabetically? (y/n) ").lower()
            
            # if so, sort the contacts alphabetically by the key name and print to terminal to check sort has happened
            if sort_prompt == 'y':
                sorted_contacts = dict(sorted(contacts.items()))
                print("\nSorted contacts: ")
                for contact in sorted_contacts.items():
                    print(contact)
                # replace original contacts dictionary with sorted one
                contacts.clear()
                contacts.update(sorted_contacts)
                break
            else:
                break

# ask the user what they want to do
def user_choice():
    while True:
        choice = int(input("\nWhat would you like to do? \n[0] add contact \n[1] search contact \n[2] sort contacts \n[3] delete contact \n[4] restore contact \n"))

        if choice in (0, 1, 2, 3, 4):
            if choice == 0: 
                add_contact()
            elif choice == 1: 
                search_contact()
            elif choice == 2: 
                sort_contacts()
            elif choice == 3: 
                delete_contact()
            elif choice == 4: 
                restore_contact()
        else:
            print("That choice is not valid, please try again.")

user_choice()
