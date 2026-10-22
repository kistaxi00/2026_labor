import turtle
import random

#OOP szerkezet: turtle.Turtle öröklődés
class Auto(turtle.Turtle):
    def __init__(self, szin, x, y, sebesseg, nev):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.sebesseg = sebesseg
        self.nev = nev

    def indit(self):
        # Előre haladás az X tengelyen
        veletlen_sebesseg = self.sebesseg + random.randint(-2, 5)
        self.forward(veletlen_sebesseg)

        # Kacsázás / Véletlenszerű elmozdulás az Y tengelyen (-5 és +5 között)
        uj_y = self.ycor() + random.randint(-5, 5)
        self.sety(uj_y)


def celvonal_rajzolas():
    rajzolo = turtle.Turtle()
    rajzolo.hideturtle()
    rajzolo.speed(0)
    rajzolo.penup()
    rajzolo.goto(300, 150)
    rajzolo.pendown()
    rajzolo.pensize(5)
    rajzolo.color("white")
    rajzolo.goto(300, -150)


def kihirdetes(szoveg, szin):
    kiiro = turtle.Turtle()
    kiiro.hideturtle()
    kiiro.color(szin)
    kiiro.penup()
    kiiro.goto(0, 100)
    kiiro.write(szoveg, align="center", font=("Arial", 20, "bold"))


# Főprogram
if __name__ == '__main__':
    ablak = turtle.Screen()
    ablak.title("Grafikus Autóverseny")
    ablak.bgcolor("black")

    celvonal_rajzolas()

    # Autók példányosítása közelebbi sávokban (Y = 15 és Y = -15)
    a1 = Auto("red", -350, 15, 10, "Piros autó")
    a2 = Auto("green", -350, -15, 10, "Zöld autó")

    # Játék állapotának követése
    jatek_allapot = {"vege": False}

    def ellenorzes():
        # 1. Ütközés vizsgálata (ha a két autó távolsága 20 pixelnél kisebb)
        if a1.distance(a2) < 20:
            jatek_allapot["vege"] = True
            kihirdetes("ÜTKÖZÉS! A játéknak vége!", "red")

        # 2. Célvonal elérésének vizsgálata (csak ha még nincs vége a játéknak)
        if jatek_allapot["vege"] == False:
            if a1.xcor() >= 300:
                jatek_allapot["vege"] = True
                kihirdetes(f"A győztes: {a1.nev}!", "yellow")

        if jatek_allapot["vege"] == False:
            if a2.xcor() >= 300:
                jatek_allapot["vege"] = True
                kihirdetes(f"A győztes: {a2.nev}!", "yellow")

    def a1_lepes():

        if jatek_allapot["vege"] == False:
            a1.indit()
            ellenorzes()

    def a2_lepes():
        if jatek_allapot["vege"] == False:
            a2.indit()
            ellenorzes()

    # Billentyűzet eseménykezelés
    ablak.listen()
    ablak.onkey(a1_lepes, "d")
    ablak.onkey(a2_lepes, "k")
    ablak.onkey(turtle.bye, "Escape")

    turtle.mainloop()


