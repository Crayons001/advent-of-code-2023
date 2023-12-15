import re

regex1 = '\D*(\d)\w*(\d)' # Regex for finding callibrations for lines with 2 or more digits
regex2 = '^\D*(\d)\D*$'    # Regex for finding callibrations for lines with only one digit
callibrations = []

with open('/home/shem/projects/advent-of-code/day1/callibrations.txt', 'r') as file:
    content =  file.readlines()
    for line in content:
        result1 = re.search(regex1, line)
        result2 = re.search(regex2, line)

        if result1:
            callibration = f"{result1.group(1)}{result1.group(2)}" # Concatenating the first and last digit to form a two-digit string
        elif result2:
            callibration = f"{result2.group(1)}{result2.group(1)}" # Duplicating the single digit to form a two-digit string

        callibrations.append(int(callibration)) # Adding the value for each line to a list 
        
    print(sum(callibrations))
    
    
