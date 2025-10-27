strInput = "14613424873684a2347k23478724o 42348n897a9la8797ng9877 s89787a7988978n987896567a557"

newString = ""
for char in strInput:
    if not char.isnumeric():
        newString = newString + char
    else:
        print(f"Hindi pasok yan kasi yan ay: {char} ")
print(newString)

