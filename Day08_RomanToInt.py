def roman_to_int(s):
    """
    Takes a string of roman numerals and returns the corresponding integer according to known roman numeral rules
    (s) contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    :type s: str
    :rtype: int
    """
    mapper = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = len(s) - 1
    integer = mapper[s[i]]
    if i == 0:
        return integer
    i -= 1
    while i >= 0:
        if mapper[s[i]] < mapper[s[i + 1]]:
            integer -= mapper[s[i]]
        else:
            integer += mapper[s[i]]
        i -= 1
    return integer
