class Shaxs:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def get_info(self):
        return f"{self.ism} {self.familiya}"


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def __str__(self):
        return self.nomi


class Talaba(Shaxs):
    def __init__(self, ism, familiya):
        super().__init__(ism, familiya)
        self.fanlar = []

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz"

    def get_info(self):
        fanlar = [fan.nomi for fan in self.fanlar]
        return f"Talaba: {self.ism} {self.familiya}, Fanlar: {fanlar}"


class Professor(Shaxs):
    def __init__(self, ism, familiya, kafedra):
        super().__init__(ism, familiya)
        self.kafedra = kafedra

    def get_info(self):
        return f"Professor: {self.ism} {self.familiya}, Kafedra: {self.kafedra}"


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, login):
        super().__init__(ism, familiya)
        self.login = login

    def get_info(self):
        return f"Foydalanuvchi: {self.login}"


class Admin(Foydalanuvchi):
    def ban_user(self):
        print("Foydalanuvchi bloklandi")

    def get_info(self):
        return f"Admin: {self.login}"


matematika = Fan("Matematika")
fizika = Fan("Fizika")

talaba1 = Talaba("Ali", "Valiyev")

talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(fizika)

print(talaba1.get_info())

talaba1.remove_fan(fizika)

print(talaba1.get_info())

prof = Professor("Anvar", "Karimov", "IT")
print(prof.get_info())

admin = Admin("Admin", "Adminov", "admin01")
print(admin.get_info())
admin.ban_user()