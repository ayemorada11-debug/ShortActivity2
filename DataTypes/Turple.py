#Tuple #IMMUTABLE
fruitsA = ("apple", "apple", "orange", "banana", "grapes")
print(fruitsA)
print(fruitsA.index("grapes"))
print(fruitsA.count("apple"))
print(fruitsA[4])
# fruitsA[4] = "strawberry"  # does not allow this assignment, immutable
# print(fruitsA[4])
fruitsB = ("duhat", "atis", "langka", "pakwan")
fruitsBasket = (fruitsA, fruitsB)
print(fruitsBasket)
mytuple = (
    (1, 2, 3, "A"),
    (4, 5, 6, "B"),
    (7, 8, 9, "C"),
    (0, "*", "#", "D")
)

print(mytuple[3][2])