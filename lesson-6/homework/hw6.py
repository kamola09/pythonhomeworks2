1. Modify String with Underscores
soz = input("So'zni kiriting: ")
result = ""
unli_harflar = "aeoui"

for i in range(len(soz)):
    result += soz[i]
    if (i+1) % 3 == 0 and i != len(soz) - 1:
        result += "_"
print(result)


Izoh: Har uchinchi harfdan keyin _ qo‘shiladi, oxirgi harfdan keyin qo‘shilmaydi.

2. Integer Squares Exercise
number1 = int(input("Sonni kiriting: "))
number2 = int(input("Sonni kiriting: "))

for i in range(number1, number2):
    print(i**2)


Izoh: number1 dan number2-1 gacha bo‘lgan sonlarning kvadratlari chiqariladi.

3. Loop-Based Exercises
Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

Exercise 2: Print the pattern
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()

Exercise 3: Sum of numbers from 1 to n
n = int(input("Sonni kiriting: "))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

Exercise 4: Display numbers divisible by 2 from 1 to n
n = int(input("Sonni kiriting: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

Exercise 5: Display numbers from a list using a loop
n = list(map(int, input("Sonlarni kiriting: ").split()))
for i in n:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)

Exercise 6: Count total number of digits in a number
son = input("Sonni kiriting: ")
count = 0
for i in son:
    count += 1
print(count)

Exercise 7: Print reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

Exercise 8: Print list in reverse order
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

Exercise 9: Display numbers from -10 to -1
for i in range(-10, 0):
    print(i)

Exercise 10: Display message “Done” after successful loop execution
for i in range(1,5):
    print(i)
else:
    print("Done")

Exercise 11: Print all prime numbers within a range
son1 = int(input("Sonni kiriting: "))
son2 = int(input("Sonni kiriting: "))

for i in range(son1, son2+1):
    if i > 1:
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            print(i)

Exercise 12: Display Fibonacci series up to 10 terms
a, b = 0, 1
print("Fibonacci ketma-ketligi:")
for _ in range(10):
    print(a, end="  ")
    a, b = b, a + b

Exercise 13: Find factorial of a given number
kopaytma = 1
son1 = int(input("Sonni kiriting: "))
for i in range(1, son1+1):
    kopaytma *= i
print(kopaytma)

Exercise 14: Return uncommon elements of two lists
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    
    for elem in list1:
        if elem not in c2 or c1[elem] > c2.get(elem, 0):
            result.append(elem)
            c1[elem] -= 1
    
    for elem in list2:
        if elem not in c1 or c2[elem] > c1.get(elem, 0):
            result.append(elem)
            c2[elem] -= 1
    
    return result

# Misol:
list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(uncommon_elements(list1, list2))  # [1, 1, 3, 4]
