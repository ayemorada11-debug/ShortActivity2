isGroupPassed = False
passingGrade = 85
rjGrade = 75
padGrade = 95
redGrade = 86
isredPassed = redGrade >= passingGrade
print(isredPassed)
isrjPassed = rjGrade >= passingGrade
print(isrjPassed)
ispadPassed = padGrade >= passingGrade
print(ispadPassed)
isGroupPassed = ispadPassed and isredPassed and isrjPassed
print(isGroupPassed)


intA = 7
intB = 11
intC = 9

isDivisible = False #initial value
remainder = intA % intB #modulus or the percent sign returns the remainder
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)

isDivisible = False #initial value <--------------------------------------
remainder = intA % intC
print(remainder)
if remainder == 0:
    isDivisible = True
print(isDivisible)