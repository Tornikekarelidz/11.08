#HOMEWORK NUM-1 პირველი ვერსია (ბანძი)
num = 1
num2 = 0
while num < 100:
    print("რიცხვი - ",num,"- კენტია")
    num = num + 2
while num2< 101:
    print("რიცხვი -",num2,"- ლუწია")
    num2 = num2 + 2

# HOMEWORK NUM-1 მეორე ვერსია (უკეთესი)
num = 0
while num < 100:
    if num == 1:
        print(num)
    else:
        print("ეს რიცხვი -",num + 1,"- კენტია")
    if num == 1:
        print(num)
    else:
        print("ეს რიცხვი -",num + 2,"- ლუწია")
        num = num + 2    
    

# HOMEWORK NUM-2
age = int(input("შეიყვანე შენი ასაკი: "))
dad_age = int(input("შეიყვანე მამაშენის ასაკი: "))
if dad_age == age * 2:
    print("bingo")
else:
    print("mouse")

# # HOMEWORK NUM-3
age = int(input("შიეყვანე შენი ასაკი: "))
if age >= 65:
    print("თქვენ ხართ ხანში შესული")
else:
    print("თქვენთვის ჯერ პენსია ადრეა *პანჩური* ")

sqesi = input("რა სქესს წარმოადგენთ: ")
if sqesi == "ქალი" or sqesi == "მამაკაცი" or sqesi == "ქალბატონი" or sqesi == "კაცი":
    print("თქვენ გეკუთვნით პენსია")
else:
    print("შენ არაამქვეყნიური არსება ხარ *პანჩური* ")