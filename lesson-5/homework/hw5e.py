
year=int(input("yilni kiriting:"))
if year%4==0  and year%100!=0 or year%400==0:
    print("kabisa yili")
else:
    print("Kabisa yili emas")


son =int(input("sonni kiriting:"))
if son%2!=0:
    print("weird")
elif son%2==0 and 2<=son<=5:
    print("Not weird")
elif son%2==0 and 6<=son<=20:
    print("Weird")
elif son%2==0 and 20<son<100:
    print("Not weird")
else:
    print("Katta son")


son1=int(input("birinchi sonni kiriting:"))
son2=int(input("ikkinchi sonni kiriting:"))
if son1%2!=0:
    son1+=1
if son2%2!=0:
    son2-=1
print(list(range(son1,son2+1,2)))

son1=int(input("birinchi sonni kiriting:"))
son2=int(input("ikkinchi sonni kiriting:"))
numbers=list(range(son1+(son1%2),son2+1-(son2%2),2))
print(numbers)
