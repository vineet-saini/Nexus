from .notes import create_note, list_notes,view_notes, update_note, delete_note
from .persistence import save_notes, load_notes

def is_valid_note_no(notes, note_no):
    return 0 <= note_no < len(notes)

def get_valid_note_no(notes):
    while True:
        try:
            note_no = int(input("Enter note number ")) - 1
            if is_valid_note_no(notes, note_no):
                return note_no
            else:
                print("Enter a valid note number ")
                continue
        except ValueError:
            print("Enter a Valid note number")
            continue

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
                result = list_notes(notes)
                for i, item in enumerate(result, start=1):
                    print(i ,item["title"])
            else:
                print("No notes found")
        elif choice == "3":
            try:
                note_no = get_valid_note_no(notes)
                if note_no is not None:
                    view_note = view_notes(notes, note_no)
                    print("Title:", view_note["title"])
                    print("Content: ", view_note["content"])
                else:
                    print("Notes not found")
            except ValueError:
                print("Enter a valid note no")
        elif choice == "4":
            try:
                note_no = get_valid_note_no(notes)
                if note_no is not None:
                    delete_note(notes, note_no)
                    save_notes(notes)
                else:
                    print("Notes not found")
            except ValueError:
                print("Enter a valid note no")

        elif choice == "5":
            try:
                note_no = get_valid_note_no(notes)
                if note_no is not None:
                    new_title = input("Enter new Title ")
                    new_content = input("Enter new Content ")
                    update_note(notes, note_no, new_title, new_content)
                    save_notes(notes)
                else:
                    print("Note not found")
            except ValueError:
                print("Enter a valid note no")

        elif choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            note = create_note(title, content)
            notes.append(note)
            save_notes(notes)
        else:
            print("invalid choice, try again")

if __name__ == "__main__":
    main()  