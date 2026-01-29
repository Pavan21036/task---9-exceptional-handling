
import logging

# Logging configuration
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        print("Error: Cannot divide by zero")

    except ValueError:
        logging.error("Invalid input: Non-numeric value entered")
        print("Error: Please enter only numbers")

    else:
        print("Division successful")

    finally:
        print("Division operation completed\n")


def open_file():
    try:
        file = open("sample.txt", "r")
        print(file.read())
        file.close()

    except FileNotFoundError:
        logging.error("File not found")
        print("Error: File does not exist")

    finally:
        print("File operation completed\n")


def main():
    print("---- Exception Handling & Logging Demo ----")
    divide_numbers()
    open_file()


if __name__ == "__main__":
    main()
