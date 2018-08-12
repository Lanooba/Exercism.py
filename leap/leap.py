def is_leap_year(year):
    remainder4 = year%4
    remainder100 = year%100
    if remainder4 != 0: #and remainder100 !=0:
        return False
    
