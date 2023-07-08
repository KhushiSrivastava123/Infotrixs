import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

def search_contact():
    query = input("Enter the name to search: ")
    results = []
    for contact in contacts:
        if query.lower() in contact['name'].lower():
            results.append(contact)
    if results:
        print("Search results:")
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
    else:
        print("No matching contacts found.")

def update_contact():
    query = input("Enter the name to update: ")
    found = False
    for contact in contacts:
        if query.lower() == contact['name'].lower():
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            contact['phone'] = phone
            contact['email'] = email
            save_contacts(contacts)
            print("Contact updated successfully!")
            found = True
            break
    if not found:
        print("Contact not found.")

def delete_contact():
    query = input("Enter the name to delete: ")
    found = False
    for contact in contacts:
        if query.lower() == contact['name'].lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            found = True
            break
    if not found:
        print("Contact not found.")

def print_menu():
    print("Contact Management System")
    print("-------------------------")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Exit")

contacts = load_contacts()

while True:
    print_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
