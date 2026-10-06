
from database import load_contacts, save_contacts


def add_contact():
    contacts = load_contacts()

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("\n✅ Contact added successfully!")


def view_contacts():
    contacts = load_contacts()

    if not contacts:
        print("\n📭 No contacts found.")
        return

    print("\n" + "=" * 50)
    print("                 ALL CONTACTS")
    print("=" * 50)

    for i, contact in enumerate(contacts, start=1):
        print(f"\n{i}. Name  : {contact['name']}")
        print(f"   Phone : {contact['phone']}")
        print(f"   Email : {contact['email']}")


def search_contact():
    contacts = load_contacts()

    if not contacts:
        print("\n📭 No contacts found.")
        return

    keyword = input("Enter name or phone to search: ").strip().lower()

    found = False

    for contact in contacts:
        if (keyword in contact["name"].lower()
                or keyword in contact["phone"]):

            print("\n--- Contact Found ---")
            print(f"Name  : {contact['name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")

            found = True

    if not found:
        print("\n❌ Contact not found.")


def update_contact():
    contacts = load_contacts()

    if not contacts:
        print("\n📭 No contacts found.")
        return

    name = input("Enter the name of the contact to update: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:

            print("\nLeave a field empty to keep the old value.")

            new_name = input(
                f"Name [{contact['name']}]: "
            ).strip()

            new_phone = input(
                f"Phone [{contact['phone']}]: "
            ).strip()

            new_email = input(
                f"Email [{contact['email']}]: "
            ).strip()

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            save_contacts(contacts)

            print("\n✅ Contact updated successfully!")
            return

    print("\n❌ Contact not found.")


def delete_contact():
    contacts = load_contacts()

    if not contacts:
        print("\n📭 No contacts found.")
        return

    name = input("Enter the name of the contact to delete: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:

            confirm = input(
                f"Are you sure you want to delete {contact['name']}? (y/n): "
            ).strip().lower()

            if confirm == "y":
                contacts.remove(contact)
                save_contacts(contacts)

                print("\n🗑️ Contact deleted successfully!")
            else:
                print("\n❌ Delete cancelled.")

            return

    print("\n❌ Contact not found.")
