import json
with open("students.json","r",encoding="utf-8")as file:
    data=json.load(file)

for student in data:
    print(f"Name:{student["name"]},Age:{student["Age"]},Course:{student["Course"]}")

import requests

API_KEY = "b3c2a123f6d09e1a8bcd8765abcd1234"  # bu joyga o'zingga berilgan API key yoz
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"\n Weather in {city}:")
    print(" Temperature:", data['main']['temp'], "°C")
    print(" Humidity:", data['main']['humidity'], "%")
    print(" Description:", data['weather'][0]['description'])
else:
    print(" Error:", data['message'])

import json
def read_books():
    with open("books_json","r",encoding="utf-8") as f:
        return json.load(f)
def write_books(books):
    with open("books_json","w",encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)
while True:
    print("\n1. Add book\n2. Update book\n3.  Delete book\n4.  Show all\n5. Exit")
    choice=input("Choose(1-5): ")
    books= read_books()

if choice=="1":
    title=input("Title:")
    author=input("author:")
    books.append({"title":title,"author":author})
    write_books(books)
    print("book append sucessfully")


elif choice=="2":
    old=input("old title:")
    new=input("new title:")
    found=False
    for book in books:
        if book["title"]==old:
            book["title"]=new
            found=True
        if found:
            print("add sucessfully")
        else:
            print("not found")

elif choice=="3":
    title=input("Qaysi kitobni o'chirmoqchisiz:")
    books=[b for b in books if b["title"]!=title]
    write_books(books)
    print("Book deleted successfully")
elif choice==4:
    for b in books:
        print(f"b{"title"}-b{"author"}")
elif choice==5:
    print("Dastur to'xtatildi")
    break


import requests
import random

API_KEY = "abcd1234"  
genre = input("Enter genre (Action, Comedy, Drama, etc): ")

url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}"

response = requests.get(url)
data = response.json()

if data["Response"] == "True":
    movies = data["Search"]
    movie = random.choice(movies)
    print(f" Recommended movie: {movie['Title']} ({movie['Year']})")
else:
    print("No movies found.")
