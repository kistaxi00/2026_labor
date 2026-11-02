Grafikus Autóverseny

Hallgatói adatok:
Takács Richárd:
BHF4ETNeptun-kód:

Feladat leírása:
A program egy kétszemélyes, grafikus autóverseny szimuláció Python nyelven. A két autó a d és a k gomb nyomására indul el a célvonalig.
Az escape gombbal lehet kilépni és a verseny során ütközésre is van lehetőség.

A játék kétféleképpen érhet véget:
Győzelem: Valamelyik autó átlépi az X = 300-as koordinátánál lévő célvonalat. 
Ütközés: A két autó túlságosan közel kerül egymáshoz (a távolságuk 20 pixel alá csökken), ekkor a játék ütközést észlel és azonnal leáll.

Felhasznált modulok:
`turtle` – Grafikus ablak, alakzatok rajzolása és billentyűzet-eseménykezelés.
`random` – Véletlenszám-generálás a dinamikus sebességhez és a kacsázáshoz.
`autóverseny.py` – Saját modul az objektumorientált logika tárolására.

Felhasználói leírás:
Telepítés: Külső könyvtár telepítése nem szükséges, a standard Python modulokat használja.
Indítás: A `main.py` fájl futtatásával indítható.
Irányítás:
`d` billentyű: Piros autó léptetése
`k` billentyű: Zöld autó léptetése
`Escape` billentyű: Kilépés a játékból

Program felépítése
Saját modul: `autóverseny.py`
Saját osztály: `Auto_TR` (a `turtle.Turtle` osztályból öröklődik)

Saját metódusok az osztályban:
`indit_TR()` – Véletlenszerű sebességű előrehaladás és Y tengelyi kacsázás.
`alaphelyzet_TR()` – Pozíció beállítása.
`megall_TR()` – Sebesség nullázása.

Saját függvények:
`celvonal_rajzolas_TR()` – Célvonal kirajzolása.
`kihirdetes_TR()` – Végeredmény vagy ütközési üzenet kiírása.