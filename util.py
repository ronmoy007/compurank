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


def is_fizzbuzz(number):
    pass


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
    
    # Multiplies each numeric element of a vector by a scalar.
    # Vec is a list of numeric values (int or float)
    # Scalar is a numeric value used to multiply each element
    # Return a new list with multiplied values, or None if an invalid element if found
    
    if not isinstance(scalar, (int, float)):    
        return None
    
    result = []                                 # List to store the resulting vector
    
    for i in vec:                               # Iterate through each element  in the vector
        if not isinstance (i, (int, float)):    # If the element is not numeric, return None
            return None
        
        # Multiply the element by the scalar and append it to the result list
        result.append (i * scalar)
        
    return result


def matrix_addition(mat1, mat2):
    pass


def matrix_multiplication(mat1, mat2):
    pass
