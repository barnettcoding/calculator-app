import random
#                  To Do:
#              1. git push
#              2. input word list
#              3. change display to colored using html or css



#word_list = ["table", "point", "weary", "pills", "crate", "trace", "adieu", "angry", "reset", "taper", "great",
#"pound", "usual", "water", "bound", "rates", "stare", "lived", "quick", "share", "favor", "paper",
#            "lanes", "rated", "route", "super", "enjoy", "avoid", "input", "overt", "under", "yodel", "boxed"]

chosen_word = []
guess_count = 0
playing = True

solution_table = [[], [], [], [], [], [], []]
#print(solution_table)
with open('words3.txt', 'r') as f:
    word_list = f.readlines()
    
for lett in random.choice(word_list):
    chosen_word.append(lett)


def guess_word(guess):
    "docstring"
    global guess_count
    global solution_count
    letter_index = 0
    solution_count = 0
    for letter in guess:
        if letter == chosen_word[letter_index]:
            #solution_table[guess_count][letter_index] = letter.upper()
            solution_table[guess_count].append(letter.upper())
            #letter_index += 1
            solution_count += 1
            
        elif letter in chosen_word:
            #solution_table[guess_count][letter_index] = letter.lower()
            solution_table[guess_count].append(letter.lower())
            #letter_index += 1
        else:
            #solution_table[guess_count][letter_index] = "_ "
            solution_table[guess_count].append("_ ")
            #letter_index += 1
        letter_index += 1
    guess_count += 1
    check_winner()
 

               
def check_winner():
    "docstring"
    global playing
    if guess_count > 0:
        
        if solution_count == 5:
            playing = False
            print(f"You Won! You correctly guessed the word {''.join(chosen_word)} in {guess_count} guesses!")
            
            pass
        elif guess_count >= 6:
            playing = False
            print(f"You Lost! The word was {''.join(chosen_word)}")
        else:
            playing = True
    
while playing:
    print(solution_table)
    guess_word(input("Guess a 5 letter Word:   "))

