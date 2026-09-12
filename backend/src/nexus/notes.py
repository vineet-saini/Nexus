from .persistence import save_notes

def create_note():
    title = input("Title: ")
    content = input("Content: ")
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
    save_notes(notes)


def update_note(notes, note_no):
    note = notes[note_no]
    new_title = input("Enter new Title ")
    new_content = input("Enter new Content ")
    note["title"] = new_title
    note["content"] = new_content
    save_notes(notes)
