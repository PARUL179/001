import re

txt = "The rain in spain"
x = re.search("^The.*Spain$", txt)
if x=='none':
    print('oops')
else:
    print('match')