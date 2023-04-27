import re


def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    new_s = re.sub(r'[\W_]', '', s).lower()
    end = len(new_s) - 1
    start = 0
    while start < end:
        if new_s[start] == new_s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True
