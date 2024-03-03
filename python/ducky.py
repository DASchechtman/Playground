import random

def Ducks():
    return "".join([random.choice([":CoolDuck:", ":DuckPopcorn:", ":DuckCoin:"]) for _ in range(10)])

for i in range(10):
    print(Ducks())