class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            'Name': name,
            'Phone Number': phone_number,
            'Email': email,
            'Address': address
        }
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(f"Name: {contact['Name']}, Phone Number: {contact['Phone Number']}")

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone Number']:
                results.append(contact)
        return results

    def update_contact(self, name, new_phone_number, new_email, new_address):
        for contact in self.contacts:
            if contact['Name'].lower() == name.lower():
                contact['Phone Number'] = new_phone_number
                contact['Email'] = new_email
                contact['Address'] = new_address
                print(f"Contact '{name}' updated successfully!")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['Name'].lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print(f"Contact '{name}' not found.")

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == '2':
            contact_book.view_contact_list()
        elif choice == '3':
            search_term = input("Enter Name or Phone Number to search: ")
            results = contact_book.search_contact(search_term)
            if results:
                print("\nSearch Results:")
                for contact in results:
                    print(contact)
            else:
                print("No matching contacts found.")
        elif choice == '4':
            name = input("Enter Name of the contact to update: ")
            new_phone_number = input("Enter new Phone Number: ")
            new_email = input("Enter new Email: ")
            new_address = input("Enter new Address: ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == '5':
            name = input("Enter Name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
