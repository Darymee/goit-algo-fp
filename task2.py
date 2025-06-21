import turtle
import math

def draw_tree(t, length, level):
    if level == 0:
        return

    t.forward(length)

    x, y = t.pos()
    angle = t.heading()

    new_length = length * math.sqrt(2) / 2

    t.left(45)
    draw_tree(t, new_length, level - 1)

    t.setpos(x, y)
    t.setheading(angle)

    t.right(45)
    draw_tree(t, new_length, level - 1)

    t.setpos(x, y)
    t.setheading(angle)

def main():
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("brown")
    t.speed("fastest")
    t.left(90) 
    t.up()
    t.goto(0, -250)
    t.down()

    draw_tree(t, 100, level)

    screen.mainloop()

if __name__ == "__main__":
    main()
