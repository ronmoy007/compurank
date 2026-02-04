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
    if len(vec1) != len(vec2):                                                      # Validates that both vectors have the same length
        return None                                                                 
    
    result = []                                                                     # Stores the resulting vector after element-wise addition
    
    for a, b in zip (vec1, vec2):                                                   # Iterates over both vectors simultaneously
        if not isinstance (a, (int, float)) or not isinstance(b, (int, float)):     # Ensures both elements are numeric values
            return None                                                             
        
        result.append(a+b)                                                          # Adds corresponding elements and appends the result
        
    return result                                                                   # Returns the resulting vector


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
    # Check that both matrices have the same number of rows                                                            
    if len(mat1) != len(mat2):                                                             
        return None
    
    # Initialize the result matrix as an empty list
    result = []                                                                             
    
    # Iterate through each pair of rows from both matrices
    for row1, row2, in zip (mat1, mat2):                  
        # Check that both rows have the same number of elements                                  
        if len (row1) != len(row2):                                                         
            return None
        
        # Initialize a new row to store the sum of elements
        row_result = []
        
         # Iterate through each pair of elements in the current rows
        for a, b, in zip (row1, row2):      
             # Validate that both elements are numeric                                                
            if not isinstance (a, (int, float)) or not isinstance (b, (int, float)):        
                return None
            
            # Add the elements and append the result to the new row
            row_result.append(a + b)                                                        
            
        # Append the completed row to the result matrix    
        result.append(row_result)                                                           
        
    # Return the resulting matrix after addition    
    return result                               
        

def matrix_multiplication(mat1, mat2):
    # Validate that inputs are non-empty lists
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None
    if not mat1 or not mat2:
        return None

    # Get matrix dimensions
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    rows_mat2 = len(mat2)
    cols_mat2 = len(mat2[0])

    # Validate matrix compatibility for multiplication
    if cols_mat1 != rows_mat2:
        return None

    # Validate that all rows have consistent lengths
    for row in mat1:
        if len(row) != cols_mat1:
            return None
    for row in mat2:
        if len(row) != cols_mat2:
            return None

    # Validate that all elements are numeric
    for row in mat1:
        for value in row:
            if not isinstance(value, (int, float)):
                return None

    for row in mat2:
        for value in row:
            if not isinstance(value, (int, float)):
                return None

    # Initialize result matrix with zeros
    result = []
    for i in range(rows_mat1):
        result.append([0] * cols_mat2)

    # Perform matrix multiplication
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result
