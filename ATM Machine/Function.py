#FUNCTION
#BUILT IM
#USER-DEFINED FUNCTION

def sum(a,b):
    sum = a+b
    print(sum)

a = 10
b = 20

#sum = a+b
#print(sum)
sum(a,b)

a = 40
b = 25

sum(a,b)

a = 50
b = 60

sum(a,b)

#function with parameters and return
def sum(I1,I2):
    sum = I1 + I2
    print(sum)
    return sum

a = 10
b = 20
c = 30
d = 40

print (sum(a,b) + sum(c,d))


import time
#function without parameters and return
def countdown():
    print("countdown")
    for i in range (5, 0, -1):
        time.sleep(i)
        print(i)

countdown()