import json
diction_of_cities = {}
new_diction_of_cities = {}

try:
    with open("cities_mapping.json") as city_map:
            diction_of_cities = json.load(city_map)
except:
    with open("cities_mapping.json", "w") as city_map:
        json.dump(diction_of_cities, city_map)   

for o, p in diction_of_cities.items():
    if o.isdigit():
        o = int(o)
        new_diction_of_cities[o] = p

diction_of_cities = new_diction_of_cities
            
def m():
    a = input("Do you want a list of cities?: ").title()
    if a == "Yes":
        print(diction_of_cities)
    else:
        print("okay")
        
m()

y = ""
while y != "0":
    y = input("Enter a number, or '0' to stop: ")
    if y != "0":
        if y.isdigit():
            y = int(y)
            if y in diction_of_cities:
                print(diction_of_cities[y])
            else:
                print("Your city is not registered")
                print("To register your city, Please follow the below instructions: ")
                x =  input("Please enter your city: ").strip().title()
                if x in diction_of_cities.values():
                    for a, b in diction_of_cities.items():
                        if b == x:
                            print("Your city is registered. This is the number assigned to your city: " + str(a))
                            break
                    print("You can choose to see the list of cities: ")
                    m()
                else:
                    c = len(diction_of_cities)
                    if c == 0:
                        diction_of_cities[c + 1] = x
                        print(x, "was added to the list and was assigned the number " + str(c + 1))
                    else:
                        z = (max(diction_of_cities.keys()))
                        diction_of_cities[z + 1] = x
                        print(x, "was added to the list and was assigned the number " + str(z + 1))
    else:
        print("Run terminated")
        with open("cities_mapping.json", "w") as city_map:
            json.dump(diction_of_cities, city_map)
            
            
            
            
            
            