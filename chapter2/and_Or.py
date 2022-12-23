age = int(input("How old are you"))

print("user answer", age)

print(type(age))


if age < 18:
    print("You can't smoke")
elif age <=19 and  age <100:
    print("Responsiblity will comes with what you decide")
elif age == 30 or age == 40:
    print("You better be get a job at least")
else:
    print("You are an Adult")

