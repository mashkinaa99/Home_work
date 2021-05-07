import json

a = 'alena.json'


def add_person():
    with open(a) as alenka:
        phone_book = json.load(alenka)

    person = {}
    person['name'] = input('enter name: ')
    person['last_name'] = input('enter last name: ')
    person['phone_number'] = input('enter phone number: ')
    person['city'] = input('enter city: ')
    person['state'] = input('enter state: ')

    phone_book["persons"].append(person)

    with open(a, 'w') as phone_book_file:
        json.dump(phone_book, phone_book_file)

    print('Contact added!\n')


def search_person_name():
    name = input('Enter a name to search: ')
    right = False
    with open(a) as f:
        search_file = json.load(f)

    for contact in search_file['persons']:
        if contact['name'] == name.title():
            print(contact)
            right = True

    if right:
        print('Contact found!\n')
    else:
        print('Contact not found\n')


def search_person_last_name():
    last_name = input('Enter a last name to search: ')
    right = False
    with open(a) as f:
        search_file = json.load(f)

    for contact in search_file['persons']:
        if contact['last_name'] == last_name.title():
            print(contact)
            right = True

    if right:
        print('Contact found!\n')
    else:
        print('Contact not found\n')


def search_person_full_name():
    full_name = input('Enter a full name to search: ')
    right = False
    with open(a) as f:
        search_file = json.load(f)

    for contact in search_file['persons']:
        b = contact['name'] + ' ' + contact['last_name']
        if b == full_name.title():
            print(contact)
            right = True

    if right:
        print('Contact found!\n')
    else:
        print('Contact not found\n')


def search_person_phone():
    phone_number = input('Enter the phone number in the format (380) to search: ')
    right = False
    with open(a) as f:
        search_file = json.load(f)

    for contact in search_file['persons']:
        if contact['phone_number'] == phone_number.title():
            print(contact)
            right = True
            break

    if right:
        print('Contact found!\n')
    else:
        print('Contact not found\n')


def search_person_location():
    city = input('Enter city or state name: ')
    right = False
    with open(a) as f:
        search_file = json.load(f)

    for contact in search_file['persons']:
        if contact['city'] == city.title() or contact['state'] == city.title():
            print(contact)
            right = True

    if right:
        print('Contact found!\n')
    else:
        print('Contact not found\n')


def del_person():
    phone_number = input('Enter the phone number in the format (380) to delete: ')
    right = False
    with open(a) as f:
        search_file = json.load(f)

    for contact_id, contact in enumerate(search_file['persons']):
        if contact['phone_number'] == phone_number.title():
            del search_file['persons'][contact_id]
            right = True

    with open(a, 'w') as f:
        json.dump(search_file, f)

    if right:
        print('Contact deleted!\n')
    else:
        print('Contact not found\n')


def upd_person():
    phone_number = input('Enter the phone number (format 380) you want to change the details of: ')
    with open(a) as f:
        search_file = json.load(f)

    for contact in search_file['persons']:
        if contact['phone_number'] == phone_number.title():
            print('Commands for changing contact data: ',
                  contact,
                  'What exactly do you want to edit?',
                  '1. Change name',
                  '2. Change last name',
                  '3. Change phone number',
                  '4. Change city',
                  '5. Change state',
                  '6. Change all',
                  sep='\n')
            edit_response = input('Here is the data for this contact: ')

            if edit_response == '1':
                name_edit_response = input('Enter new name: ')
                contact['name'] = name_edit_response.title()
                print('Name changed!\n')

            if edit_response == '2':
                last_name_edit_response = input('Enter new last name: ')
                contact['last_name'] = last_name_edit_response.title()
                print('Last name changed!\n')

            if edit_response == '3':
                phone_number_edit_response = input('Enter new phone number: ')
                contact['phone_number'] = phone_number_edit_response.title()
                print('Phone number changed!\n')

            if edit_response == '4':
                city_edit_response = input('Enter new city: ')
                contact['city'] = city_edit_response.title()
                print('City changed!\n')

            if edit_response == '5':
                state_edit_response = input('Enter new state: ')
                contact['state'] = state_edit_response.title()
                print('State changed!\n')

            if edit_response == '6':
                contact['name'] = input('Enter new name: ').title()
                contact['last_name'] = input('Enter new last name: ').title()
                contact['phone_number'] = input('Enter new phone number: ').title()
                contact['city'] = input('Enter new city: ').title()
                contact['state'] = input('Enter new state: ').title()
                print('all contact details have been changed!\n')

    with open(a, 'w') as f:
        json.dump(search_file, f)


while True:
    print('1. Add new entries',
          '2. Search by name',
          '3. Search by last name',
          '4. Search by full name',
          '5. Search by phone number',
          '6. Search by city or state',
          '7. Delete entry for this phone number',
          '8. Update a record for a given telephone number',
          '9. Exit the program',
          sep='\n')

    i = input('What do you want to do (enter a number): ')

    if i == '1':
        add_person()

    elif i == '2':
        search_person_name()

    elif i == '3':
        search_person_last_name()

    elif i == '4':
        search_person_full_name()

    elif i == '5':
        search_person_phone()

    elif i == '6':
        search_person_location()

    elif i == '7':
        del_person()

    elif i == '8':
        upd_person()

    elif i == '9':
        break
