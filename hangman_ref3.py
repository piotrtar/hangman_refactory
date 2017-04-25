import random #import random module
import time   #import time module
import datetime
from list1 import cac # import list of country and capitals
from hang import man #imports picture of hangman

def lose_word(lives, HANGMAN_picture, guess):
    if len(guess) == 1:
        lives -= 1
        HANGMAN_picture += 1
    else:
        lives -= 2
        HANGMAN_picture += 2

    print(man[HANGMAN_picture])
    print ("Wrong")
    print ("You have", + lives, 'more guesses')
    return (lives, HANGMAN_picture)

def get_dash_word(correct, word):
    seen_word = ''
    for i in word:           #Rule set for character
        if i in correct:
            seen_word += i
        else:
            seen_word += '_'

    return seen_word

def win_game( start, tries):         #Rule set for guested world
    won = True
    end = time.time()
    stop_game = float(end-start)
    print (name + " you WIN in " + str(tries) + " turns it took you", "%.2f"%(stop_game), "seconds" )

def lose_game(start, tries):
    end = time.time()
    stop_game = float(end-start)
    print (name + " you loose in " + str(tries) + " turns and it took you", "%.2f"%(stop_game), "seconds" )
    

def is_new_game(is_game_on):
    new_game = input("do you like to play again? Yes to confirm, anything to quit. ").lower()
    if (new_game != "yes"):
        is_game_on = False
    return is_game_on

def wrong_guess(guesses, used_letters, lives, HANGMAN_picture, guess):
    guesses += guess
    used_letters.append(guess)
    print('Used letters: ', used_letters)
    lives, HANGMAN_picture = lose_word(lives, HANGMAN_picture, guess)
    return lives, HANGMAN_picture
    
def main(tries, lives, used_letters, correct, HANGMAN_picture, is_game_on):
    part_on = True
    while part_on:
        hidden_words = 0            # The hidden words generate - symbol
        tries += 1
        print(get_dash_word(correct, word))
        
        guess = input("guess a character:").upper()  # Rule set what happen with single character
        if guess == word:
            win_game(start, tries)
            part_on = False
        else:
            if guess in used_letters or guess in correct:
                print("You already used this word")
            else:   
                if len(guess) == 1 and guess in word:
                    correct.append(guess)
                    print('Correct letters: ', correct)
                else:
                    lives, HANGMAN_picture = wrong_guess(guesses, used_letters, lives, HANGMAN_picture, guess)
                        
        if lives < 5:                                      #To get assistance
            print('It is the capital of ', assistance)               

        if get_dash_word(correct, word) == word:
            win_game(start, tries)      
            part_on = False
        elif lives <= 0:
            lose_game(start, tries)
            part_on = False

    is_game_on = is_new_game(is_game_on)    
    

name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
time.sleep(1)

is_game_on = True
while is_game_on:
    
    print ("Start guessing...")
    time.sleep(0.5)
    words = random.choice(cac)
    settings = {}

    word = words[1].upper()       #Taking the capital from prevous randomize
    assistance = words[0]        # prompt about the capital after 5 loses
    guesses = ''
    lives = 8                   #Seting the lives
    tries = 0                     # Starting calculate form 0 all moves
    start = time.time()            # start timer
    used_letters = []             # list of used letters
    correct = []
    HANGMAN_picture = 0

    date = datetime.date.today()
    
    main(tries, lives, used_letters, correct, HANGMAN_picture, is_game_on)


            
      


                
                
                    


            
        
        
