daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# print(daysOfWeek.count("Sat","Tue"))  # on the method argument(parameter) take exactly only 1.
print(daysOfWeek.count("Sat")) 

daysOfWeek.reverse()
print(daysOfWeek)

daysOfWeek.clear()
daysOfWeek.append("Tue")
print(daysOfWeek)
daysOfWeek.insert(0, "Mon")
print(daysOfWeek)

days_of_week = ["Wed", "Thu", "Fri", "Sat", "Sun"]

daysOfWeek.extend(days_of_week)     #add, insert method only can add up one argument only, therefore you can use the another list and extend both or among lists, in the other hand you can also use the "For Loops"
print(daysOfWeek)

