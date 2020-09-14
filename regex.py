reg_, test = input().split('|')

def regex(reg, str) -> bool:
    return reg == str or bool(reg == '.' and str) or not reg

print(regex(reg_, test))
