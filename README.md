# Infotrixs

Contact Management System allows users to manage their contacts by performing various operations such as:  

Adding a contact
Searching for a contact
Updating contact information
Deleting a contact

The code utilizes JSON file handling to store the contact information persistently. It includes functions to load contacts from a 'contacts.json' file, as well as to save the updated contact list to the same file.

The add_contact() function prompts the user to input the contact's name, phone number, and email address. It then creates a dictionary representing the contact and appends it to the existing list of contacts. The updated contact list is saved using the save_contacts() function.

The search_contact() function allows the user to search for contacts based on a provided name. It performs a case-insensitive search and displays the matching results, including the contact's name, phone number, and email address.

The update_contact() function enables the user to update the information of a specific contact. It prompts the user to enter the name of the contact to be updated, searches for a matching contact, and allows the user to modify the contact's phone number and email address. The updated contact list is saved using the save_contacts() function.

The delete_contact() function provides the functionality to delete a contact. It prompts the user to input the name of the contact to be deleted, searches for a matching contact, and removes it from the contact list. The updated contact list is saved using the save_contacts() function.

The print_menu() function displays the options available in the Contact Management System, allowing the user to navigate and perform different operations.

