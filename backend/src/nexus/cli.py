import json


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


def show_menu():
    print("""====================
       NEXUS
====================
1. Create note
2. List notes
3. View notes
4. Delete note
5. Update note
6. Exit
====================""")


def main():
    notes = load_notes()
    while True:
        show_menu()
        choice = input()
        if choice == "6":
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
        elif choice == "4":
            try:
                note_no = int(input("Enter note number ")) - 1
                if 0 <= note_no < len(notes):
                    delete_note(notes, note_no)
                else:
                    print("Notes not found")
            except ValueError:
                print("Enter a valid note no")

        elif choice == "5":
            try:
                note_no = int(input("Enter note number ")) - 1
                if 0 <= note_no < len(notes):
                    update_note(notes, note_no)
                else:
                    print("Note not found")
            except ValueError:
                print("Enter a valid note no")

        elif choice == "1":
            note = create_note()
            notes.append(note)
            save_notes(notes)
        else:
            print("invalid choice, try again")

if __name__ == "__main__":
    main()  