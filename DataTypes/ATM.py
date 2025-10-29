#list of a nested dict
ATMMachineDataBase = [
    { "Name": {
        "LastName": "Natanggal",
        "FirstName": "Kuya", }
        ,
    "AccountNo": 133437,
    "PIN" :3647  ,
    "ControlNo" : 551 ,
    "Balance" : 1500300.00
    } ,
{ "Name": {
        "LastName": "Martin",
        "FirstName": "Coco", }
        ,
    "AccountNo": 14547,
    "PIN" :1234  ,
    "ControlNo" : 896,
    "Balance" : 1500300.00
    } ,
{ "Name": {
        "LastName": "Mainit",
        "FirstName": "Tabi", }
        ,
    "AccountNo": 167897,
    "PIN" :3244  ,
    "ControlNo" : 534,
"Balance" : 1500300.00
    } ,
    ]
myName = input("Enter your name: ")
PIN = input("Enter your PIN: ")
Balance = float(input("Enter your balance: "))  # convert input to number

print(f"Good Day! {myName}! Your balance is {Balance}")


