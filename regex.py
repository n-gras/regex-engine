reg_, test = input().split('|')

# at this point, only accepts 1 character and . as wildcard
def regex(reg, str) -> bool:
    return reg == str or bool(reg == '.' and str) or not reg

print(regex(reg_, test))
