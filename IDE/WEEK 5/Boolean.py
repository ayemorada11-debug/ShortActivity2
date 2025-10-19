Present = False #boolean
Exist = True #boolean
Available = "True" #string
Valid = 1 #integer
Okay = 0 #integer
Numeric = False #boolean
Char = "5"
Numeric = Char.isnumeric()
strNumeric = str(Char.isnumeric())
print([Numeric])
print([strNumeric])

#AND, OR, NOT --------------- EXOR, NOR, NAND
#in, is, not, in, is no
#==, >=. >. <=. <. !=

x = 7
y = 11
Equal = (x != y)
print(Equal)

Equal = (x == y)
print(Equal)

Equal = (x >= y)
print(Equal)


In = (10 in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(In)
In = (10 in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(In)

In = ("pad" in " pad rj red")
print(In)

In = ("babaero" in "vincent babaero") #True
print(In)

Is = ("andrei pogi" == "andrei pogi") #True
print(Is)

IS = ("bun" == "dummy")
print(IS)
