class User:
    id = 0
    usermame = ""


class Note:
    id = 0
    title = ""
    content = ""
    user_id = None


def init_users():
    users = []
    total_notes = []
    for x in range(3):
        tempUser = User()
        tempUser.id = x
        tempUser.username = f"User {x + 1}"
        init_notes(total_notes, tempUser.id)
        users.append(tempUser)
    return users, total_notes


def init_notes(total_notes, user_id):
    for x in range(3):
        tempNote = Note()
        tempNote.user_id = user_id
        tempNote.title = f"Note {x + 1}"
        tempNote.content = f"Note content {x + 1}, for {user_id}"
        total_notes.append(tempNote)
    return total_notes
