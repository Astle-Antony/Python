import random
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
human_choice = str(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if human_choice == "0":
    print("You chose Rock!")
    print(rock)
    computer = random.randint(0,2)
    if computer == 0:
        print("Computer chose Rock!")
        print(rock)
        print("result: Draw")
    elif computer == 1:
        print("Computer chose Paper!")
        print(paper)
        print("result: You lose")
    else:
        print("Computer chose Scissors!")
        print(scissors)
        print("result: You win")
elif human_choice == "1":
    computer = random.randint(0, 2)
    print("You chose Paper!")
    print(paper)
    if computer == 0:
        print("Computer chose Rock!")
        print(rock)
        print("result: You win")
    elif computer == 1:
        print("Computer chose Paper!")
        print(paper)
        print("result: Draw")
    else:
        print("Computer chose Scissors!")
        print(scissors)
        print("result: You lose")
else:
    print("You chose Scissors!")
    print(scissors)
    computer = random.randint(0, 2)
    if computer == 0:
        print("Computer chose Rock!")
        print(rock)
        print("result: You lose")
    elif computer == 1:
        print("Computer chose Paper!")
        print(paper)
        print("result: You win")
    else:
        print("Computer chose Scissors!")
        print(scissors)
        print("result: Draw")




