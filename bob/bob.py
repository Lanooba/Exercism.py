def hey(phrase):
    #This removes all whitespace from my input string
    clean_string = phrase.strip()

    #this runs the hey method to check if the phrase argument ends with a question mark
    if clean_string.endswith("?") and all_upcheck(clean_string) == False:
        return ("Sure.")
    
    #this runs the hey method to check if the phrase argument ends with an exclamation mark
    #and is ALL  upper case
    elif all_upcheck(clean_string) == True and not clean_string.endswith("?"): 
        return ("Whoa, chill out!") 
    
    #this runs the hey method to check if the phrase argument ends with a question mark
    # and is in uppercase
    elif clean_string.endswith("?") and all_upcheck(clean_string) == True: 
        return ("Calm down, I know what I'm doing!") 
    
    #this runs the hey method to check if phrase does not match any of the stated conditions
    elif clean_string == "": 
        return ("Fine. Be that way!")   

    else: 
        return ("Whatever.")
    
def all_upcheck(phrase):
    #if statement to check whether the phrase is uppercase and returns true if it is
    if phrase.isupper():
        return True
    return False  

def one_upcheck(phrase):
     #for loop to check if each char in phrase is lowercase and return false if there is 
    for x in phrase:
        if x.islower():
            return False
        return True   
        