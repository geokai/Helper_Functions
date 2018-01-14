"""A simple example using a simple arithmetic function to demostrate the use of
a 'try/except' error handling structure with the 'assert' functoin.
"""

def is_add(a, b, result):
    try:
        assert a + b == result
    except AssertionError:
        return f'{a} + {b} ≠ {result}'
    else:
        return f'{a} + {b} = {result}'
