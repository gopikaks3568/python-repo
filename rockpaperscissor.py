import random as r

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

choice = int(
    input(
        "What do you choose?Type 0 for rock, type 1 for paper, type 2 for scissor "
    ))
cpu_choice = r.randint(0, 2)
if choice == 0:
    print("User's Choice")
    print(rock)
elif choice == 1:
    print("User's choice")
    print(paper)
else:
    print("User's choice")
    print(scissors)
if cpu_choice == 0:
    print("Computer choice")
    print(rock)
elif cpu_choice == 1:
    print("Computer's chocie")
    print(paper)
else:
    print("Computer's choice")
    print(scissors)
if choice == cpu_choice:
    print("Draw")
elif choice == 0 and cpu_choice == 2 or choice == 1 and cpu_choice == 0 or choice == 2 and cpu_choice == 1:
    print("you won!!!!")
else:
    print("You lose!!!")
