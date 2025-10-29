
##LIST

fruitsA = ["apple", "apple", "orange", "banana", "grapes"]
print(fruitsA)
print(fruitsA)
print(fruitsA)
#check specific item based on its order
print(fruitsA[3])
#check the position of certain item
print(fruitsA.index("grapes"))
#boolean check
isThere = "bayabas" in fruitsA

##Random list ex
randomMixLs = ["bayabas", True, 23]
print(randomMixLs)
print(randomMixLs[2])

##List Functions
#add sa dulo
fruitsA.append("kamatis")
print(fruitsA)
#specific add, position mentioned
fruitsA.insert(2, "linga")
print(fruitsA)
#length to know positioning using index
print(len(fruitsA))
#counting stated items
print(fruitsA.count("apple"))
#removal, first match value, isa isa lang
fruitsA.remove("apple")
print(fruitsA)
#know the position
print(fruitsA.index("banana"))
#revalue
fruitsA[1] = "langka"
print(fruitsA)