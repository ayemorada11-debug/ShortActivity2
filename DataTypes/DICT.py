#KEY : VALUE
myInfo = {"Name" : "Juan", "Age" : 98 , "Gender" : "Male",}
#all in dictionary
print(myInfo)
#specific in dictionary
print(myInfo["Name"])
print(myInfo["Age"])

myInfo["Name"] = "Johnny"
print(myInfo)
#change or add
myInfo.update({"Citizenship": "Filipino"})
print(myInfo)



myInfo = {
    "Name": {
        "FirstName": "John Ronald Reuel",
        "LastName": "Tolkien",
    },
    "Age": 81,
    "Goated Movies": [
        "The Hobbit: An Unexpected Journey",
        "The Hobbit: The Desolation of Smaug",
        "The Hobbit: The Battle of the Five Armies",
        "The Lord of the Rings: The Fellowship of the Ring",
        "The Lord of the Rings: The Two Towers"
        "The Lord of the Rings: The Return of the King"
    ]
}
print(myInfo)
print(myInfo["Name"]["LastName"])
print(myInfo["Name"])
print(myInfo["Name"]["FirstName"] + " " + myInfo["Name"]["LastName"])
print(myInfo["Goated Movies"][3])