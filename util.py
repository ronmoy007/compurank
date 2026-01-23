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
    try:
        num = int(number)                   # Tries to execute the code; if an error occurs, it will jump to the except block
    except (ValueError, TypeError):         # ValueError when it cannot be converted. TypeError when the type is incompatible.
        return None                         # If the above occurs, then the function ends 
                                            # SPECIAL CASE
    if num == 0:                            # The test requires the result to be 0
      return 0                              # Returns the same value as the response
    
    if num % 3 == 0 and num % 5 == 0:       # If both conditions are met, then return "FizzBuzz"
        return "FizzBuzz"
    elif num % 3 == 0:                      # If it is divisible by 3 and the remainder is 0
        return "Fizz"                       # then return "Fizz" 
    elif num % 5 == 0:                      # Same condition but with 5
        return "Buzz"                       # Return "Buzz"
    
    return num                              # It is not the special case 0, not divisible by 3 or 5, so return the same value


def is_prime(number):
    pass


def is_leap_year(year):
    pass


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
