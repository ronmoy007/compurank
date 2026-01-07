from util import is_palindrome

# Test the is_palindrome function
def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("Racecar")
    assert not is_palindrome("hello")
    assert not is_palindrome("race a car")
    assert is_palindrome("A man, a plan, a canal: Panama")