import re

def helper():
    str_test = input("input str:")
    m = re.findall("[a-zA-Z]+\s[a-zA-Z]+",str_test)
    print(m)
    return 1

helper()