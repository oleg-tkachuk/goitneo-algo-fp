import turtle
import math


class PythagorasTree:
    def __init__(self, recursion_level=5, size=55):
        self.recursion_level = recursion_level
        self.size = size
        self.painter = turtle.Turtle()
        self.setup_painter()

    def setup_painter(self):
        screen = turtle.Screen()
        screen.bgcolor("skyblue")
        self.painter.shape("turtle")
        self.painter.color("green")
        self.painter.fillcolor("orange")
        self.painter.speed(0)

    def draw_square(self, size):
        self.painter.begin_fill()
        for _ in range(4):
            self.painter.forward(size)
            self.painter.left(90)
        self.painter.end_fill()

    def draw_node(self, size, level):
        if level < 1:
            return
        self.draw_square(size)
        left_size = size * math.sqrt(3) / 2
        right_size = size / 2

        # Left branch
        self.painter.forward(size)
        self.painter.left(90)
        self.painter.forward(size)
        self.painter.right(150)
        self.painter.forward(left_size)
        self.painter.left(90)
        self.draw_node(left_size, level - 1)

        # Right branch
        self.painter.right(180)
        self.painter.forward(right_size)
        self.painter.left(90)
        self.draw_node(right_size, level - 1)
        self.painter.left(60)
        self.painter.back(size)

    def draw_tree(self):
        self.painter.penup()
        self.painter.goto(90, -150)
        self.painter.left(90)
        self.painter.pendown()
        self.draw_node(self.size, self.recursion_level)
        self.painter.hideturtle()


def main():
    recursion_level = 7
    size = 55

    print(f"*** GoIT Neo Algo Final Project ***")
    print(f"Task 2 - Creating a Pythagoras tree fractal using recursion")

    tree = PythagorasTree(recursion_level, size)
    tree.draw_tree()
    turtle.done()


if __name__ == "__main__":
    main()
