def hey(phrase):
    #this runs the hey method to check if the phrase argument ends with a question mark
    if phrase.endswith("?"):
        return ("Sure.")
    
    #this runs the hey method to check if the phrase argument ends with an exclamation mark
    elif phrase.endswith("!") or up_check == True: 
        return ("Whoa, chill out!") 
    
    #this runs the hey method to check if the phrase argument ends with an exclamation mark
    # and is in uppercase
    elif phrase.endswith("!") and up_check == True: 
        return ("Calm down, I know what I'm doing!") 
    
    #this runs the hey method to check if phrase does not match any of the stated conditions
    elif space_check == True: 
        return ("Fine. Be that way!")   

    else: 
        return ("Whatever.")
    
def up_check(phrase):
    #if statement to check whether the phrase is uppercase
    if phrase.isupper():
        return True
    return False  

def space_check(phrase):
    #if statement to check whether the phrase contains nothing but whitespace and returns
    #true if there is
    if phrase.isspace():
        return True
    return False 
       
            
   #def up_check_loop(phrase):
    #for loop to check if each char in phrase is uppercase; duplicative but good for 
    #learning how to do a for loop
    #for phrase:
        #return True
    #return False         