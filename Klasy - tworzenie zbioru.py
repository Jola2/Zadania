class Set:
    def __init__(self, pojemnosc):
        setattr(self, 'pojemnosc', pojemnosc)
        self._liczby = []
        self._rozmiar = len(self._liczby)

    @property
    def pojemnosc(self):
        return self._pojemnosc

    @pojemnosc.setter
    def pojemnosc(self, pojemnosc):
        if pojemnosc in range(0, 101):
            self._pojemnosc = pojemnosc
        else:
            raise ValueError('Maksymalna liczba elementów możliwych do przechowania to 100')

    @property
    def liczby(self):
        return self._liczby

    @property
    def rozmiar(self):
        return self._rozmiar

    def dodaj_element(self, nowy_element):
        if nowy_element in self._liczby:
            pass
        elif self._rozmiar == self._pojemnosc:
            print('Liczba nie została dodana. Przekroczono pojemosc')
        else:
            self._liczby.append(nowy_element)
            self._liczby.sort()
            self._rozmiar += 1

    def znajdz(self, element):
        if element in self._liczby:
            return self._liczby.index(element)
        else:
            print("Nie znaleziono takiego elementu")
            return -1

    def pisz(self):
        print(f"Rozmiar:{self._rozmiar}\nPojemnosc:{self._pojemnosc}\nLista przechowywanych elementów:{self._liczby}")

    def usun_element(self, element):
        if element not in self._liczby:
            pass
        else:
            self._liczby.remove(element)

    def dodaj(self, zbior_02):
        self._liczby.extend(value for value in zbior_02.liczby if value not in self._liczby)
        return self._liczby.sort()

    def minus(self, zbior_02):
        return [value for value in self._liczby if value not in zbior_02.liczby]

    def przeciecie(self, zbior_02):
        return [value for value in self._liczby if value in zbior_02.liczby]

def main():
    zbior_01 = Set(98)
    zbior_02 = Set(70)
    zbior_01 = Set(98)
    zbior_02 = Set(70)
    zbior_01.dodaj_element(5)
    zbior_01.dodaj_element(4)
    zbior_01.dodaj_element(3)
    zbior_01.dodaj_element(2)
    zbior_01.dodaj_element(1)
    zbior_01.dodaj_element(15)
    zbior_01.pisz()
    zbior_02.dodaj_element(1)
    zbior_02.dodaj_element(3)
    zbior_02.dodaj_element(5)
    zbior_02.dodaj_element(7)
    zbior_02.pisz()
    print(zbior_01.znajdz(6))
    print(zbior_01.usun_element(3))
    zbior_01.dodaj(zbior_02)
    zbior_01.pisz()
    print(zbior_01.minus(zbior_02))
    print(zbior_01.przeciecie(zbior_02))

if __name__ == "__main__":
    main()

