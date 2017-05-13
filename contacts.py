# -*- coding: utf-8 -*-
import csv

class Contact:
    """docstring for Contact."""
    def __init__(self, name, phone, email):
        self._name  = name
        self._phone = phone
        self._email = email

class ContactBook:
    """docstring for ContactBook."""
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
             self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if(contact._name == name):
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if(contact._name == name):
                self._print_contact(contact)
                break
            else:
                self._not_found()

    def _save(self):
        with open('contacts.csv', 'wb') as f:
            write = csv.writer(f)
            write.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                write.writerow( (contact._name, contact._phone, contact._email))

    def _print_contact(self, contact):
        print("nombre: {}".format(contact._name))
        print("phone: {}".format(contact._phone))
        print("email: {}".format(contact._email))
        print("---- + ---- + ---- + ---- + ---- +")

    def _not_found(self):
        print("Not found, man.")

def run():

    contact_book = ContactBook()

    with open("contacts.csv","r") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0],row[1],row[2])

    while True:
        command = str(raw_input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            print('añadir contacto')
            name = str(raw_input("Escribe el nombre del contacto: "))
            phone = str(raw_input("Escribe el número de telefono: "))
            email = str(raw_input("Escribe el email de tu contacto: "))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            print('buscar contacto')

        elif command == 'e':
            print('eliminar contacto')

        elif command == 'l':
            print('listado de contactos')
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()
