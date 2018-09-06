from sys import argv
script, str = argv
operators='+-*/'
index=0
for i in operators:
    index = max(index, str.find(i))
a = str[:index]  
b = str[(index+1):]
op = str[index]
if op == '+':
    print float(a) + float(b)
elif op == '-':
    print float(a)  - float(b)
elif op == '*':
    print float(a) * float(b)
else:
    print float(a)/float(b)
