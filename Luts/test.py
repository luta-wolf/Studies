import pickle

FILENAME = "user.dat"

name = "Tom"
age = 19

with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)
