##SETS - no duplicate, no order
fruitsA = {"apple", "apple", "orange", "banana", "guyabano", "lanzones"}
fruitsB = {"mango", "lanzones", "guyabano", "atis", "rambutan"} #Oh! that's a no no no
fruitsA.add("papaya") #Add
print(fruitsA)
YunYonFruits = fruitsA.union(fruitsB) #yun yon!, combine same, remove posers
print(YunYonFruits)
InterseksyonFruits = fruitsA.intersection(fruitsB) #intersection, return common value/s
print(InterseksyonFruits)
FruitDiff = fruitsA.difference(fruitsB)
print(FruitDiff)
FruitDiff = fruitsB.difference(fruitsA)
print(FruitDiff) #return difference