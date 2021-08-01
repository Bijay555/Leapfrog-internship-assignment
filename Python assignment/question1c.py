# The dictionary  given below consists of vehicles and their weights in kilograms. Construct a list of the names of vehicles with weight below 5000 kilograms. In the same list comprehension makes the key names all uppercase.

dict1={
"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110
}

vehicle_list = [tuple([keys, dict1[keys]]) for keys in dict1 if dict1[keys] < 5000]
print(vehicle_list)