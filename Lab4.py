#Exercice 1 : Student Grades Analysis

print("-----Exercise1-----")
students = {
"Alice": [85, 78, 92],
"Bob": [79, 74, 81],
"Charlie": [91, 82, 85],
"David": [76, 85, 83],
"Eve": [88, 79, 92]
}
#Task 1
print("-----Task1-----")
average = {}
for k,v in students.items():
    average[k] = round(sum(v) / len(v),1)
print(average)
#Task 2
print("-----Task2-----")
highest = max(average.values())
highest_student = max(average, key = average.get)
print(f"{highest_student} has the highest grades which is {highest}.")
#Task 3
print("-----Task3-----")
lowest = min(average.values())
lowest_student = min(average, key = average.get)
print(f"{lowest_student} has the lowest grades which is {lowest}.")
#Task 4
print("-----Task4-----")
students["Frank"] = [80, 90, 85]
print(students)

print()
#Exercise 2 : Product Inventory Management
print("-----Exercise2-----")
inventory = {
"apple": (50, 0.5),
"banana": (100, 0.2),
"orange": (75, 0.3),
"pear": (20, 0.4)
}
#Task 1
print("-----Task1-----")
for k,v in inventory.items():
    item = v[0]
    price = v[1]
    print(f"{k} with {item} items priced at ${price} each.")
#Task 2
print("-----Task2-----")
price_each = {}
for k,v in inventory.items():
    price_each[k] = v[0]*v[1]
#print(price_each)
total_values = sum(price_each.values())
print(f"The total value of the inventory is ${total_values}.")

#Task 3
print("-----Task3-----")
inventory["mango"] = (30, 0.6)
print(inventory)

#Task 4
print("-----Task4-----")
inventory["banana"] = (120, 0.2)
print(inventory)

#Task 5
print("-----Task5-----")
del inventory["pear"]
print(inventory)

print()
#Exercise 3 : Employee Records
print("-----Exercise3-----")
employees = [
("John Doe", "Accounting", "john.doe@example.com"),
("Jane Smith", "Marketing", "jane.smith@example.com"),
("Emily Davis", "HR", "emily.davis@example.com"),
("Michael Brown", "IT", "michael.brown@example.com")
]
#Task 1
print("-----Task1-----")
for item in employees:
    name = item[0]
    department = item[1]
    print(f"{name} is in {department} department.")

#Task 2 Print the email addresses of all employees in alphabetical order by their last names.
print("-----Task2-----")
name_list = []
for item in employees:
    name = item[0]
    name_list.append(name)
#print(name_list)
#sort name_list by the last name
name_list.sort(key=lambda name: name.split(" ")[-1].lower())
#print(name_list)
#create a dic with name:email
name_dic = {}
for item in employees:
    name = item[0]
    email = item[2]
    name_dic[name] = email
#print(name_dic)

for i in range(4) :
    name = name_list[i]
    email = name_dic[name_list[i]]
    print(f"{name}, {email}")

#Task 3
print("-----Task3-----")
new_employee = ("David Wilson", "Sales", "david.wilson@example.com")
employees.append(new_employee)
print(employees)
#Task 4
print("-----Task4-----")
department_dic = {}
for item in employees:
    name = item[0]
    department = item[1]
    department_dic[name] = department
#print(department_dic)
print(department_dic["Jane Smith"])


print()
#Exercise 4 : Book Library System
print("-----Exercise4-----")
library = {
"978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
"978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
"978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
"978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}
#Task 1
print("-----Task1-----")
for k,v in library.items():
    print(f"ISBN {k}, title {library[k]["title"]}, author {library[k]["author"]}, year {library[k]["year"]}.")

#Task 2
print("-----Task2-----")
print(library["978-0-14-028329-7"])

#Task 3
print("-----Task3-----")
library["978-1-4028-9462-6"] = {"title":"The Great Gatsby", "author":"F. Scott Fitzgerald", "year":"1925"}
print(library)

#Task 4
print("-----Task4-----")
library["978-0-7432-7356-5"] = {"title": "To Kill a Mockingbird","author": "Harper Lee", "year": 1961}
print(library)

#Task 5
print("-----Task5-----")
del library["978-0-452-28423-4"]
print(library)

print()
#Exercise 5 : City Population Data
print("-----Exercise5-----")
cities = {
"New York": 8419000,
"Los Angeles": 3980000,
"Chicago": 2716000,
"Houston": 2328000,
"Phoenix": 1690000
}
#Task 1
print("-----Task1-----")
for k, v in cities.items() :
    print(f"The population of {k} is {v}.")
#Task 2
print("-----Task2-----")
highest_city = max(cities, key = cities.get)
print(f"The city with the highest population is {highest_city} which has {cities[highest_city]} people.")
#Task 3
print("-----Task3-----")
lowest_city = min(cities, key = cities.get)
print(f"The city with the lowest population is {lowest_city} which has {cities[lowest_city]} people.")
#Task 4
print("-----Task4-----")
cities["Phoenix"] = 1700000
print(cities)
#Task 5
print("-----Task5-----")
cities["San Francisco"] = 884000
print(cities)


print()
#Exercise 6 : Movie Database
print("-----Exercise6-----")
movies = {
"Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
"The Godfather": {"year": 1972, "rating": 9.2, "genre":"Crime"},
"The Dark Knight": {"year": 2008, "rating": 9.0, "genre":"Action"},
"Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
"Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}
#Task 1
print("-----Task1-----")
for k, v in movies.items():
    print(f"{k}, year {movies[k]["year"]}, rating {movies[k]["rating"]}, genre {movies[k]["genre"]}.")

#Task 2
print("-----Task2-----")
new_dic = {}
for k, v in movies.items():
    new_dic[k] = movies[k]["rating"]
#print(new_dic)
print(max(new_dic, key = new_dic.get))

#Task 3
print("-----Task3-----")
movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}
print(movies)
#Task 4
print("-----Task4-----")
movies["Inception"]["rating"] = 9.0
print(movies)

#Task 5
print("-----Task5-----")
del movies["Pulp Fiction"]
print(movies)

print()
#Exercise 7 : Country Capitals
print("-----Exercise7-----")
countries = {
"USA": "Washington, D.C.",
"Canada": "Ottawa",
"France": "Paris",
"Germany": "Berlin",
"Japan": "Tokyo"
}
#Task 1
print("-----Task1-----")
for k, v in countries.items() :
    print(f"The capital of {k} is {v}.")
#Task 2
print("-----Task2-----")
print(countries["Germany"])
#Task 3
print("-----Task3-----")
countries["Australia"] = "Canberra"
print(countries)
#Task 4
print("-----Task4-----")
countries["USA"] = "New Washington"
print(countries)
#Task 5
print("-----Task5-----")
del countries["France"]
print(countries)

print()
#Exercise 8 : Shopping Cart
print("-----Exercise8-----")
cart = [
{"item": "apple", "quantity": 3, "price_per_unit": 0.5},
{"item": "banana", "quantity": 6, "price_per_unit": 0.2},
{"item": "orange", "quantity": 4, "price_per_unit": 0.3},
{"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]
#Task 1
print("-----Task1-----")
for i in range(4) :
    print(f"{cart[i]["item"]} with quantity {cart[i]["quantity"]} at each price ${cart[i]["price_per_unit"]}.")
#Task 2
print("-----Task2-----")
total_cost = 0
for i in range(4) :
    each_cost = cart[i]["quantity"] * cart[i]["price_per_unit"]
    total_cost += each_cost
print(f"${total_cost}")
#Task 3
print("-----Task3-----")
grape = {"item": "grape", "quantity": "5", "price_per_unit": "0.6"}
cart.append(grape)
print(cart)
#Task 4
print("-----Task4-----")
cart[1]["quantity"] = 10
print(cart)
#Task 5
print("-----Task5-----")
del cart[3]
print(cart)



print()
#Exercise 9 : Weather Data
print("-----Exercise9-----")
weather = {
"Monday": {"temperature": 20, "humidity": 60},
"Tuesday": {"temperature": 22, "humidity": 55},
"Wednesday": {"temperature": 19, "humidity": 65},
"Thursday": {"temperature": 23, "humidity": 50},
"Friday": {"temperature": 21, "humidity": 70}
}
#Task 1
print("-----Task1-----")
for k, v  in weather.items():
    print(f"The temperature of {k} is {weather[k]["temperature"]} degree and the humidity is {weather[k]["humidity"]}%." )
#Task 2
print("-----Task2-----")
temp_dic = {}
for k, v in weather.items() :
    temp_dic[k] = weather[k]["temperature"]
#print(temp_dic)
highest_temp_day = max(temp_dic, key = temp_dic.get)
highest_temp = temp_dic[highest_temp_day]
print(f"{highest_temp_day} has the highest temperature which is {highest_temp} degree.")
#Task 3
print("-----Task3-----")
hum_dic = {}
for k, v in weather.items() :
    hum_dic[k] = weather[k]["humidity"]
#print(hum_dic)
lowest_hum_day = min(hum_dic, key = hum_dic.get)
lowest_hum = hum_dic[lowest_hum_day]
print(f"{lowest_hum_day} has the lowest humidity which is {lowest_hum}%.")

#Task 4
print("-----Task4-----")
weather["Wednesday"]["temperature"] = 25
print(weather)
#Task 5
print("-----Task5-----")
weather["Saturday"] = {"temperature": 24, "humidity": 60}
print(weather)


print()
#Exercise 10 : Library Members
print("-----Exercise10-----")
members = [
{"name": "Alice", "age": 25, "books_borrowed": ["1984","To Kill a Mockingbird"]},
{"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
{"name": "Charlie", "age": 22, "books_borrowed": ["BraveNew World", "1984"]},
{"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
]
#Task 1
print("-----Task1-----")
for i in range(4) :
    name = members[i]["name"]
    age = members[i]["age"]
    print(f"{name}, {age} years old.")
#Task 2
print("-----Task2-----")
print(members[2]["books_borrowed"])
#Task 3
print("-----Task3-----")
new_member = {"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]}
members.append(new_member)
print(members)
#Task 4
print("-----Task4-----")
members[1]["age"] = 31
print(members)
#Task 5
print("-----Task5-----")
del members[3]
print(members)







































