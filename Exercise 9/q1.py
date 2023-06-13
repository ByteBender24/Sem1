# Create a dictionary with the city name and its corresponding pin code. Write a python
# code to retrieve the pin code given the city name. 

cities = {}

while True:
    choice = int(input('''Enter your choice.
    Enter 1 to enter cities.
    Enter 2 to stop
    '''))

    if choice == 2:
        break

    city = input("Enter city name: ")
    pin = int(input(f"Enter pincode of {city}: "))
    cities[city] = pin

print (cities)

print ("Enter city to name to retrieve pincode: ")
print (cities[input()])

