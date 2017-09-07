import re

def helper():
    str_test = input("input str:")
    m = re.findall("^www\.\w+\.com",str_test)
    print(m)

helper()