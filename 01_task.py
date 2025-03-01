print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
small_pepperoni = 2
medium_pepperoni = 3
large_pepperoni = 3
cheese_extra = 2

if size == 's' or size == 'S':
    print("small pizza is $15")
    bill = small_pizza
    if pepperoni == 'Y':
        bill = small_pizza + small_pepperoni
        print(f"your final bill is ${bill}")
    else:
        bill = small_pizza
    if  extra_cheese == 'Y':
        bill += cheese_extra
        print (f"you final bill is ${bill}")
elif size == 'm' or size == 'M':
    print("medium pizza is $20")
    bill = medium_pizza
    if pepperoni == 'Y':
        bill += medium_pepperoni
 #   else:
  #      bill = medium_pizza
    if extra_cheese == 'Y':
        bill += cheese_extra
    print(f"your final bill is ${bill}")
elif size == 'l' or size == 'L':
    print("large pizza is $25")
    bill = 25
    if pepperoni == 'Y':
        bill += large_pepperoni
      #  print(f"your bill is ${bill}")
  #  else:
   #     bill = large_pizza
    if extra_cheese == 'Y':
        bill += cheese_extra
    print(f"your final bill is ${bill}")