"""Név: Urbán Mihály
Szak: Mérnökinformatika Szoftverfejlesztő szakirány
Neptun azonosító: YQV5BS


1. Miért hasznosak a design pattern-ök a szoftverfejlesztésben?
a) Megnövelik a kód futási sebességét
b) Megkönnyítik az összetett rendszerek dokumentálását
c) Javítják a kód újrafelhasználhatóságát és karbantarthatóságát
d) Csökkentik a szoftver licencköltségeit
Válasz: c

2. Mire szolgál az init metódus Pythonban?
a) Egy osztály törlésére
b) Az osztály statikus metódusainak definiálására
c) Egy osztály metódusainak futtatására
d) Egy osztály példányának inicializálására
Válasz: d

3. Mi a célja az egységbezárásnak (encapsulation) az OOP-ban?
a) Az adatok és metódusok elrejtése a külvilág elől
b) Objektumok közötti kommunikáció javítása
c) Az öröklődés megkönnyítése
d) A program futási sebességének növelése
Válasz: a

4. Mi a helyes módja egy osztálypéldány attribútumának elérésének Pythonban?
a) Class.attribute
b) Class->attribute
c) Class::attribute
d) instance.attribute
Válasz: d

5. Mi a különbség az attribútum és a metódus között egy osztályban?
a) Az attribútumok értékeket tárolnak, a metódusok pedig műveleteket végeznek
b) Az attribútumok konstruktorok, a metódusok pedig destruktorok
c) Az attribútumok csak osztályváltozók, a metódusok pedig példányváltozók
d) Nincs különbség, mindkettő ugyanazt a célt szolgálja
Válasz: a

6. Hogyan hozunk létre egy új osztálypéldányt Pythonban?
a) ClassName()
b) ClassName.new()
c) new ClassName()
d) ClassName.create()
Válasz: a

7. Mi a célja a Singleton patternnek?
a) Több példány létrehozása
b) Különböző típusú objektumok létrehozása
c) Az objektumok többszörös öröklődése
d) Egyetlen globálisan elérhető példány biztosítása
Válasz: d

8. Melyik Python kulcsszót használjuk az öröklődés megvalósításához?
a) class Child(Parent):
b) super
c) inherits
d) extends
Válasz: a

9. Mi a "class" kulcsszó szerepe Pythonban?
a) Osztály létrehozása
b) Fájl kezelés
c) Modul importálás
d) Függvény definiálás
Válasz: a

10. Mi a célja az Adapter design patternnek?
a) Objektumok gyorsabb létrehozása
b) Két inkompatibilis interfész összekapcsolása
c) Kód ismétlésének csökkentése
d) Programozási hibák automatikus javítása
Válasz: b

11. Milyen típusú a Factory design pattern?
a) Létrehozási
b) Szerkezeti
c) Viselkedési
d) Iteratív
Válasz: a

12. Miért használunk öröklődést (inheritance) az OOP-ban?
a) Az osztályok egyszerűbbé válnak
b) Kód újrafelhasználhatósága és kódmegosztás
c) Biztonsági okokból
d) Adatbázis optimalizálás
Válasz: b

13. Mi történik Pythonban, ha egy osztályban nem definiáljuk a init metódust?
a) A program hibát generál
b) Az osztály nem használható
c) Az osztály automatikusan kap egy alapértelmezett init metódust
d) Az osztály minden metódusa hibás lesz
Válasz: c

14. Mi a Singleton pattern alapvető tulajdonsága?
a) Több példány létrehozása
b) Különböző típusú objektumok létrehozása
c) Az objektumok többszörös öröklődése
d) Egyetlen globálisan elérhető példány biztosítása
Válasz: d

15. Melyik NEM egy Python beépített kivételkezelő szerkezet?
a) try...except
b) try...finally
c) try...catch
d) try...except...finally
Válasz: c

16. Mi a célja a Factory design patternnek?
a) Létrehozási
b) Szerkezeti
c) Viselkedési
d) Iteratív
Válasz: a

17. Milyen kijelentés igaz az absztrakt osztályokra Pythonban?
a) Absztrakt osztályokat lehet példányosítani
b) Absztrakt osztályokban minden metódusnak absztraktnak kell lennie
c) Absztrakt osztályokat nem lehet örökíteni
d) Absztrakt osztályok absztrakt metódusokat tartalmaznak, amelyeket a leszármazottaknak kell implementálniuk
Válasz: d

18. Mi az OOP célja az alábbiakból?
a) Adatbázis kezelés
b) Alacsony szintű memóriakezelés
c) Eljárási, procedurális programozás kiegészítése
d) Grafikus felhasználói felület kialakítása
Válasz: c

19. Mi a célja az Adapter design patternnek?
a) Objektumok gyorsabb létrehozása
b) Két inkompatibilis interfész összekapcsolása
c) Kód ismétlésének csökkentése
d) Programozási hibák automatikus javítása
Válasz: b

20. Mi a különbség az attribútum és a metódus között egy osztályban?
a) Az attribútumok értékeket tárolnak, a metódusok pedig műveleteket végeznek
b) Az attribútumok konstruktorok, a metódusok pedig destruktorok
c) Az attribútumok csak osztályváltozók, a metódusok pedig példányváltozók
d) Nincs különbség, mindkettő ugyanazt a célt szolgálja
Válasz: a

"""
from abc import ABC, abstractmethod
from datetime import datetime

class Utanfuto(ABC):
    def __init__(self, tipus, ar, teherbiras):
        self.tipus = tipus
        self.ar = ar
        self.teherbiras = teherbiras

    @abstractmethod
    def info(self):
        pass

class FekezettUtanfuto(Utanfuto):
    def info(self):
        return f"Fekezett Utánfutó: {self.tipus}, Ár: {self.ar}, Teherbírás: {self.teherbiras}"

class PonyvasUtanfuto(Utanfuto):
    def info(self):
        return f"Fekezett Utánfutó: self. {self.tipus}, Ár: {self.ar}, Teherbírás: {self.teherbiras}"


class Kolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.utanfutok = []

    def utanfuto_hozzaad(self, utanfuto):
        self.utanfutok.append(utanfuto)

    def info (self):
        for utanfuto in self.utanfutok:
            print(utanfuto.info)


class Kolcsonzes:
    def __init__(self):
        self.kolcsonzesek = []

    def ujKolcsonzes (self, kolcsonzo, utanfuto, datum):

        if dateime.sprtime(datum, "%Y-%m-%d" ) >= datetime.now():
            self.kolcsonzesek.append((kolcsonzo, utanfuto, datum))
            print(f"Kölcsönzés rögzítve: {kolcsonzo.nev}, {utanfuto.tipus}, {datum}")
        else:
            print("Érvénytelen dátum!")

    def kolcsonzes_lemondas(self, kolcsonzo, utanfuto, datum):
    # Ellenőrizzük, hogy létezik-e a foglalás és a dátum jövőbeni-e
    letezo_kolcsonzes = (kolcsonzo, utanfuto, datum) in self.kolcsonzesek
    jovo_dátum = datetime.strptime(datum, "%Y-%m-%d") >= datetime.now()
    if letezo_kolcsonzes and jovo_dátum:
        self.kolcsonzesek.remove((kolcsonzo, utanfuto, datum))
        print("Kölcsönzés lemondva.")
    else:
        print("Érvénytelen lemondás.")

    def kolcsonzesek_listazasa(self):
    print("Jelenlegi kölcsönzések:")
    for kolcsonzes in self.kolcsonzesek:
        print(f"{kolcsonzes[0].nev}, {kolcsonzes[1].tipus}, {kolcsonzes[2]}")



    def felhasznaloi_interfesz():
while True:
print("\nUtánfutó Kölcsönző Rendszer")
print("1. Új kölcsönzés")
print("2. Kölcsönzés lemondása")
print("3. Kölcsönzések listázása")
print("4. Kilépés")
valasztas = input("Válassz egy opciót: ")
if valasztas == "1":
    kolcsonzes.uj_kolcsonzes(kolcsonzo, fekezett, input("Add meg a dátumot (YYYY-MM-DD): "))
elif valasztas == "2":
    kolcsonzes.kolcsonzes_lemondas(kolcsonzo, fekezett, input("Add meg a lemondani kívánt dátumot(YYYY - MM - DD): "))
    elif valasztas == "3":
    kolcsonzes.kolcsonzesek_listazasa()
    elif valasztas == "4":
    print("Kilépés a programból.")
    break
    else:
    print("Érvénytelen opció!")


kolcsonzo = Kolcsonzo("Példa Kölcsönző")
fekezett = FekezettUtanfuto("Nagy teher", 10000, 2000)
ponyvas = PonyvasUtanfuto("Hosszú", 8000, 1500)

kolcsonzo.utanfuto_hozzaad(fekezett)
kolcsonzo.utanfuto_hozzaad(ponyvas)

kolcsonzes = Kolcsonzes()
kolcsonzes.uj_kolcsonzes(kolcsonzo, fekezett, "2024-03-10")
kolcsonzes.uj_kolcsonzes(kolcsonzo, ponyvas, "2024-04-15")


