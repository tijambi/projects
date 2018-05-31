import turtle

turtle.up()
turtle.goto(0, -100)  # center circle around origin
turtle.width(3)
turtle.down()

turtle.begin_fill()	
turtle.fillcolor("yellow") # head fillcolor  
turtle.circle(100) # draw head
turtle.end_fill()

turtle.up()	# draw nose
turtle.home()
turtle.goto(-40, -40)
turtle.width(3)
turtle.down()
for i in range(3):
  turtle.fd(80)
  turtle.left(120)

turtle.up()
turtle.goto(-67, -40)
turtle.setheading(-60)
turtle.width(5)
turtle.down()
turtle.circle(80, 120)  # draw smile

turtle.fillcolor("black")
for i in range(-35, 105, 70):
    turtle.up()
    turtle.goto(i, 35)
    turtle.setheading(0)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(10)  # draw eyes
    turtle.end_fill()

turtle.hideturtle()
turtle.done()
