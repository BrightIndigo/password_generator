import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Please enter the desired password length: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Password Generator!")

    password_length = get_password_length()
    generated_password = generate_password(password_length)

    print(f"Your generated password: {generated_password}")

if __name__ == "__main__":
    main()
