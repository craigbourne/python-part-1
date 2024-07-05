## README containing a description of the implementation and instructions on how to execute the code

The application I have chosen to build for the assignment is a phone book, which could evolve into a contact book with the collection of more data.

The application is a simple Python 3 program that enables users to manage a list of contacts. The application has the requested functionality to add, search, sort and delete contacts. Plus the additional option of being able to restore previously deleted contacts.

The application uses the Python dictionary data structure to store, delete and restore contacts, which means that data is cleanly managed and easily accessed.

### Requirements

The only requirement to use and run the application is Python 3.

### Running the Application in an IDE

1. If you are using the application in an IDE like Visual Studio Code, please ensure that you have [Python 3 installed on your machine](https://docs.python.org/3/using/index.html).

2. Ensure that the provided code is saved to a Python file. I have provided a file called **contact_book.py**, so you do not need to create your own file.

3. Open a terminal or command prompt window.

4. Navigate to the directory where **contact_book.py** is located on your machine.

5. Run the application with Python, using the command: 
```sh
   python contact_book.py
```

### Running the Application in Jupyter Notebook

1. If you are using the application in Jupyter Notebook, then the application will run in the browser and the installation of Python on your machine is not necessary.

2. Navigate to the following link to use the application in Jupyter Notebook: [https://anaconda.cloud/share/notebooks/b9507677-3574-4030-a918-6390dbb4405d/overview](https://anaconda.cloud/share/notebooks/b9507677-3574-4030-a918-6390dbb4405d/overview).

3. Here, you can either open the application in Anaconda Cloud or download a copy of the code to your machine. If you download, then a) check your Downloads folder, b) open Anaconda Local Notebooks, and c) drag the file to File Management.

4. When opening in Anaconda Cloud, you will need to sign up for an account and then select the option to 'Open in a Cloud Notebook'.

5. Next, you will be inside the application. You can view or edit each code cell or run the application from the top menu bar by selecting 'Run' and then 'Run All Cells'.

### Features and Instructions

**1. Add a Contact**

To add a new contact:

- When prompted with '*What would you like to do?*', begin by entering '0' to add a contact.
- Enter the contact's name when asked for '*Contact name:*'.
- Enter the contact's phone number when asked for '*Phone number:*'.
- The application will display the first name of the contact and show you the current list of contacts.
- You will be asked if you want to add another contact. Enter '*y*' for yes or '*n*' for no.

**2. Searching for a Contact**

To search for a contact:

- When prompted with '*What would you like to do?*', enter '*1*' to search for a contact.
- The application will display the current list of contacts.
- Enter the name on the current list of the contact that you want to view.
- If the contact exists, details associated with the contact will be displayed.
- You will be asked if you want to search for another contact. Enter '*y*' for yes or '*n*' for no.

**3. Sorting Contacts**

To sort contacts alphabetically:

- When prompted with '*What would you like to do?*', enter '*2*' to sort contacts.
- You will be asked if you want to sort the contacts alphabetically. Enter '*y*' for yes or '*n*' for no.
- If you answer yes, the contacts will be sorted alphabetically and displayed, and the original contacts list will be updated so that contacts are organised alphabetically.

**4. Deleting a Contact**

To delete a contact:

- When prompted with '*What would you like to do?*', enter '*3*' to delete a contact.
- The application will first display the current list of contacts.
- Here, you enter the name of the contact you want to delete.
- You will be asked to confirm the deletion. Enter '*y*' for yes or '*n*' for no.
- If confirmed, the contact will be deleted and moved to the deleted_contacts dictionary.
- You will be asked if you want to delete another contact. Enter '*y*' for yes or '*n*' for no.

**5. Restoring a Deleted Contact**

To restore a deleted contact:

- When prompted with '*What would you like to do?*', enter '*4*' to restore a contact.
- The application will display the list of deleted contacts.
- Enter the name of the contact you want to restore.
- If the contact exists in the deleted contacts list, it will be restored to the active contacts list.

### Notes

- The application runs in a loop, allowing an endless chain of operations until the user decides to exit by choosing not to continue.
- Invalid inputs are handled by prompting the user to try again.