import pickle

class Hotel:
    ...

with open("hotels.bin", "rb") as f:
    hotels = pickle.load(f)

