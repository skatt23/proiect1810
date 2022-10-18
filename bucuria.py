import turtle
from turtle import Turtle, Screen
bucurie = turtle.getscreen()
t = turtle.Turtle()


turtle.penup()
turtle.setpos(-200, -200)
turtle.pendown()
turtle.pencolor("black")
turtle.pensize(2)
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()
turtle.penup()
turtle.setpos(50, -150)
turtle.pendown()
turtle.pencolor("black")
turtle.pensize(2)
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

t.penup()
t.setpos(50, 25)
t.pendown()
t.pencolor("black")
t.pensize(2)
t.fillcolor("blue")
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.setpos(-200, 25)
t.pendown()
t.pencolor("black")
t.pensize(2)
t.fillcolor("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()

FONT = ("Arial", 14, "bold")


class Graphics:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1280, height=800)
        self.screen.listen()

        self.turtle = Turtle(visible=False)
        self.turtle.speed('fastest')

    def text_at_xy(self, x, y, text):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.write(text, font=FONT)

    def text_onkey(self, x, y, text, key):
        self.screen.onkey(lambda a=x, b=y, mesaj=text: self.text_at_xy(a, b, mesaj), key)

    def text_onmouseclick(self, text):
        self.screen.onclick(lambda x, y, mesaje=text: self.text_at_xy(x, y, mesaje))


graphics = Graphics()
graphics.text_at_xy(-220, 200, "Bucuraţi-vă cu cei ce se bucură; plângeţi cu cei ce plâng.")
graphics.text_at_xy(100, 100, "Tristetea")  # just print text at location
graphics.text_at_xy(0, -220, "Tristetea atunci cand e impartasita")

graphics.text_onkey(-270, -220, "Bucuria atunci cand e impartasita!", "space")

graphics.text_onmouseclick("Bucuria")  # print text whereever mouse is clicked

graphics.screen.mainloop()
