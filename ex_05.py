class WrongHotelName(Exception):
    ...
    

class Hotel:
    def __init__(self, value, rooms=255):
        self.__name = None
        self.name = value
    
    @property
    def name(self):
        return self.__name.upper()
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise WrongHotelName("Name must be string")
        self.__name = value
    
    def __str__(self):
        return self.__name

if __name__ == "__main__":

    try:
        hotel = Hotel(9999)
    except WrongHotelName as e:
        print(e)

# hotel.name = 34562

# print(hotel.name)
