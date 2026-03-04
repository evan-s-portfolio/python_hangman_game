# Create a dictionary to store the images for the hangman game. The key is the 
# number of incorrect guesses and the value is the image as text art. 
# The game is based on allowing a maximum of 7 incorrect guesses so if this is
# changed, the images will have to be updated.
# Note that for 0 there is no image and this is becuase if there are zero incorrect 
# guesses, there's no need to display an image. 
# Also, note that for 7 the "\" has to be escaped so that's why it's "\\" but it
# will display as "\".

hangman_images = {
    0: "",

    1: """
        _________
        |/      |
        |
        |
        |
        |
        |
        |
        |
    =========
        """,

    2: """
        _________
        |/      |
        |      ( )
        |
        |
        |
        |
        |
        |
    =========
        """,

    3: """
        _________
        |/      |
        |      ( )
        |       |
        |       |
        |
        |
        |
        |
    =========
        """,

    4: """
        _________
        |/      |
        |      ( )
        |       |
        |     --|
        |
        |
        |
        |
    =========
        """,

    5: """
        _________
        |/      |
        |      ( )
        |       |
        |     --|--
        |
        |
        |
        |
    =========
        """,

    6: """
        _________
        |/      |
        |      ( )
        |       |
        |     --|--
        |      /
        |     /
        |
        |
    =========
        """,

    7: """
        _________
        |/      |
        |      ( )
        |       |
        |     --|--
        |      / \\
        |     /   \\
        |
        |
    =========
        """
}