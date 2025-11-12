class User:
    def __init__(self, first_name, last_name, email, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.status = status  # ✅ fix

    def display_task(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Status: {self.status}\n")


# List to store users
users = []


def add_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    return User(first_name, last_name, email)  # ✅ correct class name


while True:
    print("\nWelcome to User Management\n")
    print("Choose an action:")
    print("1. Add new user")
    print("2. Display all users") 
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_user = add_user()
        users.append(new_user)  # ✅ store in list
        print("✅ User added successfully!")
    elif choice == 2:
        if not users:
            print("⚠️ No users found.")
        else:
            print("\n--- List of Users ---\n")
            for user in users:
                user.display_task()
    elif choice == 3:
        print("👋 Goodbye!!!")
        exit()
    else:
        print("⚠️ Please enter a valid number (1-3).")
