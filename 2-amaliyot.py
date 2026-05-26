print("python".capitalize())
print("dasturlash".capitalize())

print("HELLO WORLD".lower())
print("PYTHON".lower())

print("salom".upper())
print("uzbek".upper())

print("python".center(15, "-"))
print("AI".center(10, "*"))

print("banana".count("a"))
print("kitoblar".count("o"))

print("hello".encode())
print("Python".encode("utf-8"))

print("music.mp3".endswith(".mp3"))
print("video.mp4".endswith(".avi"))

print("A\tB\tC".expandtabs(4))
print("1\t22\t333".expandtabs(6))

print("dastur".find("t"))
print("python".find("z"))

print("Mening ismim {}".format("Jasur"))
print("Narx: {:.1f}".format(25.678))

print("{a} + {b}".format_map({'a': 5, 'b': 10}))
print("Yosh: {y}".format_map({'y': 20}))

print("kitob".index("o"))
print("salom".index("a"))

print("Python2025".isalnum())
print("Python_2025".isalnum())

print("Salom".isalpha())
print("Hello123".isalpha())

print("ABC123".isascii())
print("Ğ".isascii())

print("2025".isdecimal())
print("20.5".isdecimal())

print("999".isdigit())
print("3kv".isdigit())

print("myVariable".isidentifier())
print("123abc".isidentifier())

print("salom".islower())
print("Salom".islower())

print("12345".isnumeric())
print("Ⅷ".isnumeric())

print("Hello!".isprintable())
print("Hello\n".isprintable())

print("     ".isspace())
print(" salom ".isspace())

print("Hello World".istitle())
print("hello World".istitle())

print("PYTHON".isupper())
print("Python".isupper())

print(",".join(["olma", "anor", "behi"]))
print("-".join(["2025", "05", "16"]))

print("AI".ljust(10, "-"))
print("Hi".ljust(8, "*"))

print("SALOM".lower())
print("PYTHON DARSI".lower())

print("   kitob".lstrip())
print("###python".lstrip("#"))

print(str.maketrans("a", "o"))
print(str.maketrans("xyz", "123"))

print("Men futbolni yaxshi koraman".partition("futbolni"))
print("a-b-c-d".partition("-"))

print("salom".replace("s", "S"))
print("qizil mashina".replace("qizil", "kok"))

print("banana".rfind("a"))
print("salom dunyo".rfind("o"))

print("python".rindex("h"))
print("banana".rindex("n"))

print("AI".rjust(10, "*"))
print("Hello".rjust(12))

print("a,b,c,d".rpartition(","))
print("1-2-3".rpartition("-"))

print("olma, anor, behi".rsplit(", ", 2))
print("one two three".rsplit(" ", 1))

print("salom   ".rstrip())
print("wow!!!".rstrip("!"))

print("olma anor behi".split())
print("2025/05/16".split("/"))

print("Hello\nPython".splitlines())
print("1\n2\n3".splitlines())

print("Python".startswith("Py"))
print("Java".startswith("P"))

print("   salom   ".strip())
print("***AI***".strip("*"))

print("PyThOn".swapcase())
print("HeLLo".swapcase())

print("python darslari".title())
print("sun moon".title())

print("hello".translate(str.maketrans("h", "y")))
print("apple".translate(str.maketrans("a", "u")))

print("salom".upper())
print("kitob".upper())

print("7".zfill(4))
print("99".zfill(5))