# working with recursion is memory intensive, python has built-in
# limit, so we set this limit higher
import sys
sys.setrecursionlimit(10000)

reg_, test = input().split('|')

# compare a single character
def compare_char(reg, str) -> bool:
    return reg == str or bool(reg == '.' and str) or not reg

# compare two strings of equal length
def compare_string(reg, str):
    if not reg:
        return True
    elif not str:
        return False
    elif compare_char(reg[0], str[0]):
        return compare_string(reg[1:], str[1:])
    else:
        return False

# compare regex with longer strings
def regex(reg, str):
    if not reg:
        return True
    elif not str:
        return False
    elif compare_string(reg, str):
        return True
    else:
        return regex(reg, str[1:])


print(regex(reg_, test))
