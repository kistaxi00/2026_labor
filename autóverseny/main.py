import turtle
import autóverseny_TR as sajatmodul

def app():
    ablak = turtle.Screen()
    ablak.title("Grafikus Autóverseny & Ütközés Szimuláció")
    ablak.bgcolor("black")

    sajatmodul.celvonal_rajzolas_TR()

    a1 = sajatmodul.Auto_TR("red", -350, 15, 10, "Piros autó")
    a2 = sajatmodul.Auto_TR("green", -350, -15, 10, "Zöld autó")


    jatek_allapot = {"vege": False}

    def ellenorzes_TR():
        if a1.distance(a2) < 20:
            jatek_allapot["vege"] = True
            sajatmodul.kihirdetes_TR("ÜTKÖZÉS! A játéknak vége!", "red")


        if jatek_allapot["vege"] == False:
            if a1.xcor() >= 300:
                jatek_allapot["vege"] = True
                sajatmodul.kihirdetes_TR(f"A győztes: {a1.nev}!", "yellow")

        if jatek_allapot["vege"] == False:
            if a2.xcor() >= 300:
                jatek_allapot["vege"] = True
                sajatmodul.kihirdetes_TR(f"A győztes: {a2.nev}!", "yellow")

    def a1_lepes_TR():
        if jatek_allapot["vege"] == False:
            a1.indit_TR()
            ellenorzes_TR()

    def a2_lepes_TR():
        if jatek_allapot["vege"] == False:
            a2.indit_TR()
            ellenorzes_TR()


    ablak.listen()
    ablak.onkey(a1_lepes_TR, "d")
    ablak.onkey(a2_lepes_TR, "k")
    ablak.onkey(turtle.bye, "Escape")

    turtle.mainloop()

if __name__ == '__main__':
    app()