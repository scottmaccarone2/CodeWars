"""
Description: A factory printer prints labels for boxes. The printer must use
colors named (for simplicity) with letters from 'a' to 'm'. For example:
'aaabbbbhaijjm' means the printer used three times color a, four times color b,
one time color h, etc. If there is a malfunction, a "bad" control string may
look like:
'aaaxbbbbyyyhwwawijjjxy'.

Goal: Write a function which returns the error rate of the printer AS A STRING.
"""

import string

def printer_error(s):
    alphabet = string.ascii_lowercase
    bad_letters = alphabet[13:]
    bad_count = 0
    for char in s:
        if char in bad_letters:
            bad_count += 1
    return str(bad_count) + "/" + str(len(s))

"""
There is a soother solution using regex. Other solutions incorporate the
.format() method. Another solution (which doesn't make sense to me because it
uses a comparision operator with 'm') looks similar to mine in concept.
"""
