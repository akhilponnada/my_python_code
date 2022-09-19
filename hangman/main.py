import random as rd
from logo import logo, stages
print(logo)

#list of words for the game.
from words import word_list

#lives
lives = 6

#generating random word from the list using random module.
random_word = rd.choice(word_list)

#setting word length to length of the random word
word_length = len(random_word)

#setting an empty list.
display_list = []


#adding "_" to the list for every letter in the random word.
for letter in range(word_length):
  display_list.append("_")

#creating a new variable to set game over as false as long as ther are no "_" left in the list.
game_over = False

# looping as long as there are no "_" in the list and replacing with user choice.
while not game_over:
  guessed_letter = str(input("Guess a letter: ")).lower()

  if guessed_letter in display_list:
    print("you've already guessed this letter.")

  # for every position of the letter in random word we are looping, replacing with correct letter.
  for item in range(word_length):
    letter = random_word[item]
    if letter == guessed_letter:
      display_list[item] = letter
      
  if guessed_letter not in random_word:
    print("you guesssed a wrong letter so you lose a life.")
    lives -= 1
    if lives == 0:
      game_over = True
      print("Your lives are over and you lose.")
  print(f"lookout for the hangman: {stages[lives]} ")
      
  print(display_list)
  # setting the game over to true after there are no "_" in list.
  if not "_" in display_list:
    game_over = True

    print("You win! Good Job")


