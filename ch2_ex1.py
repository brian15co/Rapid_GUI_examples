def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    takes in a text string and returns a list of characters from the
    text string that are contained within the valid string
    """
    
    assert text, chars
    
    validString = ""
    for char in text:
        if char in chars:
            validString += char
    
    print validString
    
valid('richard', "aeiou")