def get_hangman_stage(tries):
    """
    This function creates a list of string for each
    element of the hangman. For a string
    to draw the handman I have used a multiline strings
    using triple quotes.
    The user will have a maximum of 6 lives.
    **READme Reference - for the stage design I have used
    codefather.tech.blog.com**
    """
    stages = [  # Stages are now ordered from full hangman to none
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
    return stages[tries]
