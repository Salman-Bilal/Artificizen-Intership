
from library import Library
from exception import BookNotFoundError, NoCopiesAvailableError, AlreadyBorrowedError, NotBorrowedError

def main_cli():

    library = Library()

    while True:
        print("\n==========================================")
        print("   CENTRAL LIBRARY MANAGEMENT TERMINAL   ")
        print("==========================================")
        print("1. Add a Book to Inventory")
        print("2. Register a New Member")
        print("3. Search for a Book")
        print("4. Issue a Book (Checkout)")
        print("5. Return a Book")
        print("6. List All Books & Members")
        print("7. Shutdown Terminal System")
        
        choice = input("\n Select Command Operation (1-7): ").strip()

        try:
            if choice == "1":
                t = input("Enter Title: ")
                a = input("Enter Author: ")
                i = input("Enter ISBN: ")
                c = int(input("Enter Number of Copies: "))
                library.add_book(t, a, i, c)

            elif choice == "2":
                name = input("Enter Member Name: ")
                mid = input("Create Unique Member ID: ")
                library.add_member(name, mid)

            elif choice == "3":
                q = input(" Search title, author, or ISBN: ")
                matches = library.search_book(q)
                if matches:
                    print(f"\n Found {len(matches)} matching titles:")
                    for b in matches:
                        print(f" - {b}")
                else:
                    print(" No books matched your search query criteria.")

            elif choice == "4":
                mid = input("Enter Member ID: ")
                isbn = input("Enter Book ISBN to Issue: ")
                library.issue_book(mid, isbn)

            elif choice == "5":
                mid = input("Enter Member ID: ")
                isbn = input("Enter Book ISBN to Return: ")
                library.return_book(mid, isbn)

            elif choice == "6":
                print("\n CURRENT SYSTEM INVENTORY STATUS:")
                for b in library.books.values():
                    print(b)
                print("\n REGISTRATION DATABASE:")
                for m in library.members.values():
                    print(m)

            elif choice == "7":
                print("\n Data backups finalized. System offline. Goodbye! ")
                break
            else:
                print(" Selection command error. Choose options 1 through 7 only.")

        except ValueError:
            print(" Input Parsing Failure: Numeric fields require valid digits.")
        except (BookNotFoundError, NoCopiesAvailableError, AlreadyBorrowedError, NotBorrowedError) as custom_err:
            print(f"\n Policy Blocked Transaction: {custom_err}")

if __name__ == "__main__":
    main_cli()