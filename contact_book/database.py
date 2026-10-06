
import json
import os


DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "contacts.json")


def load_contacts():
    # Create data folder if it doesn't exist
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    # Create JSON file if it doesn't exist
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)

    # Load contacts from JSON file
    try:
        with open(DATA_FILE, "r") as file:
            contacts = json.load(file)

        return contacts

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_contacts(contacts):
    # Create data folder if it doesn't exist
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    # Save contacts to JSON file
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)