"""
This is a test file for python programming.
Extended text for documentation.
"""
print("Boring Ventures: Varables,Lists,& Dictionaries");

# Setting Basic Variables

car = "BMW"
car_owner = "Enock Kipkoech"
car_owner_age =25
owner_milage = 100001.5
total_miles_covered = car_owner_age * owner_milage
print(car, car_owner, car_owner_age, owner_milage, total_miles_covered)
print(type(car_owner_age))

# Setting Advanced Variables
cars_list = ["bmw","mercedes","porche","audi"] #Array  in JS | List
# print(type(cars_list))
print(cars_list)

# Dictionaries / Object in JS
cars_dict={
    "CAR":11
}

print(cars_dict)
print(type(cars_dict))

car_dict1 ={
    "car":"bmw",
    "age":20,
    "usd_value":30000
}
print(car_dict1["age"])

car_dict2 ={
    "car":"audi",
    "age":10,
    "usd_value":70000
}
print(car_dict1["age"])

car_dict3 ={
    "car":"porche",
    "age":2,
    "usd_value":100000
}
print(car_dict1["age"])

# collection

cars_obj_list=[car_dict1, car_dict2,car_dict3]
print(cars_obj_list)

# Access List Information
print(cars_obj_list[0]["usd_value"])


# if statement
if cars_list[0] == "bmw":
  print("Yes.Identified!")
elif cars_list[1] == "mercedes":
  print("Wozaa! Found Merc!")
else:
  print("Nope. Try again!")

# if statement breaking into many ifs
if cars_list[0] =="audi":
  print("Wolan, BIMA")

if cars_list[1] == "mercedes":
  print("marc Benz!")  

 #Tarnary if statement 
print("Wozaa Porche") if cars_list[2] == "porche" else print("Nope! Not That!")

cars_list # another way to print
will_purchase = "yes" if cars_list[0] == "bmw" else "no"
print(will_purchase)

# Real use case
threshold = 1.5
real_rate = 0.8
real_rate >= threshold

if real_rate >= threshold:
  print(real_rate)

# For Loop
print(cars_obj_list)
for item in cars_obj_list:
  # check car age
  if item['age'] > 2:
    print(item)


# While loop
counts = 0
while counts < 10:
  counts += 1 #counts + 1
  print(counts)


# While loop with break & cool down
import time
counts = 0

while True:
  time.sleep(2)
  counts = counts + 1
  print(counts)
  if counts == 5:
    break  

# Operations AND and OR (BOOLEANS)
car_age_ok = False
driver_cleared = False
car_age = 20
driver_experience = "strong"

if car_age_ok == True and driver_cleared == True:
  print("Good to Go!")
else:
  print("Sorry,no Go!")

if car_age <= 20 or driver_experience == "strong":
  print("You can Drive")
else:
  print("Can't Drive")


# GETTING DATA
import requests
import json

req = requests.get("https://api.poloniex.com/markets/price")
json_obj = json.loads(req.text)
print(json_obj[0])

# Loop through data
for day in json_obj:
  print(json_obj[1])

  # Many Requests  (API) 
symbol = "BTC_ETH"
req = requests.get("https://api.poloniex.com/markets/BTS_BTC/orderBook")
json_obj = json.loads(req.text)
print(json_obj["asks"])

# Methods & Functions - Reusable Code

import requests
import json

# method aka function
def get_api_data(url):
  req = requests.get(url)
  if req.status_code == 200:
    return json.loads(req.text)
  else:
    return 0  


  # Reusing the method 
poloniex_markets= get_api_data("https://api.poloniex.com/markets")
print(poloniex_markets[0])

poloniex_ticker24 = get_api_data("https://api.poloniex.com/markets/BTS_BTC/ticker24h")
print(poloniex_ticker24)

poloniex_orderBook = get_api_data("https://api.poloniex.com/markets/BTS_BTC/orderBook")
print(poloniex_orderBook) 

# more methods exapmles

def multiply_by_number(num):
  return num * 10

multiply_by_number(10)