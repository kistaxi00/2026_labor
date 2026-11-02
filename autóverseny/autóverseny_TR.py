import turtle
import random

class Auto_TR(turtle.Turtle):
    def __init__(self, szin, x, y, sebesseg, nev):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.sebesseg = sebesseg
        self.nev = nev


    def indit_TR(self):
        veletlen_sebesseg = self.sebesseg + random.randint(-2, 5)
        self.forward(veletlen_sebesseg)

        uj_y = self.ycor() + random.randint(-5, 5)
        self.sety(uj_y)


    def alaphelyzet_TR(self, x, y):
        self.goto(x, y)


    def megall_TR(self):
        self.speed(0)

def celvonal_rajzolas_TR():
    rajzolo = turtle.Turtle()
    rajzolo.hideturtle()
    rajzolo.speed(0)
    rajzolo.penup()
    rajzolo.goto(300, 150)
    rajzolo.pendown()
    rajzolo.pensize(5)
    rajzolo.color("white")
    rajzolo.goto(300, -150)


def kihirdetes_TR(szoveg, szin):
    kiiro = turtle.Turtle()
    kiiro.hideturtle()
    kiiro.color(szin)
    kiiro.penup()
    kiiro.goto(0, 100)
    kiiro.write(szoveg, align="center", font=("Arial", 20, "bold"))

