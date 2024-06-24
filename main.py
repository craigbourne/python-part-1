contacts = {}

def add_contact():
    while True:
        # collect name and number
        name = input("Contact name: ")
        phone = input("Phone number: ")

        # contacts key is name and value is phone number
        contacts[name] = phone
        print(contacts)

    # need to break out of loop asking for new contact
        if input("Would you like to add another contact? (y/n) : ").lower() != 'y':
            break

# ask the user what they want to do
def user_choice():
    while True:
        choice = int(input("\n What would you like to do? \n[0] add contact \n[1] search contact \n[2] delete contact \n"))

        if choice in (0,1,2):
            if choice == 0: add_contact()
            elif choice == 1:
                if contacts == {}: print("Contacts list is empty.")
                else:
                    while True:
                        print("\nCurrent contact list:")
                        for contact in contacts.keys():
                            print(contact)

                        contact_name = input("\nWhich contact from the list above would you like to view? ")

                        if contact_name in contacts:
                            print(f"\nContact details for {contact_name}:")

                            for contact in contacts[contact_name]: 
                                # prints desired contact details
                                print(f"Name: {contact_name}\nNumber: {contacts[contact_name]}")
                            # ask to continue or break out of for loop
                            if input("\nSearch contacts again? (y/n) ").lower() != 'y': break
                        else: 
                                print("\nNo such contact exists")

            else:
                # delete contact
                print("delete contact ")
        else:
            print("Invalid Choice. Please Try Again.")

user_choice()