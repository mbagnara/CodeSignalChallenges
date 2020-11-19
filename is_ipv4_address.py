import re

def isIPv4Address(inputString):

    # Reg expression to check IPv4 address
    regex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

    '''
        re.fullmatch(pattern, string, flags=0)

        If the whole string matches the regular expression pattern, return a corresponding match object. Return None if the string does not match the pattern; note that this is different from a zero-length match.

        Ref: https://docs.python.org/3/library/re.html
    '''
    matches = re.fullmatch(regex, inputString)

    # If matches does not meet the regular expression, it will raise the AttributeError exception
    try:
        _ = matches.string
    except AttributeError:
        return False

    # inputString is IPV4 address
    return matches.string == inputString


test_str = "25.24.0.0"
print(isIPv4Address(test_str))
