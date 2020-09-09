# Medium python string problems -- 1 loop.. Use + to combine strings, len(str) is the number of chars in a String,
# str[i:j] extracts the substring starting at index i and running up to but not including index j.


# ----------------------------------------------------------------------------------------------------------------------
#
# Given a string, return a string where for every char in the original, there are two chars.
#
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    new = ""
    for char in str:
        new += char * 2
    return new


# ----------------------------------------------------------------------------------------------------------------------
#
#
# Return the number of times that the string "hi" appears anywhere in the given string.
#
#
# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
    return str.count("hi")


# ----------------------------------------------------------------------------------------------------------------------
#
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
#
#
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(str):
    return str.count("cat") == str.count("dog")


# ----------------------------------------------------------------------------------------------------------------------
#
# Return the number of times that the string "code" appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.
#
#
# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
    count = 0
    i = 0
    while "co" in str[i:]:
        if len(str[i + str[i:].index("co"):]) >= 4 and str[i + 3 + str[i:].index("co")] == "e":
            count += 1
        i += str[i:].index("co") + 3
    return count


# ----------------------------------------------------------------------------------------------------------------------
#
# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.
#
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    long_s, short_s = (a, b) if len(a) >= len(b) else (b, a)
    return long_s.lower().endswith(short_s.lower())


# ----------------------------------------------------------------------------------------------------------------------
#
# Return True if the given string contains an appearance of "xyz" where the xyz is not directly
# preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
#
#
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
    i = 0
    while "xyz" in str[i:]:
        if str[i - 1 + str[i:].index("xyz")] != ".":
            return True
        i += str[i:].index("xyz") + 2
    return False
