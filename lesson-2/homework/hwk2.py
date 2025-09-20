# 1. Age Calculator
name = input("Ismingizni kiriting: ")
date_birth = int(input("Tug'ilgan yilingizni kiriting: "))
current = 2025
age = current - date_birth
print(f"Hello {name}, you are {age} years old")

# 2. Extract Car Names (LMaasleitbtui)
txt = 'LMaasleitbtui'
print(txt[0::2])   # Juft indekslardan oladi
print(txt[1::3])   # 1-indeksdan boshlab har 3-qadam

# 3. Extract Car Names (MsaatmiazD)
txt = 'MsaatmiazD'
part1 = txt[0::2]   # "Matad"
part2 = txt[1::2]   # "samiz"
word = part1[-1] + part2[1:4] + part2[-1]  # D + ama + s
print(word)   # Damas

# 4. Extract Residence Area
txt = "I'am John. I am from London"
word = txt.find("London")
print(txt[word:])   # "London"dan boshlab chiqadi

# 5. Reverse String
text = input("So'zingizni kiriting: ")
print(text[::-1])   # Matnni teskari chiqaradi

# 6. Count Vowels
matn = input("So'zingizni kiriting: ")
print("a:", matn.lower().count("a"))
print("e:", matn.lower().count("e"))
print("i:", matn.lower().count("i"))
print("o:", matn.lower().count("o"))
print("u:", matn.lower().count("u"))

# 7. Find Maximum Value
son1 = int(input("1-soningizni kiriting: "))
son2 = int(input("2-soningizni kiriting: "))
son3 = int(input("3-soningizni kiriting: "))
print("Eng katta son:", max(son1, son2, son3))

# 8. Check Palindrome
matn = input("So'zingizni kiriting: ")
teskari = matn[::-1]
if teskari == matn:
    print("Palindrom")
else:
    print("Palindrom emas")

# 9. Extract Email Domain
matn = input("Email manzilni kiriting: ")
values = matn.find('@')
print(matn[values+1:])   # @ belgisidan keyingi qismini chiqaradi

# 10. Generate Random Password (time kutubxonasi yordamida)
import time

harflar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sonlar = "0123456789"
belgilar = "!@#$%^&*?"
hammasi = harflar + sonlar + belgilar

parol = ""
uzunlik = int(input("Parol uzunligini kiriting: "))

for i in range(uzunlik):
    indeks = int(time.time() * 1000) % len(hammasi)  # vaqt asosida indeks tanlaydi
    parol += hammasi[indeks]  # shu indeksdagi belgini parolga qo‘shadi

print("Yaratilgan parol:", parol)
