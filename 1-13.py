import re

def helper():
    str_test = str(type(dir))
    print(str_test)
    m = re.findall("(?<=<class\s')[\w_]+(?='>)",str_test)
    print(m)

helper()