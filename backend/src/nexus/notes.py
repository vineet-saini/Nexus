def create_note(title, content):
    note = {
        "title": title,
        "content": content,
    }
    return note


def list_notes(notes):
    for i, item in enumerate(notes, start=1):
        print(i, item["title"])

def delete_note(notes, note_no):
    del notes[note_no]


def update_note(notes, note_no, new_title, new_content):
    note = notes[note_no]
    note["title"] = new_title
    note["content"] = new_content
