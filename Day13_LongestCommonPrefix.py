def longest_common_prefix(strs):
    """
    Takes in a list of strings and returns the longest common prefix.
    :type strs: List[str]
    :rtype: str
    """
    output = ""
    if len(strs) == 0:
        return output
    check = strs[0]
    for idx in range(1, len(strs)):
        while check != strs[idx][:len(check)]:
            check = check[:-1]
            if not check:
                return ""
    return check
