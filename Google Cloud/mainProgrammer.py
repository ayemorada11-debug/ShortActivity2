import os
import csv
import time

#File Detector
print(os.getcwd())
print(os.listdir(os.getcwd()))
#os.makedirs(os.getcwd() + "new folder 1"))
#os.makedirs(os.path.join(os.getcwd() + "new folder 2"))
#os.makedirs(os.path.join(os.path.join(os.getcwd(), "new folder 3"), "folder inside the folder")) #new folder inside a new folder
#os.makedirs(os.path.join(os.path.join(os.getcwd(), "new folder 4")), exist_ok=True) #new folder inside an existing folder
#os.makedirs(os.path.join(os.path.join(os.getcwd(), "virus")), exist_ok=True)

print(os.path.abspath(__file__))

Base = os.path.dirname(os.path.abspath(__file__))
print(Base)

#ADD NEW FILE
with open("virus.txt", 'w', newline='') as harmfile:
    print("File Created")

time.sleep(10)

#pathdir = ""
for root, dirs, files in os.walk(Base):
    for name in files:
        print(name)
        if name == "virus.txt":
            print(os.path.join(root, name))
            pathdir = os.path.join(root, name)
            os.remove(pathdir)
            break