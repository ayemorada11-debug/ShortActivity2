#string
print("hello world")
print("hello world")
print("hello world")
print(' Drei said : "nagkaon ka na lab" ' )
print(' Drei said : "nagkaon ka na lab" ' )
input("Enter your name : " )
input("Enter your age : " )
input('stop the car')
input('boundary na')

#STRING
strFullName = ("Andrei Lionne Morada")
intLength = len(strFullName)

print(intLength)
print(strFullName[0])
print(strFullName[3])
print(strFullName[5])
print(strFullName[7])
print(strFullName[intLength - 1])

strInputForUser = "ako nalang sana~"

strFullName = strInputForUser
print(strFullName)
intLength = len(strFullName)
print(intLength)

#STRING
strFullName = "Andrei Lionne Morada"
strNewValue = strFullName.upper()
print(strNewValue)

strNewValue = strFullName.lower()
print(strNewValue)

strNewValue = strFullName.count("n")
print(strNewValue)

strNewValue = strFullName.split(" ")
print(strNewValue)

strModified = strFullName.swapcase()
print(strModified)

strModified = strFullName.replace("Andrei Lionne Morada", "Ihh Ang Bangis")
print(strModified)

#String Joined
FirstName = "Andrei Lionne"
LastName = "Morada"
MiddleName = "Perez"
JoinedFirstName = ",".join((LastName, FirstName, MiddleName))
print(JoinedFirstName)

#ISNUMERIC
NewValue = strFullName.isnumeric()
print(NewValue)

NewValue = strFullName[0:7]
print(NewValue)
NewValue = strFullName[7:14]
print(NewValue)

print(strFullName.index("n"))
print(strFullName.index("n",7,11))

#
strInput = "14613424873684a2347k23478724o 42348n897a9la8797ng9877 s89787a7988978n987896567a557"

newString = ""
for char in strInput:
    if not char.isnumeric():
        newString = newString + char

print(newString)