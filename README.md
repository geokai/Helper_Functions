## A collection of Python helper functions

### pad_num():

This helper function takes a number (integer or float) and pads out with
zeros to the left if the digit count is less than the 'pad' number specified.
- There is as yet no error handling for non numerical strings.
- If a float is passed, the decimal point is counted as the total character
  count. For example, '3.4' with a pad=4 will return '03.4'
