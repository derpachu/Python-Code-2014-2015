# Sample function definitions, including a test driver

def convert(n, b):
    """Returns the base b representation of integer n as a string
       Requires: n and b are non-negative integers and 0 < b <= 36"""

    result = ''              # calculate base b equivalent of n
    while (n != 0):
        x = n % b            # the remainder gives the next base-b 'digit'
        if x < 10:
            result = str(x) + result
        else:                # use upper case letter for digit, starting with "A"
            result = chr(55 + x) + result   # 'A' for 10, 'B' for 11, 'C' for 12, ...
        n = n // b

    if not result:
        result = '0'

    return result

def revert(s, b):
    """Returns the decimal equivalent of the base b number represented by s
       Requires: s is a string of base-b digits and
                 b is an integer with 0 < b <= 36 """
    result = 0
    for c in s:                # calculate the decimal equivalent of s base b
        if c.isdigit():
            d = int(c)
        else:
            d = ord(c) - 55    # the integer value contributed by a letter digit

        result = b * result + d

    return result

def test():
    """test driver: executes some tests of convert and revert"""

    OUT_TEMPL = '{}({}, {}) returned {}'
        
    n, b = 6, 2
    nstr1 = convert(11 - n, b)
    print(OUT_TEMPL.format('convert', 11 - n, b, nstr1))

    int1 = revert(nstr1, b)
    print(OUT_TEMPL.format('revert', nstr1, b, int1))

    nstr2 = convert(int1**3, b**4)
    print(OUT_TEMPL.format('convert', int1**3, b**4, nstr2))

    int2 = revert(nstr2, b**4)
    print(OUT_TEMPL.format('revert', nstr2, b**4, int2))



