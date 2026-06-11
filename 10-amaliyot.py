#1
class User:
    def __init__(self, ism, foydalanuvchi_ismi, email, parol):
        self.ism = ism
        self.foydalanuvchi_nomi = foydalanuvchi_ismi
        self.email = email
        self.parol = parol

    def get_info(self):
        return f"Foydalanuvchi: {self.ism} (@{self.foydalanuvchi_nomi}). Email: {self.email} parol: {self.parol}"

    def get_email(self):
        return self.email
    def get_parol(self):
        return self.parol
    def get_ism(self):
        return self.ism
user1 = User("Qalandar", "qalandar_dev", "qalandar@email.com", "qwert123")

print(user1.get_info())

#2
class Foydalanuvchi:
    def __init__(self, ism, foydalanuvchi_nomi, email):
        self.foydalanuvchi_nomi = foydalanuvchi_nomi
        self.ism = ism
        self.email = email

    def get_info(self):
        return f"Foydalanuvchi: {self.foydalanuvchi_nomi}, Ismi: {self.ism}, Email: {self.email}"

user1 = Foydalanuvchi("Qalandar Yo'ldoshov", "qalandar_dev", "qalandar@email.com")
print(user1.get_info())

#3
class User:
    def __init__(self, ism, foydalanuvchi_nomi, email, parol):
     self.ism = ism
     self.foydalanuvchi_nomi = foydalanuvchi_nomi
     self.email = email
     self.parol = parol

user1 = User("Qalandar", "qalandar_dev", "qalandar@example.com", "pass123")
user2 = User("Anvar", "anvar_99", "anvar@mail.com", "anvarjon77")
user3 = User("Dilnoza", "dilnoza_ai", "dilnoza@tech.uz", "secure_pwd")

print(user1.ism)
print(user2.parol)