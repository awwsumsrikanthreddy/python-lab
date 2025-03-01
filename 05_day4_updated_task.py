rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
user_input = int(input("enter 0 for rock, 1 for paper and 2 for scissors: "))
computer_input = int(random.choice(['0','1','2']))

print(f"You entered: {user_input}")
if user_input == 0:
    print (f"{rock}")
elif user_input == 1:
    print (f"{paper}")
elif user_input == 2:
    print(f"{scissors}")
else:
    print (f"please use only 0,1,2")

if user_input >= 3:
    print("invalid choice")
    exit()
print("Computer chose:")
if computer_input == 0:
    print (f"{rock}")
elif computer_input == 1:
    print (f"{paper}")
elif computer_input == 2:
    print (f"{scissors}")

# game logic

if computer_input == user_input:
    print("try again")
elif user_input == 0 and computer_input == 1:
    print(f"computer wins")
elif user_input == 0 and computer_input == 2:
    print (f"user wins")
elif user_input == 1 and computer_input == 0:
    print(f"user wins")
elif user_input == 1 and computer_input == 2:
    print (f"computer wins")
elif user_input == 2 and computer_input == 0:
    print (f"computer wins")
elif user_input == 2 and computer_input == 1:
    print (f"user wins")
elif user_input >= 3:
    print ("please use a valid number")

