class Hotel:
    __slots__ = ["name", "rooms"]
    
    def __init__(self, name, rooms) -> None:
        self.name = name
        self.rooms = rooms


hotel = Hotel("Kalyna", 22)

hotel.area = "Kyiv"