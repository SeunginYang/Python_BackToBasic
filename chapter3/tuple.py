days = ("Mon", "Tue", "Wed" ,"Thr", "Mon", "Mon", "Mon")

print(days.count("Mon"))


list(days)           # if you want to change tuple to list this is how convert from tuple to list do it.
print(days)

print(days[-5])

sample_set = set(days) # convert the list to set, you can remove all the duplicates element
print(sample_set)      # However "Sets" are unordered, A set itself may be modified but the elements contained in the set must be of an immutable type.
