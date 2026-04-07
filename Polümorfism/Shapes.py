"""Shapes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self._color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self._color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self._color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        pass


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius
        """
                Circle constructor.

                The color is stored using superclass constructor:
                super().__init__(color)

                The radius value is stored here.
                """

    def __repr__(self) -> str:
        return f"Circle (r: {self.radius}, color: {self.get_color()})"

    """
            Return representation of the circle.

            For this exercise, this should return a string:
            Circle (r: {radius}, color: {color})
            """

    def get_area(self) -> float:
        """
                Calculate the area of the circle.

                Area of the circle is pi * r * r.
                """
        return math.pi * self.radius * self.radius


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        super().__init__(color)
        self.side = side
        """
                Square constructor.

                The color is stored using superclass constructor:
                super().__init__(color)

                The side value is stored here.
                """

    def __repr__(self) -> str:
        return f"Square (a: {self.side}, color: {self.get_color()})"

    """
            Return representation of the square.

            For this exercise, this should return a string:
            Square (a: {side}, color: {color})
            """

    def get_area(self) -> float:
        return self.side * self.side

    """
            Calculate the area of the square.

            Area of the square is side * side.
            """


class Rectangle(Shape):

    def __init__(self, color: str, length: float, width: float):
        super().__init__(color)
        self.length = length
        self.width = width
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)"""

    def get_area(self) -> float:
        return self.length * self.width
    """Calculate area of the rectangle.
    Area of the rectangle is length * width"""

    def __repr__(self) -> str:
        return f"Rectangle (l: {self.length}, w: {self.width}, color: {self.get_color()})"

    """
    Return representation of the square."""


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        self.shapes.append(shape)
        """Add a shape to the program."""

    def get_shapes(self) -> list:
        return self.shapes
    """Return all the shapes."""

    def calculate_total_area(self) -> float:
        return sum(shape.get_area() for shape in self.shapes)
    """Calculate total area of the shapes."""

    def get_circles(self) -> list:
        return [shape for shape in self.shapes if isinstance(shape, Circle)]
    """Return only circles."""

    def get_squares(self) -> list:
        return [shape for shape in self.shapes if isinstance(shape, Square)]
    """Return only squares."""

    def get_rectangles(self) -> list:
        return [shape for shape in self.shapes if isinstance(shape, Rectangle)]
    """Return only rectangles."""


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    rectangle = Rectangle("green", 5, 4)

    paint.add_shape(circle)
    paint.add_shape(square)
    paint.add_shape(rectangle)

    print(paint.calculate_total_area())
    print(paint.get_circles())