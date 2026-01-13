grade = float(input("Enter your grade: "))

if grade >= 98:
    print("Grade is greater than 1.0 : Excellent")
elif grade >= 90:
    print("Grade is greater than 1.5: Very Good")
elif grade >= 85:
    print("Grade is greater than 2.0 : Good")
elif grade >= 80:
    print("Grade is greater than 2.5: Satisfactory")
elif grade >= 70:
    print("Grade is greater than 3.0 : Poor")
else:
    print("5.0/INC/W/D")