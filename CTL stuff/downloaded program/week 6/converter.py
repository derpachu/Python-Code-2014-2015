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
def test_driver(z):
    """input a file name"""
    Input_file = open(z, "r")
    Output_file = open("outData.txt", "w")
    for line in Input_file:
        x = int(line[:6])
        y = int(line[6:])
        f = convert(x,y)
        e = str(f)
        g = revert(e,y)

        OUT_TEMPL = '{}({}, {}) returned {}'

        print(OUT_TEMPL.format('convert', x, y, f), file=Output_file)
        print(OUT_TEMPL.format('revert', e, y, g), file=Output_file)
        
    Output_file.close()
    Input_file.close()
test_driver("testData.txt")
