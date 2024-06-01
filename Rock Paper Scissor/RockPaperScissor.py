'''
WORKFLOW:
  INPUT: Rock, Paper, Scissor
  Computer choose: computer will choose randomly
  Result print

  Cases: 
    A - Rock
      Rock - Rock = tie
      rock - paper = paper win
      rock - sciorror = Scissor win

    B - Paper
      Paper - Paper = tie
      paper - rock = paper win
      paper - scissor = scissor win

    c - Scissor
      Scissor - Scissor = tie
      sciorror - rock = rock win
      scissor - paper = scisor win
'''


import random

item_list = ['Rock', 'Paper', 'Scissor']

user_input = input("Enter your move = Rock, Paper, Scissor: ")
comp_choose = random.choice(item_list)

print(f"User choose = {user_input}, Computer choose = {comp_choose}")

# tie match 
if user_input == comp_choose:
  print("Match is tie due to same chooses")
# Case1:
elif user_input =='Rock':
  if comp_choose == 'Paper':
    print("Paper wins over Rock - Computer win")
  else:
    print('Rock wins over Scissor - You win')
# Case 2:
elif user_input == 'Paper':
  if comp_choose == 'Scissor':
    print('Scissor wins over Paper - Computer Wins')
  else:
    print("Paper wins over Scissor - You win")
# Case 3:
elif user_input == 'Scissor':
  if comp_choose == 'Paper':
    print("Scissor wins over Paper - You win")
  else:
    print("Rock wins over Paper - Computer wins")