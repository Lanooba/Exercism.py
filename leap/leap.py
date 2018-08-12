def is_leap_year(year):
    remainder4 = year%4
    remainder100 = year%100
    remainder400 = year%400
    if remainder4 != 0: 
        return False
    elif remainder100 != 0 or remainder400 == 0:
        return True 
    elif remainder100 == 0 and remainder400 != 0:
        return False  
    
