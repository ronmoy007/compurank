Run the tests with: `pytest`

If any test fails, output will be something like:

```bash
======================================================== test session starts =========================================================
platform darwin -- Python 3.10.12, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/marcojuliomonroyayala/Archivos_trabajo_local/compurank
plugins: anyio-4.3.0
collected 1 item                                                                                                                     

test_utils.py F                                                                                                                [100%]

============================================================== FAILURES ==============================================================
_________________________________________________________ test_is_palindrome _________________________________________________________

    def test_is_palindrome():
>       assert is_palindrome("racecar")
E       AssertionError: assert False
E        +  where False = is_palindrome('racecar')

test_utils.py:5: AssertionError
====================================================== short test summary info =======================================================
FAILED test_utils.py::test_is_palindrome - AssertionError: assert False
```

However, after fixing the issues, the output will be something like:

```bash
======================================================== test session starts =========================================================
platform darwin -- Python 3.10.12, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/marcojuliomonroyayala/Archivos_trabajo_local/compurank
plugins: anyio-4.3.0
collected 1 item                                                                                                                     

test_utils.py .                                                                                                                [100%]

========================================================= 1 passed in 0.00s ==========================================================
```