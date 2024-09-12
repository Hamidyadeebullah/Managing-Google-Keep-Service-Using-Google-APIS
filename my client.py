import requests

base_url = "http://localhost:5000"

def create_note():
    title = input("Enter the title of the note: ")
    text = input("Enter the content of the note: ")
    url = f"{base_url}/create_note"
    data = {"title": title, "text": text}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to create note."}

def fetch_notes():
    url = f"{base_url}/show_all_notes"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch notes."}

def delete_note():
    notes = fetch_notes()
    for note in notes:
        print(f"ID: {note['id']}, Title: {note['title']}, Text: {note['text']}")

    note_id = input("Enter the ID of the note you want to delete: ")
    url = f"{base_url}/delete_note/{note_id}"
    response = requests.delete(url)
    return response.json()
def modify_note():
    notes = fetch_notes()
    for note in notes:
        print(f"ID: {note['id']}, Title: {note['title']}, Text: {note['text']}")

    note_id = input("Enter the ID of the note you want to modify: ")
    new_title = input("Enter the new title of the note: ")
    new_text = input("Enter the new content of the note: ")

    url = f"{base_url}/modify_note/{note_id}"
    data = {"title": new_title, "text": new_text}
    response = requests.put(url, json=data)
    return response.json()

if __name__ == '__main__':
    while True:
        print("\nMenu:")
        print("1. See all notes")
        print("2. Create a note")
        print("3. Modify a note")
        print("4. Delete a note")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            notes = fetch_notes()
            for note in notes:
                print(f"ID: {note['id']}, Title: {note['title']}, Text: {note['text']}")

        elif choice == '2':
            create_response = create_note()
            print(create_response)

        elif choice == '3':
            modify_response = modify_note()
            print(modify_response)

        elif choice == '4':
            delete_response = delete_note()
            print(delete_response)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")