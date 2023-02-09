import turtle

turtle.title("Cringe smile")
smile = turtle.Turtle()
smile.shape("turtle")
smile.pensize(5)
smile.pencolor("yellow")

smile.circle(100)
smile.up()

# Рисует глаза
smile.goto(-40, 120)
smile.down()
smile.fillcolor('yellow')
smile.begin_fill()
smile.circle(15)
smile.end_fill()
smile.up()

smile.goto(40, 120)
smile.down()
smile.fillcolor('yellow')
smile.begin_fill()
smile.circle(15)
smile.end_fill()
smile.up()

# Рисует нос
smile.goto(0, 75)
smile.down()
smile.fillcolor('yellow')
smile.begin_fill()
smile.circle(6)
smile.end_fill()
smile.up()

# Рисует рот
smile.goto(-40, 85)
smile.down()
smile.right(90)
smile.circle(40, 180)
smile.up()

turtle.exitonclick()