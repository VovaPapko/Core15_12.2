import pickle
from random import randint

class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

hotels = []

for i in range(10):
    hotels.append(Hotel(f"hotel-{i}", randint(100, 500)))
    
with open("hotels.bin", "wb") as f:
    pickle.dump(hotels, f)