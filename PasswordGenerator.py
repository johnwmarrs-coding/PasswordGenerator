#Author: John Marrs

from random import randint

def generate_password(lower_case, upper_case, numbers, chars, length):

    #Creates lists for each charset, includes lowercase, uppercase, numbers, and special characters
    #Actual list content is defined in the loops
    cs_lc = []
    cs_uc = []
    cs_nums = []
    cs_chars = []
    for i in range(97, 123):
        cs_lc.append(chr(i)) 
    
    for i in range(65, 91):
        cs_uc.append(chr(i)) 
    
    for i in range(0, 10):
        cs_nums.append(str(i)) 
    
    for i in range(33, 48):
        cs_chars.append(chr(i)) 
        
    #Collection of all charsets for this password
    all_chars = []
    
    #adds each sub-charset to the all_chars charset if they are desired (sent as parameter)
    if lower_case:
        all_chars.append(cs_lc)
        
    if upper_case:
        all_chars.append(cs_uc)
        
    if numbers:
        all_chars.append(cs_nums)
        
    if chars:
        all_chars.append(cs_chars)
        
    #Generates a random password
    temp_password = ''
    for l in range(0, length):
        temp_set = all_chars[randint(0, len(all_chars)-1)]
        
        temp_password = temp_password + (temp_set[randint(0, len(temp_set)-1)])
        
        
    
    return temp_password
    
        