def valid_palindrome(s, counts=0):
    """
    Takes in a string of lowercase characters and returns True if the string s can be a palindrome after deleting at
    most one character from it.
    :type s: str
    :type counts: int (counter of deleted characters)
    :rtype: bool
    """
    counter = counts
    start = 0
    end = len(s) - 1
    while end > start:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            if counter:
                return False
            else:
                counter += 1
                return valid_palindrome(s[start+1:end+1], counter) or valid_palindrome(s[start:end], counter)
    return True
