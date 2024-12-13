import json

class Person:
    def __init__(self, imie, nazwisko, adres, kod_pocztowy, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.kod_pocztowy = kod_pocztowy
        self.pesel = pesel

    def to_dict(self):

        return {
            "imie": self.imie,
            "nazwisko": self.nazwisko,
            "adres": self.adres,
            "kod_pocztowy": self.kod_pocztowy,
            "pesel": self.pesel
        }

    @staticmethod
    def from_dict(data):

        return Person(data["imie"], data["nazwisko"], data["adres"], data["kod_pocztowy"], data["pesel"])

    def save_to_json(self, filename):

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_json(filename):

        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return Person.from_dict(data)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, {self.adres}, {self.kod_pocztowy}, PESEL: {self.pesel}"


if __name__ == "__main__":
    osoba = Person("Jan", "Kowalski", "ul. Krakowska 10, Warszawa", "00-123", "85010112345")

    # Zapis do JSON
    osoba.save_to_json("osoba.json")
    print("Dane zapisane do 'osoba.json'.")

    # ODCZYT z JSON
    nowa_osoba = Person.load_from_json("osoba.json")
    print("Dane odczytane z:")
    print(nowa_osoba)
