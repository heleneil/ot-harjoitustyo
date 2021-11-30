from pathlib import Path
import csv


class User(object):
    def __init__(self, id, username):
        self.id = id
        self.username = username


class Note(object):
    id = 0
    title = ""
    content = ""
    user_id = None


'''def init_users():
    users = []
    total_notes = []
    for x in range(3):
        temp_user = User()
        temp_user.id = x
        temp_user.username = f"User {x + 1}"
        init_notes(total_notes, temp_user.id)
        users.append(temp_user)
    return users, total_notes'''


def read_users_from_file():
    p = Path(__file__).with_name('users.csv')
    with p.open('r') as file:
        type(file)

        csvreader = csv.reader(file)

        header = []
        header = next(csvreader)
        header

        users = []
        for row in csvreader:
            users.append(User(row[0], row[1]))
    return users


def init_notes(total_notes, user_id):
    for x in range(3):
        temp_note = Note()
        temp_note.user_id = user_id
        temp_note.title = f"Note {x + 1}"
        temp_note.content = f"Note content {x + 1}, for {user_id}"
        total_notes.append(temp_note)
    return total_notes
