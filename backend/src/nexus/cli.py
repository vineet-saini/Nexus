import json
notes = []
def create_note():
    title = input("Title: ")
    content = input("Content: ")
    note = {
        "title": title,
        "content": content,
    }
    return note

def list_notes(notes):
    for i, item in enumerate(notes, start = 1):
        print(i, item["title"])

def view_notes(notes, notes_no):
    note = notes[notes_no]
    print("Title:", note["title"])
    print("Content: ", note["content"])

def save_notes(notes):
    try:
        with open("notes.json", "w") as file:
            json.dump(notes, file)
    except FileNotFoundError:
        print("File not found")

def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
        return notes
    except FileNotFoundError:
        print("File not found")
        return []

def show_menu():
    print("""====================
       NEXUS
====================
1. Create note
2. List notes
3. View notes
4. Exit
====================""")

notes = load_notes()
while(True):
    show_menu()
    choice = input()
    if choice == "4":
        print("good bye")
        break
    elif choice == "2":
        if notes:
            list_notes(notes)
        else:
            print("No notes found")
    elif choice == "3":
        try:
            note_no = int(input("Enter note number ")) - 1
            if 0 <= note_no < len(notes):
                view_notes(notes, note_no)
            else:
                print("Notes not found")
        except ValueError:
            print("Enter a valid note no")

    elif choice == "1":
        note = create_note()
        notes.append(note)
        save_notes(notes)
    else:
        print("invalid choice, try again")


