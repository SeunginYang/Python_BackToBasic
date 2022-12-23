pocketMoney = 10000
pm = pocketMoney
print(pm)
user = "Chris"

if pm == 15000:
    print(f"{user} can take a taxi")
elif pm <=10000:
    print(f"{user} can take a bus")
elif pm <=5000:
    print(f"{user} can take a metro")
elif pm <=3000:
    print(f"{user} can take a bycicle")
else:
    print(f"{user}, you should walk")