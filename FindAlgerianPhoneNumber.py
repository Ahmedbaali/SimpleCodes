import re

def findFirstPhNum(text):
    f = re.compile(r'[+]213\d\d\d\d\d\d\d\d\d')
    return f.search(text)

def findAllPhNum(text):
    f = re.compile(r'[+]213\d\d\d\d\d\d\d\d\d')
    return f.findall(text)



message = input('Enter your message:')
q = input('if you want to find just the first number enter 1 if you want all numbers enter 2')
if(q == '1'):
    print(findFirstPhNum(message))
elif(q == '2'):
    print(findAllPhNum(message))
else:
    print("you didn't enter 1 or 2") 
    