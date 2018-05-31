from turtle import *

color('red', 'yellow')
begin_fill()
while True:
	forward(200)
	left(170)
	if abs(pos()) < 1:
	    break
end_fill()
goto(50, -215)
write("Copyright 2018, Steve Jerry", font=("Arial", 16, "normal"))
done()


