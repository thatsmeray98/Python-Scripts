def search4letters(phrase:str, letters:str = 'aeiou') -> set:
    """Returns a set of the lettersfound in phrase

    Args:
        phrase (str): the phrase which is to be search for the letters
        letters (str, optional): the letters to be searched in the phrase. Defaults to 'aeiou' or vowels.

    Returns:
        set: the set of all the letters present in the phrase.
    """
    return set(letters).intersection(set(phrase))