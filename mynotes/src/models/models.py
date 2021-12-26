from pathlib import Path
import csv


class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username


class Note:
    def __init__(self, id, title, content, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id


def read_users_from_file():
    p = Path(__file__).with_name('users.csv')
    with p.open('r') as file:
        type(file)

        csvreader = csv.reader(file)
        next(csvreader)

        users = []
        for row in csvreader:
            users.append(User(row[0], row[1]))
    return users


def write_user_to_file(username):
    p = Path(__file__).with_name('users.csv')

    users = read_users_from_file()
    last_user = users[-1]

    file = p.open("a")
    writer = csv.writer(file)
    row = [str(int(last_user.id)+1), username]
    writer.writerow(row)
    file.close()
    return User(str(int(last_user.id)+1), username)


def delete_user_from_file(user):
    lines = []

    p = Path(__file__).with_name('users.csv')
    with open(p, 'r') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            if row[0] != user.id:
                lines.append(row)
    with open(p, 'w') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(lines)


def read_notes_from_file():
    p = Path(__file__).with_name('notes.csv')
    with p.open('r') as file:
        type(file)

        csvreader = csv.reader(file)
        next(csvreader)

        notes = []
        for row in csvreader:
            notes.append(Note(row[0], row[1], row[2], row[3]))
    return notes


def read_notes_from_file_for_user(user):
    p = Path(__file__).with_name('notes.csv')
    with p.open('r') as file:
        type(file)

        csvreader = csv.reader(file)

        next(csvreader)

        notes = []
        for row in csvreader:
            if user.id == row[3]:
                notes.append(Note(row[0], row[1], row[2], row[3]))
    return notes


def write_note_to_file(note):
    p = Path(__file__).with_name('notes.csv')

    notes = read_notes_from_file()
    last_note = notes[-1]

    file = p.open("a")
    writer = csv.writer(file)
    row = [str(int(last_note.id)+1), note.title, note.content, note.user_id]
    writer.writerow(row)
    file.close()
    note.id = str(int(last_note.id)+1)
    return note


def delete_note_from_file(note):
    lines = []

    p = Path(__file__).with_name('notes.csv')
    with open(p, 'r') as read_file:
        reader = csv.reader(read_file)
        for row in reader:
            if row[0] != note.id:
                lines.append(row)
    with open(p, 'w') as write_file:
        writer = csv.writer(write_file)
        writer.writerows(lines)


def update_note_in_file(note):
    delete_note_from_file(note)
    write_note_to_file(note)
    return note
