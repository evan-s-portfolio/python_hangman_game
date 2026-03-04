# Import files created for the game
import word_list as wl
import hangman_images as hi

# Import library functions
from string import ascii_lowercase
from random import choice

def play_game(player_name: str) -> bool:
    """ Plays a text based hangman game
        
        args:
        -----
        player_name: Name of the player
        
        returns:
        --------
        True if the player wins the game. False if the player loses the game.

    """

    # Welcome the player to the game
    print(f"\nHello {player_name}! Let's play hangman!.")

    # Flag to indicate if the player won the game by successfully guessing the word
    player_won = False

    # The maximum number of incorrect guesses allowed 
    max_incorrect_guesses = 7

    # The number of incorrect guesses made by the player
    num_incorrect_guesses = 0

    # List to keep track of the letters guessed by the player
    letters_guessed = []

    # Set the word to guess. The word_list.py file, which is imported at the top of this file, 
    # contains a list named words with 400 words. Randomly choose one of the words. 
    word_to_guess = choice(wl.words)

    # Create a variable to store a masked version of the word to guess and display it.
    # Each letter is an underscore followed by a space for readability so the player
    # knows how many letters are in the word. 
    word_to_guess_masked = "".join( ["_ " for i in range( len(word_to_guess) )] )
    print(f"\nWord to guess: {word_to_guess_masked}")

    # Now play the game! Keep playing until the word is guessed or the player reaches 
    # the maximum number of incorrect guesses.
    game_over = False
    while not game_over:
        # Ask the player to make a guess by entering a letter. The input needs to be
        # verified so a loop is used because the player may have to enter the guess 
        # again if it's incorrect.
        valid_input = False
        while not valid_input:
            # Ask the player to enter a letter
            letter_guess = input("\nPlease guess a letter: ")

            # Validate player entry. Check if:
            #   - The player didn't enter a letter (by pressing Enter)
            #   - The player entered more than one letter
            #   - The player didn't enter a lowercase letter (use ascii_lowercase to check this)
            #   - The player entered a letter previously guessed
            # If so, display an error message and then loop to prompt for input again. Otherwise,
            # the input is valid so set the flag to break out of the loop.
            if len(letter_guess) == 0:
                print("Please enter a letter")
            elif len(letter_guess) > 1:
                print("Please enter one letter only")
            elif letter_guess not in ascii_lowercase:
                print("Please enter a lowercase letter (a to z only)")
            elif letter_guess in letters_guessed:
                print("Please enter a letter you haven't already guessed")
            else:
                valid_input = True            

        # Input validated. Add the letter to the list of letters guessed. 
        letters_guessed.append(letter_guess)

        # Check if the letter guessed is in the word
        if letter_guess in word_to_guess:
            print(f"The letter {letter_guess} is in the word")

            # Reset word_to_guess_masked by iterating through the letters in word_to_guess. 
            # If a letter has been guessed, based on the letters_guessed list, display the letter.
            # Otherwise, display an underscore. Note that after each letter there is a space for 
            # readability so the player knows how many letters are in the word.
            word_to_guess_masked = " ".join( [letter if letter in letters_guessed else "_" for letter in word_to_guess] )

        else:
            print(f"The letter {letter_guess} is not in the word")

            num_incorrect_guesses += 1

            # No need to update word_to_guess_masked on an incorrect guess since there's no change

        # Display the masked word to guess
        print(f"\nWord to guess: {word_to_guess_masked}")

        # Display the letters guessed so far as a comma separated list
        list_of_letters_guessed = ", ".join(letters_guessed)
        print(f"Letters guessed: {list_of_letters_guessed}")

        # Check if the user has guessed the word. This can be done by checking if
        # word_to_guess_masked contains no "_" characters. If so, set flag to end game 
        # and set flag to indicate the player won the game.
        if "_" not in word_to_guess_masked:
            print(f"\nCongratulations {player_name}! You correctly guessed the word and won the game!\n")
            game_over = True
            player_won = True

        else:
            # Display hangman image. The hangman_images.py file, which is imported at the 
            # top of this file, contains a dictionary named hangman_images. The key is the 
            # number of incorrect guesses and the value is the image in text art. 
            print(f"{hi.hangman_images.get(num_incorrect_guesses)}")
            
            # Check whether the player has used up all the incorrect guesses allowed.
            # If so, set flag to end game.
            if num_incorrect_guesses == max_incorrect_guesses:
                print(f"\nGame over. You lost. Better luck next time {player_name}.\n")
                print(f"The word was '{word_to_guess}'.\n")
                game_over = True

    # Return value indicating if the player won the game
    return player_won


name = input("Please enter your name: ")
play_game(name)
