ATMMachineDataBase = [
    {
        "Name": {"LastName": "James", "FirstName": "Lebron"},
        "AccountNo": 133437,
        "PIN": 3647,
        "ControlNo": 551,
        "Balance": 1433.90
    },
    {
        "Name": {"LastName": "Romnick", "FirstName": "Kapares"},
        "AccountNo": 14547,
        "PIN": 1234,
        "ControlNo": 896,
        "Balance": 1434.00
    },
    {
        "Name": {"LastName": "Dizon", "FirstName": "Jepoy"},
        "AccountNo": 167897,
        "PIN": 3244,
        "ControlNo": 534,
        "Balance": 1334.67
    }
]

myName = input("Enter your first name: ")
PIN = int(input("Enter your PIN: "))

found = False

for account in ATMMachineDataBase:
    if account["Name"]["FirstName"].lower() == myName.lower() and account["PIN"] == PIN:
        print(f"Good Day, {myName}! Your balance is ₱{account['Balance']:.2f}.")
        found = True
        break

if not found:
    print("Invalid name or PIN. Please try again.")