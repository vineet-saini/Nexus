import json

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
