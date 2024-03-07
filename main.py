class Rectangle:
    """
    A class to represent a rectangle.
    ...

    Attributes
    ----------
    length : int
        length of the rectangle
    width : int
        width of the rectangle

    Methods
    -------
    area():
        Counts the area of a rectangle.
    perimeter():
        Counts the perimeter of a rectangle.
    """

    def __init__(self, length: int, width: int) -> None:
        """
        Constructs all the necessary attributes for a rectangle object.
        :param length:
        :param width:
        """
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        """
        Representation of an instance.
        :return:
        """
        return f"Rectangle('length' {self.length}; 'width' {self.width})"

    def area(self) -> int:
        """
        Counts the area of a rectangle.
        :return:
        """
        return self.width * self.length

    def perimeter(self) -> int:
        """
        Counts the perimeter of a rectangle.
        :return:
        """
        return 2 * (self.length + self.width)


if __name__ == "__main__":
    rect_1 = Rectangle(3, 2)
    area_rect_1 = rect_1.area()
    perimeter_rect_1 = rect_1.perimeter()
    print(f"Area: {area_rect_1}, perimeter: {perimeter_rect_1}")

