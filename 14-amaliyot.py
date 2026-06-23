from datetime import datetime, timedelta

today = datetime.today()

for i in range(10):
    sana = today + timedelta(weeks=2 * i)
    print(sana.strftime("%Y-%m-%d"))

from datetime import datetime

today = datetime.today()

ramazon = datetime(2027, 2, 8)
qurbon = datetime(2026, 5, 27)

print("Ramazongacha:", (ramazon - today).days, "kun")
print("Qurbon hayitigacha:", (qurbon - today).days, "kun")

from datetime import date

def yosh_hisobla():
    yil = int(input("Tug'ilgan yil: "))
    oy = int(input("Tug'ilgan oy: "))
    kun = int(input("Tug'ilgan kun: "))

    tugilgan = date(yil, oy, kun)
    bugun = date.today()

    farq = bugun - tugilgan

    yil = farq.days // 365
    oy = (farq.days % 365) // 30
    kun = (farq.days % 365) % 30

    print(f"{yil} yil, {oy} oy, {kun} kun o'tgan.")

yosh_hisobla()

telefon = input("Telefon raqamini kiriting: ")

if telefon.startswith("+998") and len(telefon) == 13 and telefon[1:].isdigit():
    print("To'g'ri raqam")
else:
    print("Noto'g'ri raqam")


def url_top(matn):
    sozlar = matn.split()

    for soz in sozlar:
        if soz.startswith("http://") or soz.startswith("https://"):
            print(soz)


matn = "Saytlar: https://google.com va https://youtube.com"

url_top(matn)