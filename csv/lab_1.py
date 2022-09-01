import csv
import re

class PhoneContact:
    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone


class Phone:
    def __init__(self) -> None:
        self.contacts = []

    def load_contacts_from_csv(self, filename):
        fieldnames = ['Name', 'Phone']
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                phone_contact = PhoneContact(row['Name'], row['Phone'])
                self.contacts.append(phone_contact)
    
    def search_contacts(self):
        search = input("Enter a contact name: ")
        found = False
        for phone_contact in self.contacts:
            if re.search(search, phone_contact.name, re.IGNORECASE):
                found = True
                print(f"Name: {phone_contact.name}, Phone: {phone_contact.phone}")
        if not found:
            print('No contacts found')


phone = Phone()
phone.load_contacts_from_csv('contacts.csv')
phone.search_contacts()