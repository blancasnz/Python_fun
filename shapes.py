import turtle

def animator():
    window = turtle.Screen()
    window.bgcolor("black")

    trevor = turtle.Turtle()
    trevor.shape("turtle")
    trevor.color("white")
    trevor.speed("slow")

    counter = 4
    while counter > 0 :
        counter = counter - 1
        trevor.forward(100)
        trevor.right(90)

    harold = turtle.Turtle()
    harold.shape("arrow")
    harold.color("blue")
    harold.circle(100)

    chibi = turtle.Turtle()
    chibi.shape("circle")
    chibi.color("pink")
    chibi.speed("slow")

    chibi.left(180)
    chibi.forward(100)
    chibi.left(135)
    chibi.forward(140)
    chibi.left(135)
    chibi.forward(100)

    window.exitonclick()

animator()
