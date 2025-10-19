
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

#String Join
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

