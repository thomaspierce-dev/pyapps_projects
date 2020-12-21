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

rps = [rock, paper, scissors]
computer = random.choice(rps)
choice = int(input("Pick a weapon: 1 - rock, 2 - paper, 3 - scissors: "))

person_choice = rps[choice - 1]
computer_choice = computer

print(person_choice, "Your Choice")
print(computer_choice, "Computer Choice")
print("")

if person_choice == rock and computer_choice == scissors:
  print("You Win!")
if person_choice == scissors and computer_choice == paper:
  print("You Win!")
if person_choice == paper and computer_choice == rock:
  print("You Win!")
if computer_choice == rock and person_choice == scissors:
  print("Computer Wins!")
if computer_choice == scissors and person_choice == paper:
  print("Computer Wins!")
if computer_choice == paper and person_choice == rock:
  print("Computer Wins!")
if computer_choice == rock and person_choice == rock:
  print("It's a Tie!")
if computer_choice == scissors and person_choice == scissors:
  print("It's a Tie!")
if computer_choice == paper and person_choice == paper:
  print("It's a Tie!")

'''
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
'''