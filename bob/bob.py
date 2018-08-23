def hey(phrase):
    #This removes all whitespace from my input string
    clean_string = phrase.strip()

    #this runs the hey method to check if the phrase argument ends with a question mark
    if clean_string.endswith("?"):
        return ("Sure.")
    
    #this runs the hey method to check if the phrase argument ends with an exclamation mark
    elif clean_string.endswith("!") or up_check(clean_string) == True: 
        return ("Whoa, chill out!") 
    
    #this runs the hey method to check if the phrase argument ends with an exclamation mark
    # and is in uppercase
    elif clean_string.endswith("!") and up_check(clean_string) == True: 
        return ("Calm down, I know what I'm doing!") 
    
    #this runs the hey method to check if phrase does not match any of the stated conditions
    elif clean_string == "": 
        return ("Fine. Be that way!")   

    else: 
        return ("Whatever.")
    
def up_check(phrase):
    #if statement to check whether the phrase is uppercase
    if phrase.isupper():
        return True
    return False  

       
            
   #def up_check_loop(phrase):
    #for loop to check if each char in phrase is uppercase; duplicative but good for 
    #learning how to do a for loop
    #for phrase:
        #return True
    #return False         