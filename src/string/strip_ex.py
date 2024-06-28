# strip() method - Remove the leading and trailing characters (whitespace by default)
# lstrip() - Removing Leading characters (whitespace by default) from Strings
# rstrip() - Removing Trailing characters (whitespace by default) from Strings

str1 = "000abcd0sam0001230000"
print(str1.strip('0'))               # abcd0sam000123

str2 = "   Sam  Lin       "
print("[{}]".format(str2.strip()))   # [Sam  Lin]
print("[{}]".format(str2.lstrip()))  # [Sam  Lin       ]
print("[{}]".format(str2.rstrip()))  # [   Sam  Lin]
