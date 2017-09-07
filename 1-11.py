import re

def helper():
    str_test = input("input str:")
    m = re.findall("\w{1,15}@qq\.com",str_test)
    print(m)

helper()