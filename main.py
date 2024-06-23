contacts = {}

# ask the user what they want to do
def user_choice():
    while True:
        choice = int(input("\n What would you like to do? \n[0] add contact \n[1] view contact \n[2] edit a contact \n[3] delete a contact \n"))

        if choice in (0,1,2,3):
            if choice == 0:
                while True:
                    name = input("Contact name: ")
                    phone = input("Phone number: ")
                    # contacts key is name and value is phone number
                    contacts[name] = phone
                    print(contacts)

                    # need to break out of askinf for new contact

            elif choice == 1:
                # view contact
                print("view contact")
            elif choice == 2:
                # edit contact
                print("edit contact ")
            else:
                # delete contact
                print("delete contact ")
        else:
            print("Invalid Choice. Please Try Again.")

user_choice()