from ex_05 import Hotel


class Resort:
    def __init__(self, hotels):
        self.hotels = hotels
    
    def iterator(self, n=3):
        result = ""
        count = 0
        for h in self.hotels:
            result += str(h) + "\n"
            count += 1
            if count >= n:
                yield result
                count = 0
                result = ""
        if result:
            yield result
    
    def __str__(self):
        return "\n".join(str(h) for h in self.hotels)


hotels = []
for i in range(10):
    hotels.append(Hotel(str(i)))
    
resort = Resort(hotels)

for rec in resort.iterator(7):
    print(rec)
    print("page")
