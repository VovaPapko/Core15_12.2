class Hotel:
    ...

hotel = Hotel()

print(hotel.__dict__)

hotel.rooms = 234

print(list(hotel.__dict__))

def return_rooms(self):
    print(self.rooms)

setattr(Hotel, "print_rooms", return_rooms)

hotel.print_rooms()
