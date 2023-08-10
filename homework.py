#HOMEWORK NUM-1
# num = 1
# num2 = 0
# while num < 100:
#     print("რიცხვი",num,"კენტია")
#     num = num + 2
# while num2< 101:
#     print("რიცხვი",num2,"ლუწია")
#     num2 = num2 + 2

#HOMEWORK NUM-2
# age = int(input("შეიყვანე შენი ასაკი: "))
# dad_age = int(input("შეიყვანე მამაშენის ასაკი: "))
# if dad_age == age * 2:
#     print("bingo")
# else:
#     print("mouse")

#HOMEWORK NUM-3
age = int(input("შიეყვანე შენი ასაკი: "))
sqesi = input("რა სქესს წარმოადგენთ: ")

if age >= 65:
    print("თქვენ ხართ ხანში შესული ამიტომ")
else:
    print("თქვენთვის ჯერ პენსია ადრეა *პანჩური* ")

if sqesi == "ქალი" or sqesi == "მამაკაცი" or sqesi == "ქალბატონი" or sqesi == "კაცი":
    print("თქვენ გეკუთვნით პენსია")
else:
    print("შენ არხარ ამქვეყნიური არსება *პანჩური* ")