import pytest
from polygon import Polygon
def test_polygon_initialization():
    """tests initialization of a Polygon object"""
    polygon = Polygon("Triangle", [3, 3, 3])
    assert polygon.get_name() == "Triangle"
    assert polygon.get_sides() == [3, 3, 3]

def test_getters_and_setters():
    """tests getter and setter methods for name and sides"""
    polygon = Polygon("Triangle", [3, 3, 3])
    polygon.set_name("Square")
    polygon.set_sides([4, 4, 4, 4])

    assert polygon.get_name() == "Square"
    assert polygon.get_sides() == [4, 4, 4, 4]
def test_polygon_equality():
    """tests __eq__ method for Polygon objects """
    polygon1 = Polygon("Triangle", [3, 3, 3])
    polygon2 = Polygon("Triangle", [3, 3, 3])
    assert polygon1 == polygon2

def test_polygon_inequality():
    """ tests__ne__ method for Polygon objects"""
    polygon1 = Polygon("Triangle", [3, 3, 3])
    polygon2 = Polygon("Square", [4, 4, 4, 4])
    assert polygon1 != polygon2

def test_polygon_str():
    """tests the format for printing"""
    polygon = Polygon("Triangle", [3, 3, 3])
    assert str(polygon) == "Triangle with sides: [3, 3, 3]"

def test_calculate_circumference():
    """tests calculate_circumference method for Polygon objects"""
    polygon = Polygon("Triangle", [3, 3, 3])
    assert polygon.calculate_circumference() == 9


