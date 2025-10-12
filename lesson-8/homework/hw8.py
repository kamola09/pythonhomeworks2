try:
    a = int(input("Sonni kiriting: "))
    b = int(input("Yana bir son kiriting: "))
    natija = a / b
    print("Natija:", natija)
except ZeroDivisionError:
    print(" Nolga bo‘lib bo‘lmaydi!")

try:
    a = int(input("Butun son kiriting: "))
    print("Kiritilgan son:", a)
except ValueError:
    print(" Faqat butun son kiriting!")

try:
    fayl = input("Fayl nomini kiriting: ")
    with open(fayl, "r") as f:
        mazmun = f.read()
        print("Fayl mazmuni:\n", mazmun)
except FileNotFoundError:
    print(" Fayl topilmadi!")

try:
    a = 5
    b = "a"
    natija = a + b
except TypeError:
    print(" Tur mos emas, raqam bilan matnni qo‘shib bo‘lmaydi!")

try:
    file = input("Fayl nomini kiriting: ")
    matn = input("Faylga yoziladigan matnni kiriting: ")
    with open(file, "w") as f:
        f.write(matn)
        print("Faylga matn muvaffaqiyatli yozildi.")
except PermissionError:
    print(" Sizga bu faylga yozish uchun ruxsat yo‘q.")

try:
    sonlar = list(input("Sonlar kiriting (masalan: 12345): "))
    index = int(input("Indeksni kiriting: "))
    print("Tanlangan son:", sonlar[index])
except IndexError:
    print(" Bunday indeks mavjud emas!")

try:
    while True:
        print("Dastur ishlayapti... To‘xtatish uchun Ctrl + C bosing.")
except KeyboardInterrupt:
    print("\n❗ Foydalanuvchi dasturni to‘xtatdi.")

try:
    x = 10 / 0
except ArithmeticError:

try:
    with open("example.txt", "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError:
    print(" Kodlashda xatolik (UnicodeDecodeError) yuz berdi.")

try:
    son = 5
    son.append(3)
except AttributeError:
    print(" Xatolik: 'int' tipida append metodi yo‘q.")

with open("example.txt", "r") as file:
    print(file.read())

n = int(input("Nechta qatorni o‘qish kerak: "))
with open("example.txt", "r") as file:
    for i in range(n):
        qator = file.readline()
        if not qator:
            break
        print(qator.strip())


with open("example.txt", "a") as file:
    file.write("\nBu yangi matn\n")

with open("example.txt", "r") as file:
    content = file.read()
print(content)

n = int(input("Nechta oxirgi qatorni o‘qish kerak: "))
with open("example.txt", "r") as file:
    lines = file.readlines()
for line in lines[-n:]:
    print(line.strip())

with open("example.txt", "r") as file:
    lines = file.readlines()
print(lines)

with open("example.txt", "r") as file:
    content = ""
    for line in file:
        content += line
print(content)

with open("example.txt", "r") as file:
    lines = file.readlines()
print(lines)

with open("example.txt", "r") as file:
    words = file.read().split()

max_len = len(max(words, key=len))
max_words = [word for word in words if len(word) == max_len]

print(max_len, max_words)

count = 0
with open("example.txt", "r") as file:
    for line in file:
        count += 1
print("Qatorlar soni:", count)

from collections import Counter

with open("example.txt", "r") as file:
    words = file.read().split()
    word_count = Counter(words)

for soz, soni in word_count.items():
    print(soz, "-", soni)

import os

file_size = os.path.getsize("example.txt")
print("Fayl hajmi:", file_size, "bayt")

my_list = ["Python", "is", "fun"]

with open("list.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")
print("Ro‘yxat faylga yozildi.")

with open("example.txt", "r") as original, open("copy.txt", "w") as new_file:
    new_file.write(original.read())

print("Fayl nusxalandi.")

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

import random

with open("example.txt", "r") as file:
    lines = file.readlines()
    random_line = random.choice(lines)
print("Tasodifiy qator:", random_line.strip())

file = open("example.txt", "r")
print("Fayl yopilganmi?", file.closed)
file.close()
print("Fayl yopilganmi?", file.closed)

with open("example.txt", "r") as file:
    lines = [line.strip() for line in file]

print(lines)

with open("example.txt", "r") as file:
    text = file.read().replace(",", " ")  # vergulni bo‘shliq bilan almashtiramiz
    words = text.split()
    print("So‘zlar soni:", len(words))

import glob

chars = []
for filename in glob.glob("*.txt"):
    with open(filename, "r") as file:
        chars.extend(list(file.read()))

print("Belgilar soni:", len(chars))

import string

for letter in string.ascii_uppercase:  # A dan Z gacha
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is file {letter}.txt\n")

print("A.txt dan Z.txt gacha fayllar yaratildi.")

import string

letters = string.ascii_lowercase  # a-z
n = 5  # har qatorda nechta harf bo‘lsin

with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        file.write(letters[i:i+n] + "\n")

print("Harflar faylga yozildi.")



