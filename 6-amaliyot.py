#1
# while True:
#     rang = input("Svetofor qaysi rangda? (qizil, sariq, yashil): ")
#     if rang in ['qizil', 'sariq', 'yashil']:
#         print("Raxmat, to'g'ri keladi")
#         break
#     else:
#         print("Bu xato rang. Qaytadan urinib ko'ring.\n")

#2
# son = int(input("1 dan 10gacha son tanlang"))
# togri_son = 5
# while son != togri_son:
#     print("Noto'g'ri")
#     son = int(input("Qaytadan urinib ko'ring"))
# else:
#     print("Tabriklaymiz, siz topdingiz")

#3
# ismlar = []
# print("Yaqin do'stlaringiz ro'yhatini tuzamiz.")
# n=1
# while True:
#     savol = f"{n}--do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (yes/no)")
#     if javob == "yes":
#         n+=1
#         continue
#     else:
#         break
#
# print("\nDo'stlaringizni ro'yxati:")
# for ism in ismlar:
#             print(ism.title())

#4
# USD = 12600
# print("Valyuta ayriboshlash")
# print("Dasturdan chiqish uchun 'exit' deb yozing.\n")
# while True:
#     som = input("So'm qiymatini kiriting (yoki exit):")
#     if som == "exit":
#         print("Dastur to'xtatildi.")
#         break