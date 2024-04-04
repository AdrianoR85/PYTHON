from random import choice
fruits = ["apple", "banana", "orange", "grape", "strawberry"]

def show():
  print('=' * 30)
  print(" Welcome to the Hangman game!")
  print('=' * 30)
  print("I am thinking of a word...")
  print("You have 6 chances to guess the word!")
  print("Good Luck!")
  print()

def hangman():
  show()
  secret_word = choice(fruits)
  chances = 6
  letters_found = ['_' for i in secret_word]

  while chances > 0:
    print(f"You have {chances} chances left!")
    print(f'Letters Found: {" ".join(letters_found)}')

    letter = input("\nEnter your letter: ").lower()

    if letter in secret_word:
      index = 0
      for l in secret_word:
          if l == letter:
              letters_found[index] = letter
          index += 1
    else:
      print('\nLetter not found')
      chances -= 1

    if "_" not in letters_found:
      print("\nYou Win!")
      break
  
  if "_" in letters_found:
    print("\nYou Lose!")
    print("\nThe secret word is: {secret_word}")

if __name__ == "__main__":
    hangman()
