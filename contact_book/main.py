from contacts import (
    add_contact,
    view_contacts,
    search_contact,
    update_contact,
    delete_contact
)


def show_menu():
    print("\n" + "=" * 30)
    print("       CONTACT BOOK")
    print("=" * 30)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("=" * 30)


def main():
    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("\nThank you for using Contact Book!")
            break

        else:
            print("\n❌ Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()