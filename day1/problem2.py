import re

# Regex for finding callibrations for each line (with more than one digit or word)
regex1 = '(one|two|three|four|five|six|seven|eight|nine|\d)\w*(one|two|three|four|five|six|seven|eight|nine|\d)'
# Regex for finding callibrations for lines with one figure (either digit or word)
regex2 = '^\w*(one|two|three|four|five|six|seven|eight|nine|\d)\w*$'

callibrations = []  # List for storing all extracted callibrations as integers

# Dictionary for converting non-digit words to digits
numbers_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('/home/shem/projects/advent-of-code/day1/callibrations.txt', 'r') as file:
    content =  file.readlines()
    for line in content:
        result1 = re.search(regex1, line)
        result2 = re.search(regex2, line)

        if result1:
            firstDigit = result1.group(1)
            secondDigit = result1.group(2)

            if firstDigit.isalpha():
                firstDigit = numbers_dict[firstDigit]
            if secondDigit.isalpha():
                secondDigit = numbers_dict[secondDigit]

            callibration = f"{firstDigit}{secondDigit}"

        elif result2:
            onlyDigit = result2.group(1)
            if onlyDigit.isalpha():
                onlyDigit = numbers_dict[onlyDigit]

            callibration = f"{onlyDigit}{onlyDigit}"

        callibrations.append(int(callibration)) # Adding the value for each line to a list 
        
    print(sum(callibrations))
    
    
