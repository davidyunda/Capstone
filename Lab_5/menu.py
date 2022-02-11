"""
This program allows the user to add basic information like the name, country and numbers of catches for each record 
holder of Chainsaw Juggling as well as delete or update based on their name
"""
import peewee
from RecordHolder import Records


def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    all_records = Records.select()
    for record in all_records:
        print(record)


def add_new_record():
    record_name = input('Enter name:')
    record_country = input('Enter country: ')
    record_catches = int(input('Enter the number of catches: '))
    try:
        new_record = Records(name=record_name, country=record_country, number_of_catches=record_catches)
        new_record.save()
    except peewee.IntegrityError:
        print('Error adding record')


def edit_existing_record():
    change_name = input('Enter name: ')
    match_record = Records.get_or_none(Records.name == change_name)
    if match_record:
        catches = int(input('Enter the number of catches: '))
        match_record.number_of_catches = catches
        match_record.save()
    else:
        print('Name not found')


def delete_record():
    delete_name = input('Enter name: ')
    match_record = Records.get_or_none(Records.name == delete_name)
    if match_record:
        match_record.delete().where(Records.name == delete_name).execute()
    else:
        print('Name not found')


if __name__ == '__main__':
    main()