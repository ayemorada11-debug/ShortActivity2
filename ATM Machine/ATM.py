
#Simple ATM Machine Flow

#welcome_message():
#card_reader(isCardInserted):
#input_and_validate_pin_number(pinNumber): return isValid
#transaction_selection(transaction):
#amount_and_account_selection(amount):
#transaction_validation(amount, balance): return isValid
#card_ejection():
#card_dispensing():
#print_receipt(amount, balance):

import time

def welcome_message():
    time.sleep(1)
    print ("Welcome to my Life Bank")
    time.sleep(1)
    print("-------------")
    time.sleep(1)
    print("Please enter your card")

def card_reader(isCardInsterted):
    if isCardInsterted == "YES" :
        print("Card is Inserted")
        return True
    else:
        return False

def Pin_number():
    for i in range(4):
        if i == 3:
            print("Card is blocked. Mali ka kase")
            return False

        InputPinNumber = input("Enter your Pin Number: ") #INPUT

        if InputPinNumber == Pin:
            return True
        else:
            print("Card is blocked. Mali ka kase")

def transaction_selection():
    transaction = input("Select transaction: ")
    return transaction

def transaction_validation(amount, balance):
    if balance > amount:
        return True
    else:
        print ("Insufficient Balance, Card will be ejected")
        return False

def card_ejection():
    print("Card is ejected")

def card_dispensing():
    print("Card is dispensing")

def print_receipt(amount):
    global balance
    balance = balance - amount
    print("Remaining balance : " + str(balance))
    print("Get your receipt")
    print("\n-------------------------------")
    print("           Life Bank")
    print("       Transaction Receipt")
    print("-------------------------------")
    print("Transaction : Withdraw")
    print(f"Amount      : ₱{amount}")
    print(f"Balance     : ₱{balance}")
    print("Status      : SUCCESS")
    print("-------------------------------")
    print("Thank you for banking with us!")
    print("-------------------------------\n")


amount = 0
balance = 1000
Pin= "9117"

while True:
    welcome_message()
    isCardInserted = input("Is Card Inserted? (YES/NO)") #SENSOR
    if not card_reader(isCardInserted): #FALSE
        print("Card is not inserted")
        continue
    print("Next Steps")
    if not Pin_number():#SENSOR
        continue
    print("Next Steps")

    transaction = transaction_selection()  # Only call once

    if transaction == "withdraw":
        amount = int(input("Amount: "))
        if transaction_validation(amount, balance):
            print("Withdrawing...")
            time.sleep(2)
            card_ejection()
            time.sleep(2)
            card_dispensing()
            time.sleep(2)
            print_receipt(amount)
            time.sleep(1)

        else:
            card_ejection()
            continue

    elif transaction == "check balance":
        print("Balance Checking...")

    else:
        card_ejection()
        continue
