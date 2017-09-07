import re

def helper():
    str_test = input()
    m = re.findall('[bh][aui]t',str_test)
    print(m)
    return 1
    #m = re.search('[bh][aui]t',str_test)
    #print(m.groups())
    #return 1

helper()