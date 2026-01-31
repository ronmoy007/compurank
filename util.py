def is_palindrome(str_to_evaluate):         # Palindrome is a word that can be read from left to right and viceversa and retains its meaning.
    is_palindrome = False                   
   
    cleaned = ""                            # We create a variable with an empty string where we will store the later result.
                                            # WE START CLEANING
    for char in str_to_evaluate.lower():    # Convert each caracter of the string to evaluate to lowercase.
        if char.isalnum():                  # Determine whether it is a letter or a number, or if it is a special character. If so, remove it.   
            cleaned += char                 # The result will be sent to the empty variable created previously.
                                            # WE COMPARE
    if cleaned == cleaned[::-1]:            # If the text of the empty string reads the same from left to right or viceversa.
            is_palindrome = True            # If so, then it states that it is a palindrome
    
    return is_palindrome                    # Returns the response to the program to indicate whether it is a palindrome


def is_fizzbuzz(number):                    # Classic exercise: if it is divisible by 3, return "Fizz"; if divisible by 5, return "Buzz"; if divisible by both, return "FizzBuzz"
    if isinstance(number, str):
        if not number.isdigit():
            return None
        number = int(number)

    if not isinstance (number, int):
        return None 
                                            # SPECIAL CASE
    if number == 0:                         # The test requires the result to be 0
      return 0                              # Returns the same value as the response
    
    if number % 3 == 0 and number % 5 == 0: # If both conditions are met, then return "FizzBuzz"
        return "FizzBuzz"
    elif number % 3 == 0:                   # If it is divisible by 3 and the remainder is 0
        return "Fizz"                       # then return "Fizz" 
    elif number % 5 == 0:                   # Same condition but with 5
        return "Buzz"                       # Return "Buzz"
    
    return number                           # It is not the special case 0, not divisible by 3 or 5, so return the same value



def is_prime(number):                       # Defines the function and receives the parameter
    if not isinstance(number, int):         # Checks if the parameter is an integer
        return None                         # If it is not, then return None
    
    if number <= 1:                         # If the parameter is less than or equal to one
        return False                        # Then return False
    
    for i in range (2,number):              # Divides the parameter by all numbers from 2 up to one before the parameter, in order
        if number % i == 0:                 # If the remainder is zero, then it is divisible by that number, therefore it is not prime
            return False                    # Since it is not prime, return False
        
    return True                             # If the above condition is never met, then it is prime. Therefore, return True


def is_leap_year(year):                     # Defines the function. Year is the value to be evaluated
    if not isinstance(year, int):           # Checks that the value is an integer
        return None                         # If it is not, then return None
    
    if year % 400 == 0:                     # If it is divisible by 400
        return True                         # Then it is a leap year
    
    if year % 100 == 0:                     # If it is divisible by 100
        return False                        # Then it is not a leap year
    
    if year % 4 == 0:                       # If it is divisible by 4
        return True                         # Then it is a leap yea
    
    return False                            # In any other case, it is not


def do_calculator(expression):
    pass


def generate_difference_between_dates(date1, date2, unit):
    pass


def vector_addition(vec1, vec2):
    pass


def vector_multiplication(vec, scalar):
    pass


def matrix_addition(mat1, mat2):
    pass


def matrix_multiplication(mat1, mat2):
    pass
