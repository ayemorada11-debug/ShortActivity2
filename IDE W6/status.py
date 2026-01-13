citizenship = "Filipino"
age = 69
registered = False

if citizenship == "Filipino" and age >= 18:
    if registered:
        print("you can vote na, baby")
    else:
        print("you can't vote but can register, baby")
elif citizenship == "Filipino" and age < 18:
    print("you can't vote until u are 18 na, baby")
else:
    print("you can't vote nor register, baby")