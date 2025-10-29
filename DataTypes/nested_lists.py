##Malulusog na prutas
fruitsA = ["apple", "apple", "orange", "banana", "grapes"]
fruitsB = ["mango", "lanzones", "guyabano", "atis", "rambutan"]
fruitsC = ["duhat", "santol", "sineguelas", "chico", "caimito"]
# all combined, tabulated
FruitBasketList = [fruitsA, fruitsB, fruitsC] #list of a list
print(FruitBasketList)
##specific??
print(FruitBasketList[2])
print(FruitBasketList[2][2])
#add, outputs single line list
FruitBasketList_Plus = fruitsA + fruitsB + fruitsC #single list
print(FruitBasketList_Plus)
#extend FruitBasketList_Extended
fruitsA.extend(fruitsB)
fruitsA.extend(fruitsC)
print(fruitsA) #single 