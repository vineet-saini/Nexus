from .notes import create_note, list_notes, update_note, delete_note
from .persistence import save_notes, load_notes


def view_notes(notes, notes_no):
    note = notes[notes_no]
    print("Title:", note["title"])
    print("Content: ", note["content"])



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