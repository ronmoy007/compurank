from util import is_palindrome, is_fizzbuzz, is_prime, is_leap_year, do_calculator, generate_difference_between_dates, vector_addition, vector_multiplication, matrix_addition, matrix_multiplication

# Test the is_palindrome function
def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("Racecar")
    assert not is_palindrome("hello")
    assert not is_palindrome("race a car")
    assert is_palindrome("A man, a plan, a canal: Panama")


def test_is_fizzbuzz():
    assert is_fizzbuzz(3) == "Fizz"
    assert is_fizzbuzz(5) == "Buzz"
    assert is_fizzbuzz(15) == "FizzBuzz"
    assert is_fizzbuzz(7) == 7
    # Edge cases
    assert is_fizzbuzz(0) == 0
    assert is_fizzbuzz("15") == "FizzBuzz"
    assert is_fizzbuzz("x") == None


def test_is_prime():
    # Happy path
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    # Edge cases
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime("x") == None


def test_is_leap_year():
    # Happy path
    assert is_leap_year(2000) == True
    assert is_leap_year(2004) == True
    assert is_leap_year(2096) == True
    assert is_leap_year(2100) == False
    assert is_leap_year(2104) == True
    # Edge cases
    assert is_leap_year("x") == None

def test_do_calculator():
    # Happy path
    assert do_calculator("2+2") == 4
    assert do_calculator("2-2") == 0
    assert do_calculator("2*2") == 4
    assert do_calculator("2/2") == 1
    # Edge cases
    assert do_calculator("2+") == None
    assert do_calculator("+2") == None
    assert do_calculator("2") == None
    assert do_calculator("*") == None


def test_generate_difference_between_dates():
    # Happy path
    assert generate_difference_between_dates("1986-09-06", "2026-01-01", "years") == 39
    assert generate_difference_between_dates("1986-09-06", "2026-01-01", "months") == 471
    assert generate_difference_between_dates("1986-09-06", "2026-01-01", "days") == 14362
    # Edge cases
    assert generate_difference_between_dates("1986-09-06", "1986-09-06", "years") == 0
    assert generate_difference_between_dates("1986-09-06", "1986-09-06", "months") == 0
    assert generate_difference_between_dates("1986-09-06", "1986-09-06", "days") == 0
    # Invalid date formats
    assert generate_difference_between_dates("1986-09-06", "2026-01-01", "invalid") == None


def test_vector_addition():
    # Happy path
    assert vector_addition([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert vector_addition([1, 2, 3], [0, 0, 0]) == [1, 2, 3]
    # Edge case 1: Different lengths
    assert vector_addition([1, 2], [3, 4, 5]) == None
    # Edge case 2: Non-numeric values
    assert vector_addition([1, 2, 3], [4, 'five', 6]) == None


def test_vector_multiplication():
    # Happy path
    assert vector_multiplication([1, 2, 3], 2) == [2, 4, 6]
    assert vector_multiplication([1, 2, 3], 0) == [0, 0, 0]
    assert vector_multiplication([1, 2, 3], -1) == [-1, -2, -3]
    # Edge case 1: Non-numeric values
    assert vector_multiplication([1, 2, 3], 'two') == None
    assert vector_multiplication([1, 2, 3], [4, 5, 'six']) == None


def test_matrix_addition():
    # Happy path
    assert matrix_addition([[1, 2], 
                            [3, 4]], 
                                    [[5, 6], 
                                     [7, 8]]) == [[6, 8], 
                                                  [10, 12]]
    assert matrix_addition([[1, 2]], [[3, 4]]) == [[4, 6]]
    # Edge case 1: Incompatible dimensions
    assert matrix_addition([[1, 2]], 
                                    [[3], 
                                     [4]]) == None
    # Edge case 2: Non-numeric values
    assert matrix_addition([[1, 2]], 
                                    [[3, 4], 
                                     [5, 'six']]) == None

def test_matrix_multiplication():
    # Happy path
    assert matrix_multiplication([[1, 2],
                                  [3, 4]], 
                                         [[5, 6], 
                                          [7, 8]]) == [[19, 22],
                                                       [43, 50]]
    assert matrix_multiplication([[1, 2]], 
                                         [[3], 
                                          [4]]) == [[11]]
    # Edge case 1: Incompatible dimensions
    assert matrix_multiplication([[1, 2]], 
                                         [[3, 4]]) == None
    # Edge case 2: Non-numeric values
    assert matrix_multiplication([[1, 2]], 
                                        [[3, 4], 
                                         [5, 'six']]) == None

def test_oop_programing():
    from util import Person

    person1 = Person("Alice", "1986-09-06")
    person2 = Person("Bob", "1996-09-06")

    # Test attributes and methods
    assert isinstance(person1, Person)

    # assert only name is attribute
    for person in [person1, person2]:
        assert hasattr(person, "name")
        assert not hasattr(person, "age")

    assert person1.name == "Alice"
    assert person2.name == "Bob"

    assert person1.calculate_age_by_date("2026-01-01") == 39
    assert person2.calculate_age_by_date("2026-01-01") == 29

    assert person1.greet(person2) == "Hello Bob, I am Alice."    
    assert person1.greet("Not a person") == None
    
    from util import Employee

    employee1 = Employee("Charlie", "Software Engineer")
    employee2 = Employee("Dave", "Data Scientist")

    # Test attributes and methods
    assert isinstance(employee1, Employee)
    assert isinstance(employee2, Employee)
    assert employee1.name == "Charlie"
    assert employee2.name == "Dave"
    assert employee1.info() == "Charlie is working as a Software Engineer."
    assert employee2.info() == "Dave is working as a Data Scientist."


    