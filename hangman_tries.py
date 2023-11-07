def get_hangman_stage(tries):
    """
    This function creates a list of string for each element of the hangman. For a string
    to draw the handman I have used a multiline strings using triple quotes.     
    The user will have a maximum of 6 lives. 
    **READme Reference - for the stage design I have used codefather.tech.blog.com**
    """
    stages = [# Stages are now ordered from full hangman to none
        # Stage 0: Final stage with full hangman
        """
            ------
            |    |
            |    O
            |  --|--
            |    |
            |   / \\
            |
        ------------
        """,
        # Stage 1
        """
            ------
            |    |
            |    O
            |  --|
            |    |
            |   / \\
            |
        ------------
        """,
        # Stage 2
        """
            ------
            |    |
            |    O
            |    |
            |    |
            |   / \\
            |
        ------------
        """,
        # Stage 3
        """
            ------
            |    |
            |    O
            |    |
            |    |
            |   /
            |
        ------------
        """,
        # Stage 4
        """
            ------
            |    |
            |    O
            |    |
            |    |
            |
            |
        ------------
        """,
        # Stage 5
        """
            ------
            |    |
            |    O
            |
            |
            |
            |
        ------------
        """,
        # Stage 6: First stage with only the head
        """
            ------
            |    |
            |
            |
            |
            |
            |
        ------------
        """
    ]
    return stages[tries] #Use the number of tries left as the index