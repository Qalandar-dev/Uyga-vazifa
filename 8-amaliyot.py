#1
def ortacha_baho(ism, *baho):
    return f"{ism}ning o'rtacha bahosi: {sum(baho) / len(baho)}"

print(ortacha_baho("Ali", 5, 4, 5, 3))

#2
def mahsulot_yaratish(nomi, **malumotlar):
    malumotlar["nomi"] = nomi
    return malumotlar

telefon = mahsulot_yaratish(
    "iPhone 15",
    narx=1200,
    rang="Qora",
    brend="Apple",
    xotira="256 GB"
)
print(telefon)