# For loops
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for names in ["Adam", "Alex","Mariah","Martine","Columbus"]:
    print(names)

# Key
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for word in webster:
    print(webster[word])

# Control Flow and Looping
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number % 2 == 0:
        print(number)

# Lists + Functions
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count

# Create a dictionary
prices = {
  "banana": 4,
   "apple": 2,
   "orange": 1.5,
   "pear": 3,
}

# Create a stock
stock = {
  "banana": 6,
   "apple": 0,
   "orange": 32,
   "pear": 15,
}

# Keeping Track of the Produce
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for food in prices:
    print(food)
    print("price: %s" % prices[food])
    print("stock: %s" % stock[food])

# Something value
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

for key in prices:
   print(key)
   print("price: %s" % prices[key])
   print("stock: %s" % stock[key])

  total = 0
for item in prices:
     total += stock[item] * prices[item]
     print(total)

# Making a list
groceries = ["banana", "orange", "apple"]

# Making a Purchase
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        total = total + prices[item]
    return total

# Stocking Out
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total
print (compute_bill(shopping_list))

