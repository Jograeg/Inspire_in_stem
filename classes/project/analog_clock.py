import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.title("simple analog clock")
wn.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h,m,s,pen):
    pen.penup()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

for clock in range(12):
    pen.fd(190)
    pen.pendown()
    pen.fd(20)
    pen.penup()
    pen.goto(0,0)
    pen.rt(6)

    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

for clock in range(60):
    pen.fd(200)
    pen.pendown() 
    pen.fd(10)
    pen.penup()
    pen.goto(0,0)
    pen.rt(6)

 #one
pen.penup()
pen.goto(0,0)
pen.setheading(60)
pen.fd(145)
pen.setheading(0)
pen.fd(15)
pen.write(1,move = False, align = "center", font = ("Arial",25,"normal"))

#two   
pen.penup()
pen.goto(0,0)
pen.setheading(30)
pen.fd(135)
pen.setheading(0)
pen.fd(35)
pen.write(2,move = False, align = "center", font = ("Arial",25,"normal"))

#three
pen.penup()
pen.goto(0,0)
pen.setheading(352)
pen.fd(150)
pen.setheading(0)
pen.fd(25)
pen.write(3,move = False, align = "center", font = ("Arial",25,"normal"))

#four
pen.penup()
pen.goto(0,0)
pen.setheading(315)
pen.fd(150)
pen.setheading(0)
pen.fd(45)
pen.write(4,move = False, align = "center", font = ("Arial",25,"normal"))

#five
pen.penup()
pen.goto(0,0)
pen.setheading(290)
pen.fd(178)
pen.setheading(0)
pen.fd(25)
pen.write(5,move = False, align = "center", font = ("Arial",25,"normal"))

#six
pen.penup()
pen.goto(0,0)
pen.setheading(270)
pen.fd(190)
pen.setheading(0)
pen.fd(190)
pen.write(6,move = False, align = "center", font = ("Arial",25,"normal"))

#seven
pen.penup()
pen.goto(0,0)
pen.setheading(258)
pen.fd(170)
pen.setheading(180)
pen.fd(48)
pen.write(7,move = False, align = "center", font = ("Arial",25,"normal"))

#eight
pen.penup()
pen.goto(0,0)
pen.setheading(228)
pen.fd(150)
pen.setheading(180)
pen.fd(50)
pen.write(8,move = False, align = "center", font = ("Arial",25,"normal"))

#nine
pen.penup()
pen.goto(0,0)
pen.setheading(188)
pen.fd(150)
pen.setheading(180)
pen.fd(25)
pen.write(9,move = False, align = "center", font = ("Arial",25,"normal"))

#ten
pen.penup()
pen.goto(0,0)
pen.setheading(150)
pen.fd(135)
pen.setheading(180)
pen.fd(25)
pen.write(10,move = False, align = "center", font = ("Arial",25,"normal"))

#eleven
pen.penup()
pen.goto(0,0)
pen.setheading(120)
pen.fd(145)
pen.setheading(180)
pen.fd(15)
pen.write(11,move = False, align = "center", font = ("Arial",25,"normal"))

#twelve
pen.penup()
pen.goto(0,0)
pen.setheading(60)
pen.fd(150)
pen.write(12,move = False, align = "center", font = ("Arial",25,"normal"))

#hour hand
pen.up()
pen.goto(0,0)
pen.color("red")
pen.setheading(90)
angle = (h / 12) * 360
pen.rt(angle)
pen.pendown()
pen.fd(50)

#minute hand
pen.up()
pen.goto(0,0)
pen.color("Blue")
pen.setheading(90)
angle = (m / 60) * 360
pen.rt(angle)
pen.pendown()
pen.fd(100)

#second hand
pen.up()
pen.goto(0,0)
pen.color("orange")
pen.setheading(90)
angle = (s / 60) * 360
pen.rt(angle)
pen.pendown()
pen.fd(150)

#extra writing its designed by who
pen.penup()
pen.goto(0,0)
pen.pencolor("gold")
pen.setheading(268)
pen.fd(125)
pen.setheading(0)
pen.fd(5)
pen.write("Designed by James",move = False, align = "centre", font = ("Arial",12,"normal"))

# writing name on the clock's face
pen.penup()
pen.goto(0,0)
pen.pencolor("gold")
pen.setheading(88)
pen.fd(96)
pen.write("JAMES",move = False, align = "centre", font = ("Arial",12,"normal"))

#main loop
while True:
    h = int(time.strftime("%H"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

draw_clock(h, m, s, pen)
wn.update()
time.sleep(1)
pen.clear()
wn.mainloop()
            