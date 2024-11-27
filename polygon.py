class Polygon:
    def __init__(self, name, sides):
        self.__name  = name
        self.__sides = sides
    def get_name(self):
        """gets name of polygon"""

        return self.__name

    def set_name(self, name):
        """sets the name of the polygon"""
        self.__name = name

    def get_sides(self):
        """ gets the sides of the polygon"""
        return self.__sides

    def set_sides(self, sides):
        """ Sets the sides of the polygon"""
        self.__sides = sides
    def __eq__(self, other):
        """checks if two polygons are equal based on their name and sides"""
        return self.__name == other.__name and self.__sides == other.__sides
    def __ne__(self, other):
        """reurns the opposite of the __eq__ function result"""
        return not self.__eq(other)
    def __str__(self):
        """gives a user friendly format for printing"""
        return f"{self.__name} with sides: {self.__sides}"
    def calculate_circumference(self):
        """calculates circumference of polygon"""
        return sum(self.__sides)
def main():
    """executes all components of polygon class"""

    triangle = Polygon("Triangle with sides: ", [3, 3, 3])
    square = Polygon("Square with sides: ", [4, 4, 4, 4])
    hexagon = Polygon("Hexagon with sides: ", [6, 6, 6, 6, 6, 6])

    print(triangle)
    print(f"circumference is {triangle.calculate_circumference()}")

    print(square)
    print(f"circumference is {square.calculate_circumference()}")

    print(hexagon)
    print(f"circumference is {hexagon.calculate_circumference()}")

if __name__ == "__main__":
    main()
        
