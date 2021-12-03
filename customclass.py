# Eli Arindaeng
# Assignment 10.1: Your Own Class

class Hydroflask:
    def __init__(self, owner, color, size, water = "full"):
        self.owner = owner
        self.color = color
        self.size = float(size)
        
        # hydro flask is full by default, unless specified
        if water == "full":
            self.water = self.size
        else:
            self.water = water

    # get methods
    def get_owner(self):
        return self.owner

    def get_color(self):
        return self.color 

    def get_size(self):
        return self.size

    def get_water(self):
        return self.water

    # sets amount of water to hydro flask's size
    def fill(self):
        self.water = self.size

    # drinks {gulps} oz of water
    # if drink results in 0 oz, prints 'empty' message
    def drink(self, gulps):
        if self.water <= gulps:
            self.water = 0
            print(f"{self.owner}'s hydro flask is empty!")
        else:
            self.water -= gulps

    # string magic method
    def __str__(self):
        return f"{self.owner}'s {self.color} hydro flask [{self.water} oz / {self.size} oz]"

def main():
    # Creates a new hydro flask object: Bob's blue 21 oz hydro flask (full)
    b = Hydroflask("Bob", "blue", 21)
    print(b)

    # Drinks 12 oz from Bob's hydro flask, 9 oz left
    b.drink(12)
    print(f"{b.get_owner()}'s hydro flask has {b.get_water()} oz")

    # Drinks 12 more oz from Bob's hydro flask, now empty
    b.drink(12)
    print(f"{b.get_owner()}'s hydro flask has {b.get_water()} oz")

    # Fills Bob's hydro flask back to 21 oz
    b.fill()
    print(f"{b.get_owner()}'s hydro flask has {b.get_water()} oz")
    
    # Creates a new hydro flask object: Cathy's cerulean 32 oz hydro flask (5 oz of water)
    c = Hydroflask("Cathy", "cerulean", 32, 5)
    print(c)

    # Drinks 2.5 oz from Cathy's hydro flask, 2.5 oz left
    c.drink(2.5)
    print(f"{c.get_owner()}'s hydro flask has {c.get_water()} oz")

    # Drinks 10 oz from Cathy's hydro flask, now empty
    c.drink(10)
    print(f"{c.get_owner()}'s hydro flask has {c.get_water()} oz")




if __name__ == "__main__":
    main()