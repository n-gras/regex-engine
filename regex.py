# working with recursion is memory intensive, python has built-in
# limit of 1000, so we could set this limit higher
# import sys
# sys.setrecursionlimit(10000)


# compare a single character
def compare_char(reg, str_) -> bool:
    return reg == str_ or bool(reg == '.' and str_) or not reg


# compare two strings of equal length
def compare_string(reg, str_) -> bool:
    if not reg or (reg == '$' and not str_):  # check for end-pattern '$'
        return True                           # if regex is consumed by function, True
    elif not str_:
        return False                          # if str consumed but regex isn't, False

    # wildcards
    if len(reg) > 1:
        # escape sequence
        if reg[0] == "\\":
            return compare_string(reg[1:], str_[:])
        # '?' zero or one wildcard
        if reg[1] == '?':
            # case 1: 0 times,                   or case 2: 1 time
            return compare_string(reg[2:], str_) or compare_string(reg[2:], str_[1:])

        # '*' zero or more wildcard
        elif reg[1] == '*':
            # case 1: 0 times,                   or case 2: 1 time, then check again
            return compare_string(reg[2:], str_) or compare_string(reg, str_[1:])

        # '+' one or more wildcard
        elif reg[1] == '+' and compare_char(reg[0], str_[0]):
            # check if at least 1 time, then treat like '*'
            return compare_string(reg.replace('+', '*', 1), str_[1:])

    # regular character comparison
    if compare_char(reg[0], str_[0]):
        return compare_string(reg[1:], str_[1:])
    else:
        return False


# compare regex with longer strings
def regex(reg, str_) -> bool:
    if not reg:
        return True
    elif not str_:
        return False
    elif reg[0] == '^':  # check for begin-pattern '^'
        return compare_string(reg[1:], str_)
    elif compare_string(reg, str_):
        return True
    else:
        return regex(reg, str_[1:])


# Counter for amount of recursion happening - not really necessary just interesting
class Count_recur(object):
    def __init__(self, func_):
        self.func = func_
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.func(*args, **kwargs)


if __name__ == '__main__':
    # wrap regex functions in counter
    regex = Count_recur(regex)
    compare_string = Count_recur(compare_string)
    compare_char = Count_recur(compare_char)

    reg_, test = input().split('|')
    print(regex(reg_, test))
    # print('Regex has been called', regex.counter, 'times')
    # print('Compare_string has been called', compare_string.counter, 'times')
    # print('Compare_char has been called', compare_char.counter, 'times')
