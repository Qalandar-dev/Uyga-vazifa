#1
sozlar = ["olma", "banan", "gilos", "shaftoli"]

uzunliklar = list(map(len, sozlar))

print(uzunliklar)

#2
sonlar = [10, 24, 30, 41, 50]

satrlar = list(map(str, sonlar))

print(satrlar)

#3
sozlar = ["olma", "banan", "anor", "uzum", "gilos"]

natija = list(filter(lambda x: x[0].lower() in "aeiouo‘", sozlar))

print(natija)

#4
sonlar = [12, 345, 6789, 100, 99, 456]

natija = list(filter(lambda x: 100 <= x <= 999, sonlar))

print(natija)

#5
ismlar = ["Ali", "Vali", "Hasan"]

natija = list(map(lambda x: "Mr. " + x, ismlar))

print(natija)

#6
sonlar = [1, 2, 3, 4, 5, 6, 7, 8]

juftlar = filter(lambda x: x % 2 == 0, sonlar)
natija = list(map(lambda x: x * 10, juftlar))

print(natija)