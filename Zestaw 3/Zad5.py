class Stan:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.przejscia = {}

    def dodaj_przejscie(self, wejscie, stan_docelowy, wyjscie):
        self.przejscia[wejscie] = (stan_docelowy, wyjscie)

    def wykonaj_przejscie(self, wejscie):
        if wejscie in self.przejscia:
            stan_docelowy, wyjscie = self.przejscia[wejscie]
            return stan_docelowy, wyjscie
        else:
            raise ValueError(f"Brak przejścia dla wejścia '{wejscie}' w stanie '{self.nazwa}'")


class AutomatMealy:
    def __init__(self, stan_poczatkowy):
        self.stan_aktualny = stan_poczatkowy

    def przetworz_wejscie(self, lista_wejsc):
        wynik = []
        for wejscie in lista_wejsc:
            try:
                self.stan_aktualny, wyjscie = self.stan_aktualny.wykonaj_przejscie(wejscie)
                wynik.append(wyjscie)
                print(f"Wejście: {wejscie} -> Stan: {self.stan_aktualny.nazwa}, Wyjście: {wyjscie}")
            except ValueError as e:
                print(e)
                break
        return wynik


stan_A = Stan("A")
stan_B = Stan("B")
stan_C = Stan("C")

stan_A.dodaj_przejscie("0", stan_A, "x")
stan_A.dodaj_przejscie("1", stan_B, "y")

stan_B.dodaj_przejscie("0", stan_A, "z")
stan_B.dodaj_przejscie("1", stan_C, "w")

stan_C.dodaj_przejscie("0", stan_C, "v")
stan_C.dodaj_przejscie("1", stan_A, "u")

#Początek
automat = AutomatMealy(stan_A)

wejscia = ["1", "0", "1", "1", "0", "1"]
wynik = automat.przetworz_wejscie(wejscia)

print("\nWyjście:", wynik)
