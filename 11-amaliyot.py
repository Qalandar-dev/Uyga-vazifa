class Avto:
    def __init__(self, model, rang, korobka, narh, kilometr=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = kilometr

    def get_info(self):
        return (f"Model: {self.model}, Rang: {self.rang}, "
                f"Korobka: {self.korobka}, Narh: {self.narh}$, "
                f"Kilometr: {self.kilometr} km")

    def update_km(self, km):
        self.kilometr += km


class Avtosalon:
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtolar = []

    def add_avto(self, avto):
        self.avtolar.append(avto)

    def get_avtolar(self):
        if not self.avtolar:
            return "Avtosalonda avtomobillar mavjud emas."

        info = f"{self.nomi} avtosalonidagi avtomobillar:\n"
        for avto in self.avtolar:
            info += avto.get_info() + "\n"
        return info



avto1 = Avto("Malibu", "Qora", "Avtomat", 30000)
avto2 = Avto("Cobalt", "Oq", "Mexanik", 15000)


avto1.update_km(5000)

print(avto1.get_info())
print(avto2.get_info())


salon = Avtosalon("Premium Auto", "Toshkent")

salon.add_avto(avto1)
salon.add_avto(avto2)

print( salon.get_avtolar())

print("Avto1 __dict__:")
print(avto1.__dict__)

print("Avto klassi metodlari:")
print(dir(Avto))

print("str klassi metodlari:")
print(dir(str))

print("int klassi metodlari:")
print(dir(int))