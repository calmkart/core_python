import re

def helper():
    str_test = input("input str:")
    m = re.findall("([a-zA-Z]+(?<![\s,]))",str_test)
    print(m)

helper()